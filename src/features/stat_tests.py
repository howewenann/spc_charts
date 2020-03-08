from pathlib import Path

# hypothesis testing libraries
from scipy.stats import shapiro
from statsmodels.stats.stattools import jarque_bera
from statsmodels.stats.diagnostic import acorr_ljungbox

# Functions for stat tests
def shapiro_wilks_(data, alpha=0.05):

    # normality test
    stat, p = shapiro(data)
    print("Statistics=%.3f, p=%.3f" % (stat, p))

    # interpret
    if p > alpha:
        print("Sample looks Gaussian (fail to reject H0)")
    else:
        print("Sample does not look Gaussian (reject H0)")

    return None


def jarque_bera_(data, alpha=0.05):

    # normality test
    stat, p, skew, kurt = jarque_bera(data)
    print("Statistics=%.3f, p=%.3f, skew=%.3f, kurt=%.3f" % (stat, p, skew, kurt))

    # interpret
    if p > alpha:
        print("Sample looks Gaussian (fail to reject H0)")
    else:
        print("Sample does not look Gaussian (reject H0)")

    return None


def ljungbox_(data, lags=10, alpha=0.05, print_extra=False):

    # Test for auto correlations H0: rho(k) = 0 for k = 1, 2, ..., h
    stat, p = acorr_ljungbox(data, lags=lags)
    print("Statistics=%.3f, p=%.3f" % (stat[lags-1], p[lags-1]))

    # interpret
    if p[lags-1] > alpha:
        print("No auto correlation up to lag %d (fail to reject H0)" % (lags))
    else:
        print("There is correlation up to lag %d (reject H0)" % (lags))

    if print_extra:
        print("\n")
        print(stat)
        print(p)

    return None


if __name__ == "__main__":

    import numpy as np
    from scipy.stats import t
    from scipy.stats import norm
    from statsmodels.tsa.arima_process import arma_generate_sample

    seed = 123
    sample_size = 100

    # Simulate t-distribution
    df = 2
    t_rv = t.rvs(df, size=sample_size)

    # Run normality tests
    print(
        "Normality test for t-distribution with df = %d, sample size = %d"
        % (df, sample_size)
    )
    print("\n")
    print("Shapiro-wilks test")
    shapiro_wilks_(t_rv)
    print("\n")
    print("Jarque-Bera test")
    jarque_bera_(t_rv)
    print("\n")

    # Simulate normal distribution
    mu = 4
    sigma = 2
    norm_rv = norm.rvs(mu, sigma, size=sample_size, random_state=seed)

    # Run normality tests
    print(
        "Normality test for normal distribution with mu = %d, sigma = %d, sample size = %d"
        % (mu, sigma, sample_size)
    )
    print("\n")
    print("Shapiro-wilks test")
    shapiro_wilks_(norm_rv)
    print("\n")
    print("Jarque-Bera test")
    jarque_bera_(norm_rv)
    print("\n")

    # Simulate AR1 model
    ar = np.array([0.9])
    ma = np.array([0])
    ar1 = arma_generate_sample(
        ar=np.r_[1, -ar], 
        ma=np.r_[1, ma], 
        nsample=sample_size, 
        scale=1
    )
    
    # Test for auto-correlation
    print(
        "Autocorrelation test for AR1 process with ar = %.2f, sample size = %d"
        % (ar[0], sample_size)
    )
    print("\n")
    print("ljungbox test")
    ljungbox_(ar1, lags = 5, alpha=0.05, print_extra=True)
    print("\n")

    # Test for auto-correlation
    print(
        "Normality test for independent normal distribution with mu = %d, sigma = %d, sample size = %d"
        % (mu, sigma, sample_size)
    )
    print("\n")
    print("ljungbox test")
    ljungbox_(norm_rv, lags = 5, alpha=0.05, print_extra=True)
