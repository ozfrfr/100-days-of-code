'''
program which would mark a spot with X
using two digits, reading from row to column
'''

row1 = [ "⬜️", "⬜️", "⬜️"]
row2 = [ "⬜️", "⬜", "⬜️"]
row3 = [ "⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3 ]

print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put the treasure? ")

# this is for the positions of the first and second entry.
horizontal = int(position[0])
vertical = int(position[1])

# reading from row to column
# this block captures the first number's index row on the map list of lists 
# then uses the second position number to get the position for X inside the first number index position's list 
selected_row = map[horizontal - 1]
selected_row[vertical -1] = "X"

print(f"{row1}\n{row2}\n{row3}")


