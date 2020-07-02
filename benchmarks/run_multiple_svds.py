import sys
import time

import numpy as np
from joblib import Parallel, delayed


def run_svd(seed, size=2000):
    rs = np.random.RandomState(seed)
    array = rs.randn(size, size)
    U, S, V = np.linalg.svd(array)
    return S[0]


if __name__ == "__main__":
    assert len(sys.argv) == 3

    n_calls, n_jobs = int(sys.argv[1]), int(sys.argv[2])
    assert n_calls > 0
    assert n_jobs > 0

    t0 = time.time()
    res = Parallel(n_jobs=n_jobs)(
        delayed(run_svd)(i, size=2000) for i in range(n_calls)
    )
    print(time.time() - t0)
