# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure (x,y)? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

position.replace(" ", "")
coords = position.split(",")
x = int(coords[0]) - 1
y = int(coords[1]) - 1

map[x][y] = "X"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")