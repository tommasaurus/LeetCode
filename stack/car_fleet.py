class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create an array that shows the arrival time of each car according to their position and speed, disregarding the existence of other cars. Then the solution would be that, starting with the closest starting position, we iterate backwards and see if the time is greater or less than the previous. In the case that the time is less than the previous, then a fleet is formed. In the case that the time is greater than the previous, then a new fleet is formed. 
        cars = {}
        for i, each in enumerate(position):
            cars[each] = speed[i]
        
        position = sorted(position)
        time = []

        for each in position:
            time.append((float(target - each)/float(cars[each])))
        
        # time = [(float(target - position[i])/float(speed[i])) for i in range(len(position))]
        fleets = 0
        last_time = -1
        for i, each in enumerate(time[::-1]):
            if each > last_time:
                fleets += 1
                last_time = each

        return fleets