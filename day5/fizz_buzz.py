


for n in range(1,101):
  if n % 3 == 0 and n % 5 == 0:
    print(f"{n} - FizzBuzz")
  elif n % 3 == 0:
    print(f"{n} - Fizz")
  elif n % 5 == 0:
    print(f"{n} - Buzz")
  else:
    print(f"{n}")
  
  