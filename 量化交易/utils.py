import os
from typing import Sequence, Any
import pandas as pd


# 告警函数，传入条件，如果不满足则抛出指定异常
def assert_msg(condition: Any, msg: str) -> None:
    if not condition:
        raise Exception(msg)


def read_file(filename: str) -> pd.DataFrame:
    """
    读入数据，返回dataframe

    :param filename: 数据文件
    :return:         dataframe
    """
    # 获取文件绝对路径
    filepath = os.path.join(os.path.dirname(__file__), filename)

    # 判断文件是否存在
    assert_msg(os.path.exists(filepath), '文件不存在')

    # 读取文件
    return pd.read_csv(
        filepath,
        index_col=0,
        parse_dates=True,
        infer_datetime_format=True
    )


def SMA(values: Sequence[float], n: int) -> pd.Series:
    """
    返回简单滑动平均

    :param values: 序列值
    :param n:      移动平均窗口大小
    :return:       移动平均值
    """
    return pd.Series(values).rolling(n).mean()


def crossover(series1: Sequence[float], series2: Sequence[float]) -> bool:
    """
    检查两个序列是否在结尾交叉

    :param series1:  序列1
    :param series2:  序列2
    :return:         如果交叉返回Ture, 反之False
    """
    return series1[-2] < series2[-2] and series1[-1] > series2[-1]