from random import randrange
n = randrange(1000)
while True:
    v = int(input())
    if n == v:
        print("You win!")
        break
    print("smaller" if n<v else "bigger")
