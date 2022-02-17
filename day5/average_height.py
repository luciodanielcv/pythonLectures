

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#sum = sum(student_heights)
#average = sum / len(student_heights)

sum = 0
counter = 0
for height in student_heights:
  sum += height
  counter += 1

average = sum / counter
print(f"The average height is: {average}")



