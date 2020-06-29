import time

from joblib import Memory


memory = Memory('/nfs/gatsbystor/pierreg/joblib-cache')


def my_function(i):
    time.sleep(1)
    return i


my_function_cached = memory.cache(my_function)
