""" input = [[2,3,[4,7],[1,4]]]
rooms = 10
output = 8,9,10 are available so 3 is the output """

input = [[2, 3], [4, 7], [1, 4]]
rooms = 10
natural_num_set = set(range(1, rooms + 1))
for occupy in input:
    temp_tuple = tuple(range(occupy[0], occupy[1] + 1))
    for room in temp_tuple:
        try:
            natural_num_set.remove(room)
        except KeyError:
            pass

print(len(natural_num_set))
