import pandas as pd
import numpy as np

def convert_residuals_to_original(chart_df, predictions, features=["obs", "UCL", "Center", "LCL"]):
    chart_df = chart_df.copy()
    chart_df.loc[:, features] = chart_df.loc[:, features].values + predictions[:, None]
    return chart_df


def gen_rv(dist, args, size, random_state=123):
    rv = dist.rvs(*args, size=size, random_state=random_state)
    return rv


def gen_rv_seq(dist, args_list, size_list, random_state=123):
    
    # Get number of sequences
    n_seq = len(size_list)
    
    # create empty rv
    ret = pd.DataFrame()
    
    for i in range(n_seq):
        rv_temp = gen_rv(dist, args=args_list[i], size=size_list[i], random_state=random_state).tolist()
        rv_df = pd.DataFrame({'seq':i, 'rv':rv_temp})
        ret = ret.append(rv_df)

    ret = ret.reset_index(drop=True)
    
    return ret

if __name__ == "__main__":
    pass
