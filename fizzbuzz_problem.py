#Fizz Buzz problem practice. (Solved 20/10/22)

#Description
#Fizzbuzz is a well known programming assignment, asked during interviews.
#It take an input n and outputs the numbers from 1 to n.
#For each multiple of 3, print "Fizz" instead of the number.
#Same for each multiple of 5, but print "Buzz" instead.
#For numbers which are multiples of both, output "FizzBuzz"

#In this case, we need write the code to skip the even numbers, so
#that the logic only applies to odd numbers, if you want, try
#the other side, skip odd numbers instead of even.
##Note: You can change the words for whatever you want.

n = int(input("Enter a number: "))
for x in range (1,n):
	if x % 3 == 0 and x % 5 == 0:
		print("FizzBuzz")
	elif x % 2 == 0:
		continue
	elif x % 3 == 0:
		print("Fizz")
	elif x % 5 == 0:
		print("Buzz")
	else:
		print("Odd number in the sight", x)