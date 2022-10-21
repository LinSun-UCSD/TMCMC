"""
@author: Lin Sun
email: lsun@ucsd.edu
main file to test transitional mcmc implementation
example: 8DOF system

"""
import numpy as np
import pickle
from tmcmc_mod import pdfs
from tmcmc_mod.tmcmc import run_tmcmc
import os as os
from h_measurement_eqn.h_measurement_eqn import h_measurement_eqn
from h_measurement_eqn.ismember import ismember
from h_measurement_eqn.normalize import normalize
import matplotlib.pyplot as plt

# choose 'multiprocessing' for local workstation or 'mpi' for supercomputer
parallel_processing = 'multiprocessing'

# measurement data:
g = 9.81  # gravity acceleration
# ground motion input
GMinput = {
    "totalStep": 1000,  # earthquake record stpes
    "fs": 50,  # sampling rate
    "filename": 'NORTHR_SYL090',  # the earthquake file to load
    "path": os.getcwd() + "\\earthquake record"  # earthquake record folder
}
# Parameters to update
ParameterInfo = {
    "ParameterName": ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8"],  # stiffness at each floor
    "TrueParameterValues": np.ones((8, 1), ) * 1e9,  # true parameters
    "UpdateParameterIndex": []
}
k0 = 1e9
UpdateParameterName = ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8"]
ParameterInfo["UpdateParameterIndex"] = ismember(ParameterInfo["ParameterName"], UpdateParameterName)
TrueUpdateParameterValues = ParameterInfo["TrueParameterValues"][:, 0]
# compute the true response
measure_vector = np.array([[0, 1, 2, 3, 4, 5, 6, 7]])  # take first floor and top floor acceleration as measurement
TrueResponse = h_measurement_eqn(ParameterInfo["TrueParameterValues"], GMinput, 1, GMinput["totalStep"], measure_vector,
                                 k0)
TrueResponse, max = normalize(TrueResponse)
NoisyTrueResponse = TrueResponse + np.random.randn(TrueResponse.shape[0], TrueResponse.shape[1]) * 0.01

# number of particles (to approximate the posterior)
Np = 250

# prior distribution of parameters
prior_mean = np.array([[1.14, 1.32, 0.35, 0.95, 0.87, 1.235, 0.935, 0.85]])
i = 0
all_pars = [pdfs.TruncatedNormal(mu=prior_mean[0, i] * TrueUpdateParameterValues[i],
                                 sig=0.3 * np.abs(prior_mean[0, i] * TrueUpdateParameterValues[i]), low=1, up=np.Inf)
            for i in range(8)]

ny = 8
RMS_measurementNoise = 1 / 100
R = RMS_measurementNoise ** 2 * np.ones((1 * ny, 1))


def log_likelihood(particle_num, theta):
    """
    Required!
    log-likelihood function which is problem specific
    for the 2DOF example log-likelihood is

    Parameters
    ----------
    particle_num : int
        particle number.
    s : numpy array of size Np (number of parameters in all_pars)
        particle location in Np space

    Returns
    -------
    LL : float
        log-likelihood function value.

    """
    # calculate the mean
    theta.reshape(-1, 1)
    y = h_measurement_eqn(theta, GMinput, 1, GMinput["t otalStep"], measure_vector, k0)
    for i in range(y.shape[1]):
        y[:, i] = y[:, i] / max[i]
    N, Ny = y.shape
    delta = NoisyTrueResponse - y
    par_sigma_normalized = [0.01] * Ny
    if y.shape != NoisyTrueResponse.shape:
        return -np.Inf

    LL = -0.5 * N * Ny * np.log(2 * np.pi) - np.sum(N * np.log(par_sigma_normalized)) - np.sum(
        0.5 * (np.power(par_sigma_normalized, -2)) * np.sum(delta ** 2, axis=0))
    return LL


# run main
if __name__ == '__main__':
    """main part to run tmcmc for the 8DOF example"""

    mytrace, comm = run_tmcmc(Np, all_pars,
                              log_likelihood, parallel_processing,
                              "status_file_8DOF.txt")

    # save results
    with open('mytrace.pickle', 'wb') as handle1:
        pickle.dump(mytrace, handle1, protocol=pickle.HIGHEST_PROTOCOL)

    if parallel_processing == 'mpi':
        comm.Abort(0)
