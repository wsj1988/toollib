# -*- coding: utf-8 -*-

import time

FORMAT = '%Y-%m-%d %H:%M:%S'


def str_2_ts(str_dt):
    """convert string datetime to timestamp"""
    ts = time.mktime(time.strptime(str_dt, FORMAT))
    return ts


def ts_2_str(ts_dt):
    """convert timestamp to string, notation as `%Y-%m-%d %H:%M:%S`"""
    str_dt = time.strftime(FORMAT, time.localtime(ts_dt))
    return str_dt


if __name__ == '__main__':
    str_dt1 = time.strftime(FORMAT, time.localtime())
    ts1 = str_2_ts(str_dt1)
    print ts1

    ts2 = time.time()
    str_dt2 = ts_2_str(ts2)
    print str_dt2
