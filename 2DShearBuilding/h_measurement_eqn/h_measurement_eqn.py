import numpy as np
from .get_mass import get_mass
from .get_stiffness import get_stiffness
from .get_classical_damping import get_classical_damping
from .get_continuous_state_space import get_continuous_state_space
from .get_response_state_space import get_response_state_space



def h_measurement_eqn(parameter_SP, GMinput, StepUpdateSize, UpdateNum, measure_vector, k0):
    input_path = GMinput["path"]
    filename = GMinput["filename"]
    fs = GMinput["fs"]
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


    step = StepUpdateSize * UpdateNum
    t = np.arange(0, step, 1) / fs
    K_global = get_stiffness(parameter_SP, DOF, measure_vector, k0)
    C_global, _, _, _ = get_classical_damping(K_global, M_global, damping, "no")
    Ac, Bc, Cc, Dc = get_continuous_state_space(K_global, M_global, C_global, B, output_type[0])
    temp, _, _, _, _, _ = get_response_state_space(Ac, Bc, Cc, Dc, a[0:step], t)
    temp = temp[measure_vector, :]
    response = np.transpose(temp[0])
    return response
