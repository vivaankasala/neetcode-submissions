class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for number in nums:
            count[number] = count.get(number, 0) + 1

        top_k = sorted(count, key=count.get, reverse=True)[:k]

        return top_k