import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        heap = []
        heapq.heapify(heap)
        for i in range(rows):
            for j in range(cols):
                heapq.heappush(heap,matrix[i][j])
        while k-1!=0:
            # print(k-1)
            heapq.heappop(heap)
            k = k-1
        return heapq.heappop(heap)