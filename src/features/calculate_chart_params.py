import pandas as pd
import numpy as np

# Helper functions
def calculate_MR(x):
    MR = x.rolling(window=2).apply(lambda x: x.max() - x.min(), raw=True)
    return MR


def estimate_sigma_from_MR(MR):
    sigma = MR.mean() / 1.128
    return sigma


def calculate_ewma(x, alpha=0.1, center=None):

    x_bar = x.mean()

    if center is None:
        center = x_bar

    x_temp = x.copy().tolist()
    x_temp.insert(0, center)

    # Convert list to series
    x_series = pd.Series(x_temp)

    # calculate offset to omit first observation (center)
    offset = len(x_series) - len(x)

    # Return ewma
    ret = x_series.ewm(alpha=alpha, adjust=False).mean()[offset:]

    return ret


# Parameter calculations
def MR_params(MR, center=None):

    MR_bar = MR.mean()

    if center is None:
        center = MR_bar

    # params
    UCL = 3.267 * MR_bar
    center = center
    LCL = 0

    ret = pd.DataFrame({"obs": MR.tolist(), "UCL": UCL, "Center": center, "LCL": LCL})

    return ret


def x_ind_params(x, sigma, center=None, L=3):

    x_bar = x.mean()

    if center is None:
        center = x_bar

    # params
    UCL = center + L * sigma
    center = center
    LCL = center - L * sigma

    ret = pd.DataFrame({"obs": x.tolist(), "UCL": UCL, "Center": center, "LCL": LCL})

    return ret


def c_chart_params(x, center=None, L=3):

    x_bar = x.mean()

    if center is None:
        center = x_bar

    UCL = center + L * np.sqrt(center)
    center = center
    LCL = center - L * np.sqrt(center)

    # Counts cannot be negative
    if LCL < 0:
        LCL = 0

    ret_df = pd.DataFrame({"obs": x.tolist(), "UCL": UCL, "Center": center, "LCL": LCL})

    return ret_df


def ewma_params(x, sigma, alpha=0.1, center=None, L=3):

    x_bar = x.mean()

    if center is None:
        center = x_bar

    # Calculate ewma from x
    ewma = calculate_ewma(x, alpha=alpha, center=center)

    # Get length of x to generate index
    length = len(x)

    # Set up the index
    i = pd.Series(list(range(1, length + 1)))

    # params
    UCL = center + L * sigma * np.sqrt(
        (alpha / (2 - alpha)) * (1 - (1 - alpha) ** (2 * i))
    )
    center = center
    LCL = center - L * sigma * np.sqrt(
        (alpha / (2 - alpha)) * (1 - (1 - alpha) ** (2 * i))
    )

    ret = pd.DataFrame({"obs": ewma.tolist(), "UCL": UCL, "Center": center, "LCL": LCL})

    return ret


if __name__ == "__main__":
    pass
