import random

a = random.sample(range(0,201),100)
b = random.sample(range(0,401),200)

print(sorted([num for num in a if num in b]))

