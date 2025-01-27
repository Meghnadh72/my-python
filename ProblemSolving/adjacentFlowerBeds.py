class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        len_of_list = len(flowerbed)
        import math

        max_possible = (
            len_of_list // 2 if len_of_list % 2 == 0 else math.ceil(len_of_list / 2)
        )
        if n > max_possible:
            return False
        flower_bed_occupied = False
        for index, flower in enumerate(flowerbed):
            if flower:
                flower_bed_occupied = True
            else:
                if not flower_bed_occupied:
                    if index == len_of_list - 1:
                        n -= 1
                        return n <= 0
                    if not flowerbed[index + 1]:
                        n -= 1
                        flowerbed[index] = 1
                        flower_bed_occupied = True
                else:
                    flower_bed_occupied = False
        return n <= 0
