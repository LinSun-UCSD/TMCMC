import numpy as np
from get_mass import get_mass
from get_stiffness import get_stiffness
from get_classical_damping import get_classical_damping
from get_continuous_state_space import get_continuous_state_space
from get_response_state_space import get_response_state_space
from compute_response_SPs import compute_response_SPs
from multiprocessing import Pool


def h_measurement_eqn(parameter_SP, GMinput, StepUpdateSize, UpdateNum, measure_vector, k0):
    input_path = GMinput["path"]
    filename = GMinput["filename"]
    fs = GMinput["fs"]
    num_SP = parameter_SP.shape[1]
    # input K, M and C
    DOF = 8
    m0 = 625000
    M_global = get_mass(m0, DOF)
    c0 = 400000
    damping = {
        "mode": np.array([1, 3]),
        "ratio": np.array([0.05, 0.05])
    }
    B = np.ones((DOF, 1))
    # load the input
    temp = np.loadtxt(input_path + "/" + filename + ".txt", dtype=float)
    a = temp[2:temp.shape[0]] * 9.81

    # compute the response

    output_type = ["abs", "rel"]
    if num_SP > 1:
        step = StepUpdateSize * (UpdateNum+1)
        temp = np.zeros((len(measure_vector[0]), step, num_SP))
        t = np.arange(0, step, 1) / fs
        response = np.zeros((len(measure_vector[0])*StepUpdateSize, num_SP))
        for i in range(num_SP):
            K_global = get_stiffness(parameter_SP[:, i], DOF,measure_vector, k0)
            C_global, _, _, _ = get_classical_damping(K_global, M_global, damping, "no")
            Ac, Bc, Cc, Dc = get_continuous_state_space(K_global, M_global, C_global, B, output_type[0])
            temp1, _, _, _, _, _ = get_response_state_space(Ac, Bc, Cc, Dc, a[0: step], t)
            temp1 = temp1[measure_vector, :]
            temp[:, :, i] = temp1
        # toPass = [(parameter_SP[:, i], M_global, damping, DOF, B, output_type, step, a, t) for i in range(parameter_SP.shape[1])]
        # if __name__ == 'h_measurement_eqn':
        #     pool = Pool(processes=8)
        #     results = pool.starmap(compute_response_SPs, toPass)
        #     pool.close()
        # for i in range(results):
        #     temp[:, :, i] = results[i]
        for j in range(num_SP):
            if StepUpdateSize == 1:
                temp1 = temp[:, temp.shape[1]-1, j]
                response[:, j] = temp1
            else:
                temp1 = temp[:, temp.shape[1]-1-(StepUpdateSize-1):temp.shape[1]-1+1, j]
                temp2 = np.reshape(np.transpose(temp1), (StepUpdateSize*temp.shape[0], 1))
                response[:, j] = temp2.reshape((temp2.shape[0],))
    elif num_SP == 1:
        step = StepUpdateSize * UpdateNum
        temp = np.zeros((DOF, step, num_SP))
        t = np.arange(0, step, 1) / fs
        K_global = get_stiffness(parameter_SP, DOF, measure_vector, k0)
        C_global, _, _, _ = get_classical_damping(K_global, M_global, damping, "no")
        Ac, Bc, Cc, Dc = get_continuous_state_space(K_global, M_global, C_global, B, output_type[0])
        temp, _, _, _, _, _ = get_response_state_space(Ac, Bc, Cc, Dc, a[0:step], t)
        temp = temp[measure_vector, :]
        response = np.transpose(temp[0])
    return response
