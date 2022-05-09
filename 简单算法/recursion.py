"""
假设有四种面额的钱币，1 元、2 元、5 元和 10 元，而您一共给我 10 元，那您可以奖赏我 1 张 10 元，
或者 10 张 1 元，或者 5 张 1 元外加 1 张 5 元等等。如果考虑每次奖赏的金额和先后顺序，那么最终一共有多少种不同的奖赏方式呢？”

递归解法：
1、假设 n=k-1 的时候，我们已经知道如何去求所有奖赏的组合。那么只要求解 n=k 的时候，会有哪些金额的选择，以及每种选择后还剩下多少奖金需要支付就可以了。
2、初始状态，就是 n=1 的时候，会有多少种奖赏。
"""
from typing import List


reward = [1, 2, 5, 10]


def ans(total_reward: int, result: List[int]) -> None:

    # 当total_reward为0时，说明满足条件输出解
    if total_reward == 0:
        print(result)

    # 如果小于0，不满足条件，跳过
    elif total_reward < 0:
        pass

    # 其他情况进入递归过程
    else:
        for i in range(len(reward)):
            new_result = result[:]
            new_result.append(reward[i])
            ans(total_reward - reward[i], new_result)


ans(10, [])
