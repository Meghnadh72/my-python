""" There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies. """

candies = [2, 3, 5, 1, 3]
extraCandies = 3
from collections import defaultdict

result = []
index_map = defaultdict(list)
for index, candy in enumerate(candies):
    index_map[candy].append(index)
    result.append(False)

candies = sorted(candies)
largest = candies[-1]
for candy in candies:
    if candy + extraCandies >= largest:
        for each_index in index_map[candy]:
            result[each_index] = True
print(result)
