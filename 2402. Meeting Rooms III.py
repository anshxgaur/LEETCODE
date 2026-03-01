import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        busy_rooms = []
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                end_time, room = heapq.heappop(busy_rooms)
                new_end = end_time + duration
                heapq.heappush(busy_rooms, (new_end, room))
            
            count[room] += 1
        
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
