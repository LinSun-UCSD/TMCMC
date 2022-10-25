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
k0 = 1e9
m0 = 625000
# Parameters to update
ParameterInfo = {
    "ParameterName": ["k1", "k2", "k3", "k4","k5", "k6", "k7", "k8"],  # stiffness at each floor

    "TrueParameterValues": np.ones((8, 1), ) * k0,  # true parameters
    "UpdateParameterIndex": []
}

# compute the true response
measure_vector = np.array([[0, 1]])  # take first floor and top floor acceleration as measurement
trueY, maxEig, maxEigVec = h_measurement_eqn(ParameterInfo["TrueParameterValues"], measure_vector, k0, m0)
trueY[0, :] = trueY[0, :] / maxEig
for i in range(trueY.shape[1]):
    trueY[1:trueY.shape[0], i] = trueY[1:trueY.shape[0], i] / maxEigVec[i]
# pollute the y
N = 5  # data sets num
noiseY = np.zeros((trueY.shape[0], trueY.shape[1], N))
# pollute the eigenvalues
for i in range(N):
    for mod in range(noiseY.shape[1]):
        noiseY[0, mod, i] = (np.random.randn(1) * 0.05 * trueY[0, mod] + trueY[0, mod])
    noiseY[1:noiseY.shape[0], :, i] = (np.random.randn(noiseY.shape[0] - 1, noiseY.shape[1]) * 0.05 +
                                       trueY[1:noiseY.shape[0], :])
# noiseY[0] = np.array([[0.3860,0.3922,0.4157,0.3592,0.3615],[2.3614,2.5877,2.7070,2.3875,2.7272]])
sigmaEigenvalues = 0.05 * trueY[0, :]
sigmaEigenvectors = 0.05 * np.ones(trueY.shape[1], )

# pollute the eigenvectors

# number of particles (to approximate the posterior)
Np = 500

# prior distribution of parameters
prior_mean = np.array([[1, 1, 1, 1, 1, 1, 1, 1]])
i = 0
# all_pars = [pdfs.TruncatedNormal(mu=prior_mean[0, i] * k0,
#                                  sig=0.3 * np.abs(prior_mean[0, i] * k0), low=0.00001, up=np.Inf)
#             for i in range(8)]
all_pars = [pdfs.Uniform(lower=0.6 * k0, upper=1.3 * k0)
            for i in range(8)]


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
    y, _, _ = h_measurement_eqn(theta, measure_vector, k0, m0)
    # take only omega
    eigenValues = y[0, :] / maxEig
    eigenVectors = y[1:y.shape[0], :]
    # SIGMA TERM
    sigmaTerm = 1
    for s in sigmaEigenvalues:
        sigmaTerm *= s
    for s in sigmaEigenvectors:
        sigmaTerm *= s

    LL = -N * np.log((2 * np.pi * sigmaTerm))
    # eigen values term
    for mode in range(len(eigenValues)):
        LL += (-0.5 * (sigmaEigenvalues[mode] ** (-2)) * sum((eigenValues[mode] - noiseY[0, mode, :]) ** 2))

    for mode in range(len(eigenValues)):
        predictEigenvector = eigenVectors[:, mode]
        for measure in range(noiseY.shape[2]):
            expEigenvector = noiseY[1:noiseY.shape[0], mode, measure]
            alpha = np.dot(expEigenvector, predictEigenvector) / \
                    (np.linalg.norm(expEigenvector) * np.linalg.norm(predictEigenvector))
            delta = expEigenvector / np.linalg.norm(expEigenvector) \
                    - alpha * predictEigenvector / np.linalg.norm(predictEigenvector)
            LL += (-0.5 * (sigmaEigenvectors[mode] ** (-2)) * np.dot(delta, delta))

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
