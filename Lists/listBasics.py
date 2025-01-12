symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
#           0   1    2    3   4    5    6 - Index
#           1   2    3    4   5    6    7 - Element Numbers
symbols_list = symbols.split(',')
print(symbols)

#Slicing List
first_4 = symbols_list[:4]
print(first_4)
#Slice from 2nd element to 6th element ( 1st index to 5th index)
second_6 = symbols_list[1:6] 
print(second_6)