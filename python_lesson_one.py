"""This is a worksheet I wrote up to help get you comfortable with Python. 
                           ____
  ________________________/ O  \___/
 <_/_\_/_\_/_\_/_\_/_\_/_______/   \ 

If you need help, ask a friend or shoot me an email: scott.numamoto@pioneers.berkeley.edu
Or facebook/text if that's your thing. If this takes more than an hour and you 
can't finish, don't worry about it.

I defined functions below of various names. Each have a "string" immediately
below the "def function_name():" statement. These strings are supposed to show
what Python would print if it ran the commands after the ">>>"

The line immediately following the ">>>" shows the result. Your job will be to
make sure the command (the stuff after >>>) and the result (the next line) is 
accurate.

To check your work run the file (F5) - Don't worry when you get hit with a massive
wall of text. You'll probably see something like this:

				(Move text would be output above the following in IDLE)

				**********************************************************************
which function:	File "python_lesson_one.py", line 72, in __main__.p_type_checker
				Failed example:
which line:		    type(94) ==
				Exception raised:
				    Traceback (most recent call last):
				      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
				        compileflags, 1) in test.globs
				      File "<doctest __main__.p_type_checker[4]>", line 1
				        type(94) ==
				                   ^
Specific error:	    SyntaxError: invalid syntax
				**********************************************************************
				15 items had failures:
Progress on		   3 of   3 in __main__.a_print_if_odd
each of the		   4 of   4 in __main__.b_repeat
functions		   4 of   4 in __main__.c_print_multiples
				   3 of   3 in __main__.d_print_up_to
				   6 of   6 in __main__.e_school
				   3 of   3 in __main__.f_num_sides
				   3 of   3 in __main__.g_worthy_of_the_sword
				   2 of   2 in __main__.h_total_cost_of_lunch
				   3 of   3 in __main__.i_area_of_rectangle
				   3 of   3 in __main__.j_minutes_to_seconds
				   2 of   2 in __main__.k_triangle_length
				   3 of   3 in __main__.l_feet_to_inches
				   6 of   6 in __main__.n_division
				   3 of   7 in __main__.o_evaluating_functions
				   9 of  13 in __main__.p_type_checker
				***Test Failed*** 57 failures.
				all done

This just means you either haven't answered a question yet or answered it
incorrectly. Only the first error will show up per function - if you get stuck
you can always just erase that question or comment it out with # (more on
that at the end)
"""
from operator import add, sub, mul

def p_type_checker():
	"""This sections checks your understanding of data types. We covered three
	types: int (short for integer), float (what I called decimal), and 
	str (short for string). On the following lines fill in what each data 
	type is so the statement evaluates to true. I did the few one for you - 
	remember upper case vs. lower case matters

	If you get stuck, you can always try typing the left side of the equation
	( type(3) ) into an Interactive Python window to give you a hint.

	>>> type(3) == int
	True

	>>> type("What Up") == str
	True

	>>> type("94.7") == str
	True

	>>> type(8.9) == float
	True

	>>> type(94) == 
	True

	>>> type("Hayward") ==
	True

	>>> type(3.14) == 
	True

	>>> type("1") ==
	True

	>>> type("Nine") ==
	True

	>>> type(-23) == 
	True

	>>> type(0) ==
	True

	>>> type("33") ==
	True

	>>> type(6.0) == 
	True
	"""
	print "Nice!"

def o_evaluating_functions():
	"""This is a quick check on evaluating functions. 

	Quick refresher on functions:

	>>> add(3,5) == 8
	True

	add: function name
	3: first argument (like an input)
	5: second argumnt (like another input)
	(): next to a function name, these CALL the function
	==: an operator comparing left and right sides of the equation
	8: the result of the function CALL
	True: me saying that add(3,5) is equal to 8

	Note that the arguments of a function are evaluated before calling the
	function. Thus the following statements are equivalent:

	add(3, mul(4,5))
	add(3, 20)
	23

	I did a few for you. If you try hints, first run this:
	from operator import add, sub, mul

	>>> add(1, 1) == 2
	True

	>>> mul(sub(8,3), 6) == 30
	True

	>>> sub(6, add(3,1)) == 2
	True

	>>> add(3,4) ==
	True

	>>> mul(add(1,1), 8) == 
	True

	>>> sub(add(5, 10), mul(5,1)) ==
	True
	"""
	print "kewl"

def n_division():
	"""So far, we've used addition, subtraction, and multiplication - not 
	division.
	Division gives different results depending on the data types of the 
	numbers. If you divide and either number is a decimal, the answer will be 
	a decimal.

	5.0 / 3 = 1.666		2 / 5.0 = 0.4	12 / 6.0 = 2.0
	5 / 3.0 = 1.666		2.0 / 5 = 0.4	12.0 / 6 = 2.0





	If you divide and both numbers are ints, the answer will also be an int.
	Everything after the decimal point will be truncated or erased.

	5 / 3 = 1			2 / 5 = 0

	Try filling out the following equations:
	If you get stuck, test it out in Interactive Python

	>>> 9.0 / 3 ==
	True
	>>> 9 / 1 ==
	True
	>>> 5 / 2.0 ==
	True
	>>> 4.0 / 8.0 ==
	True
	>>> 8 / 2.0 ==
	True
	>>> 1 / 2 == 
	True
	"""
	print "aight" 


def m_creating_functions():
	"""In this next part you're going to be making your own functions.
	Instead of changing these really long strings, you'll be writing below 
	them. The next couple functions I've completed for you
	"""
	print "Got it"

def l_feet_to_inches(num_feet):
	"""Converts feet in to inches. Notice that we don't always have to name
	our functions f, and their arguments x and y

	>>> feet_to_inches(2)
	24

	>>> feet_to_inches(5)
	60

	>>> feet_to_inches(3)
	36

	-- You would be writing in the following stuff after the quotations --
	"""
	return num_feet * 12

def k_triangle_length(side1, side2):
	"""Calculates the longest side of a right triangle, given the other lengths

	>>> triangle_length(3,4)
	5.0

	>>> triangle_length(6,8)
	10.0
	"""
	return (side1**2 + side2**2)**.5

def j_minutes_to_seconds(num_minutes):
	"""Converts minutes into seconds
	>>> minutes_to_seconds(1)
	60

	>>> minutes_to_seconds(3)
	180

	>>> minutes_to_seconds(5)
	300
	"""
	"ERASE THIS LINE AND REPLACE WITH YOURS"

def i_area_of_rectangle(side1, side2):
	"""Calculates area of a rectangle given side lengths
	>>> area_of_rectangle(3,4)
	12
	>>> area_of_rectangle(5,3)
	15
	>>> area_of_rectangle(100,2)
	200
	"""
	"ERASE THIS LINE AND REPLACE WITH YOURS"

def h_total_cost_of_lunch(num_burgers):
	"""Calculates cost of getting a given amount of burgers
	>>> total_cost_of_lunch(1)
	5
	>>> total_cost_of_lunch(3)
	15
	"""
	burger_cost = 5
	"ERASE THIS LINE AND REPLACE WITH YOURS - make use of burger_cost too!"

# When text follows a #, it is commented. Thus this text has no effect on the 
# program - you could alter it too and nothing would change

# So far everything we've done has followed one single path. What if we don't
# always want to do the same thing? Thus, the if statement - allowing us to
# take different paths based on the information we have

# Take a look at section 1.5.4 of this website: 
# http://composingprograms.com/pages/15-control.html#conditional-statements
# It'll get you up to speed on if statements.

# Composing Programs introduced a new data type: Boolean
# an int could be 1, 2, -5, 10, or any other integer
# a Boolean can only be True or False, but many other expressions evaluate
# to Booleans, as shown on the website.

def g_worthy_of_the_sword(name):
	"""Determines if a person is worthy of the sword
	>>> worthy_of_the_sword("Merlin")
	False
	>>> worthy_of_the_sword("Elvis")
	False
	>>> worthy_of_the_sword("King Arthur")
	True
	"""
	if name == "King Arthur":
		return True
	else:
		return False

def f_num_sides(shape):
	"""Returns the number of sides of given shape
	>>> num_sides("square")
	4
	>>> num_sides("rectangle")
	4
	>>> num_sides("triangle")
	3
	"""
	"REPLACE THIS LINE WITH YOUR CODE"

def e_school(grade):
	"""Returns the current school level as a string
	>>> school(3)
	"elementary"
	>>> school(6)
	"elementary"
	>>> school(7)
	"middle"
	>>> school(8)
	"middle"
	>>> school(9)
	"high"
	>>> school(12)
	"high"
	"""
	"REPLACE THIS LINE WITH YOUR CODE"

# Nice almost to the end - one last topic iteration
# This allows programmers (that's you) to be lazy... err efficient
# Say you want to want to print every number 0 to 10
# You call the print keyword on each int - but that's a lot of typing
# Instead we'll use iteration with the while clause
# Check out section 1.5.6 to to learn how to use while statements
# http://composingprograms.com/pages/15-control.html#conditional-statements

def d_print_up_to(top_num):
	"""Counts up to a given number

	This is an example I wrote for you, marked with my comments
	>>> print_up_to(3)
	0
	1
	2
	3
	>>> print_up_to(1)
	0
	1
	>>> print_up_to(4)
	0
	1
	2
	3
	4
	"""

	# Create a varaible to serve as a counter
	num_to_print = 0

	# Repeat the indented statements as long as the following condition is True
	while num_to_print <= top_num:
		print num_to_print

		# Increase our counter by 1 to come closer to our goal
		num_to_print = num_to_print + 1

		# Note that if we didin't have this, the function would loop back 
		# around forever in what is called infinite recursion
		# Python is smart enough to recognize when this is happening and stop

	# Note that there is no return statement here - all the function does is
	# print numbers to the screen. If you don't include a return statement
	# when python finishes reading your function, it will actually return
	# None, another special Data Type

def c_print_multiples(num, times):
	"""Prints multiples of num a certain number of times
	Another example for you
	>>> print_multiples(4, 3)
	0
	4
	8
	>>> print_multiples(6, 4)
	0
	6
	12
	18
	>>> print_multiples(33, 0)

	>>> print_multiples(8, 1)
	0
	"""
	#Define a counter to count our reptitions
	counter = 0

	# While counter is less than the number of times we should repeat
	while counter < times:
		# Print the multiple of num
		print num * counter

		# Increase our counter to avoid infinite recursion
		counter = counter + 1

def b_repeat(word, num_times):
	"""Prints a string (word) a certain number of times
	>>> repeat("beep", 3)
	beep
	beep
	beep

	>>> repeat("No this is Patrick", 2)
	No this is Patrick
	No this is Patrick

	>>> repeat("umm", 0)

	>>> repeat("fills you with determination", 4)
	fills you with determination
	fills you with determination
	fills you with determination
	fills you with determination
	"""
	"REPLACE WITH YOUR CODE HERE"

def a_print_if_odd(top):
	"""Prints numbers 0 to top inclusive, but only if each number is odd
	You can check if a number is odd with the modulus operator: %
	It returns the remainder from doing division. Thus 
	5 % 3 = 2      (1 * 3) + 2
	4 % 2 = 0      (2 * 2) + 0
	8 % 3 = 2      (3 * 2) + 2
	18 % 5 = 3     (3 * 5) + 3

	You can thus find what the remainder is after dividing by 2 to determine
	even or odd

	Combine what you know about while and if statements!
	Remember while clauses loop everything that's indented one tab's worth right
	The same goes for if  clauses. These can be combined by indenting even more.

	while x > 4:
		stuff				#repeated regardless of if condition
		if x < 9:
			other stuff		#repeated only if condition is true
		more stuff			#repeated regardless of if condition
	still stuff				#not repeated

	>>> print_if_odd(5)
	1
	3
	5
	>>> print_if_odd(1)
	1
	>>> print_if_odd(4)
	1
	3
	"""
	"REPLACE WITH YOUR CODE HERE"

# Nice you finished. Try taking what you learned here and applying it to 
# robotext - perhaps you can create an autopilot mode
# Maybe rearrange all the numbers sequentially? Or shift them all to a certain
# corner? Ask your friends for help!
# This will get you going for the autonomous mode

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    print "all done"