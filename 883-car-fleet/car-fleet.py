class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [[position[i], speed] for i, speed in enumerate(speed)]
        fleet.sort(key=lambda x : x[0], reverse=True)
        stack = []
        for car in fleet:
            arrivaltime = (target-car[0]) / car[1]
            stack.append(arrivaltime)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)