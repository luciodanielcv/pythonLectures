# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


the_highest = 0
counter = 0
for score in student_scores:
  if counter == 0:
    the_highest = score
  elif score > the_highest:
    the_highest = score
  counter += 1

print(f"The highest score is: {the_highest}")
print("The max function evaluates this: " + str(max(student_scores)))
