

#Prime number checker

#Write your code below this line 👇

def prime_checker(number):
  is_prime = True
  for i in range(2,number):
    if number % i == 0:
      print("It is NOT a prime number!")
      print(f"It is divisible by {i}")
      is_prime = False
      break
  
  if is_prime:
    print("It is a prime number!")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

