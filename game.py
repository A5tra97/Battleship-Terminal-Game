from random import randint

#Game Map. A List to represent the rows on the playing field with each row index representing one column accross rows. So index [1[1]] would be column 1 row 1
#An index of [4[3]] will be row four column 3. These indexes are used to find a value in list 4 index 3.
map = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

for list in map:
    print(list)