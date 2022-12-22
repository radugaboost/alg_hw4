# Сложность данного алгоритма O(n)
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        a = pairs.pop()[0]
        res = 1
        while pairs:
            c, d = pairs.pop()
            if d < a:
                res += 1
                a = c
        return 