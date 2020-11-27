# Take an array of any length with numbers or strings etc. and randomize it in O(n) time

# print(Solution.randomize_array([1, 0, 3, 9, 2]))
# >> [3, 1, 9, 0, 2]

import random


class Solution(object):
    def randomize_array(self, array):

        for last_index in range(len(array)-1, 0, -1):
            last_value = array[last_index]

            new_index = random.randint(0, last_index)

            array[last_index] = array[new_index]
            array[new_index] = last_value

        return array

# time O(n), space O(1)


print(Solution().randomize_array([]))
print(Solution().randomize_array(
    [[1, 2], ["gus", "laura"], "lol", {"gus": "laura"}]))
print(Solution().randomize_array(["gus", "laura", "eph", "mike", "samad"]))
