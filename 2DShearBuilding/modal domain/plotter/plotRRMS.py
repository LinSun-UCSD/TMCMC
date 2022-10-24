import numpy as np
import pickle


def compute_RRMS(true, est):
    RRMS = np.sqrt(np.mean(np.power(np.subtract(true, est), 2))) / np.sqrt(np.mean(np.power(true, 2)))
    return RRMS


def plotRRMS(pickleFileName, stages, samples, trueValues, h_measurement_eqn, measure_vector, k0, GMinput):
    with open(pickleFileName, 'rb') as handle1:
        mytrace = pickle.load(handle1)
    TrueResponse = h_measurement_eqn(trueValues, GMinput, 1,
                                     GMinput["totalStep"], measure_vector, k0)
    rrms = []
    for stage in stages:
        tempRRMS = np.zeros((len(samples), TrueResponse.shape[1]))
        for i in range(len(samples)):
            sample = samples[i]
            tempResponse = h_measurement_eqn(mytrace[stage][0][sample, :], GMinput, 1,
                                             GMinput["totalStep"], measure_vector, k0)

            for j in range(tempResponse.shape[1]):
                tempRRMS[i, j] = compute_RRMS(tempResponse[:, j], TrueResponse[:, j])
        rrms.append(tempRRMS)
    return rrms
