class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        for n in nums:
            mapper[n] = mapper.get(n, 0) + 1
        # nums = sorted(mapper.keys(), key = lambda a: -1 * mapper[a])
        # return nums[:k]

        heap = []
        for num in mapper.keys():
            heapq.heappush(heap, (mapper[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        # print(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res