usernum = []
actNum = []
total = 0
import random


def check(x):
	for i in range(4):
		if (actNum[i] == usernum[i]):
			x = x + 1
	if x == 4:
		print("You got them all right! Congrats!")
	else:
		print("You got " + str(x) + " of them right.")
	usernum.clear()


def askuser():
	usernum.append(int(input("What do you think the first number is?:")))
	usernum.append(int(input("What do you think the second number is?:")))
	usernum.append(int(input("What do you think the third number is?:")))
	usernum.append(int(input("What do you think the four number is?:")))


x = 0
for i in range(0, 4):
	actNum.append(random.randint(1, 9))

while x != 4:
	askuser()
	for i in range(4):
		if (actNum[i] == usernum[i]):
			x = x + 1
	if x == 4:
		print("You got them all right! Congrats!")
	else:
		print("You got " + str(x) + " of them right.")
	usernum.clear()
	total = total + 1

if total > 1:
	print("It took you " + str(total) + " tries.")
else:
	print("It took you 1 try.")
