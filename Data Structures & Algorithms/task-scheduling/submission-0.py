class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # AAABB
        # first count frequencies
        # greedy strategy
        # use a max_heap
        # a queue to hold (remaining count, cooldown_time)
        # in each CPU cycle:
        #   pop most frequent from heap, decrement, and if remains, push (count, time+n) to queue
        #   if task at queue is ready, pop and push its count back to heap
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    queue.append((cnt, time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time
