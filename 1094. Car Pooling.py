class Solution(object):
    def carPooling(self, trips, capacity):

        stops = [0] * 1001  # Since locations range from 0 to 1000

        for num_passengers, start, end in trips:
            stops[start] += num_passengers
            stops[end] -= num_passengers

        current_passengers = 0
        for passengers in stops:
            current_passengers += passengers
            if current_passengers > capacity:
                return False

        return True
