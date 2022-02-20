

def greet():
  print("Hello!")
  print("How've you been?")
  print("Hope well")

def greet_with_name(name):
  print(f"Hello {name}!")
  print(f"How've you been {name}?")
  print("Hope well")



#Functions with more than 1 input
def greet_with_name_and_location(name, location):
  print(f"Hello {name}!")
  print(f"How've you been {name}?")
  print(f"How's {location}?")

greet()
print()
greet_with_name("LDCV")
print()
greet_with_name_and_location("LDCV", "hgo pue")

#Non-positional-argument calls
#Keyword-argunment calls
print()
greet_with_name_and_location(location="The location", name="The name")
greet_with_name_and_location(name="The name", location="The location")


