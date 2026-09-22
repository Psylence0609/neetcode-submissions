class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # keep the interval that ends earliest.
        intervals.sort(key = lambda pair: pair[1])
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]


        return res