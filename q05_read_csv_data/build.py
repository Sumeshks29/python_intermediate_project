# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = './data/ipl_matches_small.csv'
# Enter code here
def read_ipl_data_csv(path,dtype):
    return np.genfromtxt(path, delimiter=',',skip_header=1,dtype=dtype)



