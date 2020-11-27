# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs(i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].


class Solution(object):
    def numEquivalentDominoes(self, dominoes):
        count = 0
        seen = []

        for domino in dominoes:
            if domino in seen:
                count += 1
                continue

            seen += [domino, list(reversed(domino))]

        return count


print(Solution().numEquivalentDominoes([[1, 2], [2, 1], [3, 4], [5, 6]]))
