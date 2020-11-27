# Take an array of any length with numbers or strings etc. and randomize it in O(n) time

# print(Solution.randomize_array([1, 0, 3, 9, 2]))
# >> [3, 1, 9, 0, 2]

import random


class Solution(object):

    def randomize_array(self, items):

        for current_spot, current_item in enumerate(items):
            new_spot = random.randint(current_spot, len(items) - 1)
            items[current_spot] = items[new_spot]
            items[new_spot] = current_item

        return items


for i in range(30):
    # print(Solution().randomize_array([9, 4, 8, 3, 7]))
    print(Solution().randomize_array(['Gus', 'Laura', 'Mike', 'Eph']))
