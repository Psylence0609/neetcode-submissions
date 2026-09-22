class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: (x[1], x[0]), reverse = True)
        result = []

        for interval in intervals:
            if not result:
                result.append(interval)
                continue
            prev = result[-1]
            if prev[0] <= interval[1]:
                result[-1] = [min(interval[0], prev[0]), prev[1]]
            else:
                result.append(interval)
        return result