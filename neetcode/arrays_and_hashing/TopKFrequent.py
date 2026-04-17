import heapq

def topKFrequent(nums, k):
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    
    max_heap = []

    for num in freq:
        heapq.heappush(max_heap, (-freq[num], num))

    res = []

    for i in range(k):
        neg_freq, val = heapq.heappop(max_heap)
        res.append(val)
    
    return res

# Time Complexity: O(nlogn), because of the sortinig manner of the heap
# Space Complexity: O(n), because we are using multiple data structures to store