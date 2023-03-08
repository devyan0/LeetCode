class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = 0
        loop_cnt = 1
        while i < len(target):
            i_prev = i
            for j, c in enumerate(source):
                if c == target[i]:
                    i += 1
                    if i == len(target): return loop_cnt
            if i_prev == i: return -1
            loop_cnt += 1
        
        return loop_cnt