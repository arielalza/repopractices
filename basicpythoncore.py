###Personal note reminder: The double "##" means that part works

#Firts steps on python

##print( 7%(5//2) )
##print( (3**2)//2 )
 

#Part 1: Core python, basic concepts, strings & variables, functions & modules
#regular expressions, control structures, and more.

#Choice $1.000.000 or 0.01 doubled every day for 30 days.
#Task: Write a program to calculate the result amount from the doubling penny.
##print(0.01*(2**30))
#Thats result in 10737418.24 (first attemp and correct)

#For some text we need use the backslash \ (AltGr + ? in spanish layout)
#For example to use single quote
#in texts. 
#This doesn't works. The output results in syntax error because we don't use \
#print('Hi I'm Ariel')
#This print works, the output is 'Hi I'm Ariel'
##print('Hi I\'m Ariel')

#We can use the \ for other things (like in bash) for new tabs = \t 
#for new lines =  \n 
#and other uses.And we can use triple quote that automatically add new
#lines for strings example:
##print("""there are 
#multiple
#lines""")

#Strings operations
##print("Spam" * 3)
##print(4 * '2')
##print('¡' + "pao" * 6 + '!')
#Output result = ¡paopaopaopaopaopao!

#Variables, basic concepts
##user = G4k
##user_name = G4K
#Restrictions for variables: They can use letters, numbers and underscores
#but they can't start with a number, example bellow
#1user_score = 127
#Invalid for the " 1 " in the star, the correct is without the one.
##user_score = 127

#python " input " function
#when the input function is invoke, the programs flow in stopped until the
#user enter some value
#Remember, the input function, returns all input how an string. So, in
#many cases, we need to convert the result of the input, in the correct
#type to use them.
##x = input()
##print(x)
#The input statement need every time parentheses, and we can provide a
#string into the input statement to produce a promp messaage, for example
##name = input("Enter your user name: ")
##print("Hi, " + name)

#Importante things working with multiple variables.
#Task: write two inputs, one number and one word, and multiplicate them.
#If we do this:
#number = input()
#word = input()
#print(word * number)
#WE GET an error message.

#THe correct option, is convert the result of the variable into the 
#corresponding type, in this case, to use it as a number.
#number, 4. word, python
#number = int(input())
#word = input()
##print(word * number)
#result: pythonpythonpythonpython

#in the case we need to convert a number to string, we can use str
##age = 19
##print("When he wins the final champion, his was " + str(age) + " years old")

##x = 5
##y = x + 3
##y = int(str(y) + "2")
##print(y)

##x = 3
##num = 17
##print(num % x)

###############################################################################
###############################################################################


#We start the journal of loops and statements (if, for, while, break,etc)
#if with else 

##number = int(input("Enter a number: "))

##if number < 10:
	##print("Bad choice boy, ending program")
##else:
	##print("Good choice boy, continue the journal")

#note: the if statement can be nest, one inside other
#and "Indetation" is the white line or space in the code like
#if expression < example
###print()

#simple club problem, only people who are 18 or older are allowed
##age = int(input("Enter your age: "))
##name = input("Write your name: ")
##if age >= 18:
	##print("Welcome " + name)
##else:
	##print("Sorry, you're not 18 years old")
#note: every if condition block only can handle one else statement. We can
#chain more if to complete, but we have the option " elif " (stand for if else)

#example chain
##if X = 1:
#	print()
#else:
##	if X = 2
#else: 
	#if

#with elif
#if X = 1:
#print()
#elif X = 2
#print()
#elif X = 3
#print()
#else:
#print("error")


#27/09/2022

#Booleans operators and other things
#Operators: and, or, not

#basic examples

#weight_kg = int(intput())

#if weight_kg >= 50 and weight_kg <= 100:
	#print("You're healthy") 

#type = input()
#if type == "Debit" or type == "Credit":
#	print("accepted")

#The list in python works similar to bash. So we skip writting that.