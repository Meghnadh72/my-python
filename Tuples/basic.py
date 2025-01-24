# A new Tuple - part of sequence
new_tuple = tuple()
new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

print(new_tuple[0])  # Access by index

# Can't modify contents (immutability)
# new_tuple[1] = 4  # Throws an error

other_tuple = (0, 2, 3, [4, 5, 6, "trsfs"])

other_tuple[3][0] = "Meghnadh"  # Can Modify since target element is mutable
print(other_tuple)

other_tuple[3][3][2] = "fgklnfs"  # Can't Modify since target element is immutable

# Same Applies to List or Dictionary Target element has to be mutable to modify
new_list = [(2, 3, 5), 4, 5, 4, 3, 2]
