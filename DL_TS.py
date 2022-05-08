# ====================================================================================================
# TS: time series
# ====================================================================================================
# import library

import numpy as np
# ----------------------------------------------------------------------------------------------------
# transition matrix

P = [[0, 0, 1],
     [1/2, 1/2, 0],
     [1/3, 2/3, 0]]

a = np.random.choice(3, 1, p=P[1][:])
# ----------------------------------------------------------------------------------------------------
# sequential processes
# sequence generated by Markov chain
# starting from 0, S1 = 0, S2 = 1, S3 = 2


def sequence(iter):

    x = 0

    S = []
    S.append(x)

    for i in range(iter):

        x = np.random.choice(3, 1, p=P[x][:])[0]

        S.append(x)

    return print(S)
# ====================================================================================================
