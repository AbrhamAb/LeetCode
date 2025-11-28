class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.next_num = 1
        self.in_heap = set()
    
    def popSmallest(self):
        if self.heap:
            num = heapq.heappop(self.heap)
            self.in_heap.remove(num)
            return num
        result = self.next_num
        self.next_num += 1
        return result
    
    def addBack(self, num):
        if num < self.next_num and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)