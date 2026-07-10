import random
n = random.randint(1,100)
a = -1
gusses = 0
while(a != n):
    gusses += 1
    a = int(input("Guess the Number:"))
    if(a > n):
        print("Lower number please")
    else:
        print("Higher number please")

print(f"You have guessed the number {n} correctly in {gusses} attempts")