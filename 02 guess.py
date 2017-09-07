#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import random
assert sys.version_info >= (3,4), "This script requires at least Python 3.4"


while True:

	number = random.randint(1,20)

	print("Hello, and welcome to the game! You need to guess a number between 1 and 20 to win! But be careful, you only get 5 tries! Good luck!")

	try_num = 5

	while try_num > 0:
		guess = input()
		try_num += -1


		try:
			#convert the guess to an integer
			guess = int(guess)


			#check if the guess is less than the random number
			if guess < number:
				print('Too low! You have ' +str(try_num) + ' guesses left!')
			if guess > number:
				print('Too high! You have ' +str(try_num) +' guesses left!')
			if guess ==number:
				print('Congratulations! You guessed right!')
				break


		except ValueError:
			print('Please enter a whole number.')
			
	print("Would you like to try again? Please type 'yes' or 'no'.")
	answer = input()
	if answer == ("yes"):
		continue
	elif answer ==("no"):
		break
	else:
		print("Since you put neither 'yes' or 'no', you get to play again!")

