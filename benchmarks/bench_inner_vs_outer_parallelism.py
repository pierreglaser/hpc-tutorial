import os
import subprocess
import sys

import pandas as pd


cmd = [sys.executable, "run_multiple_svds.py"]


def set_n_jobs_and_mkl_num_threads(n, parallelism_level):
    assert isinstance(n, int)
    if n == -1:
        n = os.cpu_count()

    if parallelism_level == "inner":
        return n, 1
    if parallelism_level == "outer":
        return 1, n
    elif parallelism_level == "both":
        return n, n
    else:
        raise ValueError


if __name__ == "__main__":
    all_results = []

    for level in ["inner", "outer", "both"]:
        for n_calls in [1, 4, 8, 16, 24, 48]:
            mkl_num_threads, n_jobs = set_n_jobs_and_mkl_num_threads(-1, level)
            p = subprocess.Popen(
                cmd + [str(n_calls)] + [str(n_jobs)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env={"MKL_NUM_THREADS": str(mkl_num_threads)},
            )
            p.wait()
            out, err = p.communicate()
            res = {
                "mkl_num_threads": mkl_num_threads,
                "n_jobs": n_jobs,
                "n_calls": n_calls,
                "time": out.decode().strip(),
            }
            print(res)
            all_results.append(res)

    df = pd.DataFrame(all_results)
    df.to_csv("results.csv")
