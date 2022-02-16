

import random

options=["heads", "tails"]
print(f"List is this: {options}")

tossString = random.choice(options)

print(f"Choice is: {tossString}")


options.remove(tossString)
tossString = random.choice(options)

print(f"Second choice is: {tossString}")

print(f"List is this: {options}")


#append to add an item to the list
#expand to add multiple items to the list


