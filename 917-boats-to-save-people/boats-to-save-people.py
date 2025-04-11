class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        boats = 0

        while l <= r:
            # If heaviest + lightest fit
            if people[l] + people[r] <= limit:
                # Add the lightest
                l += 1
            # Add the heaviest
            r -= 1
            boats += 1

        return boats