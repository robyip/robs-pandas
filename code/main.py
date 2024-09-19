import random 

celebrities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(f"Original Celebrities : {celebrities}")

celebrities_rand = random.sample(celebrities, len(celebrities))

print(f"Ramdom Celebrities : {celebrities_rand}")

sweepstakers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(f"Original Sweepstaker list : {sweepstakers}")

sweepstakers_rand = random.sample(sweepstakers, len(sweepstakers))

print(f"Random Sweepstaker list : {sweepstakers_rand}")

