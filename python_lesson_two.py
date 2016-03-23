"""Python Lesson II: Lists

This lesson's based on the Section 2.3 from Composing Programs, which you can
find here: http://composingprograms.com/pages/23-sequences.html

Lists allow us to increase the scope of the data that we can manipulate
"""

def what_are_lists():
	"""We're now using a new data type - lists. Lists are sequences.

	listy_list = [0, 1, 2, 3, 4]
	wordy_list = ["red", "yellow"]
	combined_list = [3.0, "alpha", 9]
	inception_list = [[1, 1, 2], [3, 5, 8], [13, 21, 34], [55, 89, 144]]

	They can contain all sorts of data and can be of any length.

	lists can be added to combine multiple lists

	>>> list1 = [1,2,3,4]
	>>> list2 = [5,6,7,8]
	>>> list1 + list2
	[1, 2, 3, 4, 5, 6, 7, 8]

	lists can also be multplied like repeated adding

	>>> list1 * 2
	[1, 2, 3, 4, 1, 2, 3, 4]

	>>> list2 * 3 == list2 + list2 + list2
	True

	Lists are ordered, so each element has a specific index. In CS, counting
	starts from 0. Thus the first element has index 0, second 1, and so on

			["alpha", "bravo", "charlie", "delta"]
	Index:	 0		  1		   2 	      3

	Define a list below so that the lines following evaulate correctly

	>>> undertale = 
	>>> undertale[0]
	'Sans'
	>>> undertale[2]
	'Flowey'
	>>> undertale[1]
	'Papyrus'
	>>> undertale[5]
	'Asgore'

	Each of these act like variables - you can read them (as shown above)
	but also reassign them and use them in functions

	>>> undertale[0] = "Mettaton"
	>>> print undertale[0]*2
	MettatonMettaton

	What if you had lists in lists so you could list while you list?

	>>> i_heard_you_like_lists = [[1, 2, 3], ["attack", "defend"]]
	>>> i_heard_you_like_lists[0][0]
	1
	>>> i_heard_you_like_lists[0][2]
	3
	>>> i_heard_you_like_lists[1][1]
	'defend'

	Lists also have some useful functions pre-made

	len(list1) will give the length of a list

	>>> example = ['a', 'b', 'c', 'd']
	>>> len(example)
	4

	#Notice that this one evaluates only to 2 - not 5
	#There are only two elements, each list
	#Even though each of those lists have their own lists
	>>> len(i_heard_you_like_lists)
	2

	list1.append(element) will add element to the end of list1
	>>> example.append('e')
	>>> example
	['a', 'b', 'c', 'd', 'e']

	list1.insert(index, element) will add an element at a specific location
	The element following will be scooted over.

	list1.remove(element) will remove the first occurnece of that element

	list1.pop(index) will return the element at the index and remove it from 
	the list. If no index is given, it acts upon the last element
	>>> example.pop(0)
	'a'
	>>> example
	['b', 'c', 'd', 'e']
	>>> example.pop()
	'e'
	>>> example
	['b', 'c', 'd']

	Using the functions above, fix the following statements. You may need
	to add or remove ">>>" 's depending on how you go about it.
	>>> fix = ['d', 'e', 'e', 'e', 'r', 'm', 'x', 'n', 'a', 't', 'i',]
	
	>>>
	>>>
	>>>
	>>>

	>>> fix
	['d', 'e', 't', 'e', 'r', 'm', 'i', 'n', 'a', 't', 'i', 'o', 'n']
	"""
	print "Nice"

def print_list(lst):
	"""Now that you have an undertanding of lists, lets go deeper

	We can use iteration to go through lists similar to lesson 1. The
	following function will print out lists

	>>> example = [0,1,2,3]
	>>> print_list(example)
	0
	1
	2
	3
	"""
	index = 0
	while index < len(lst):
		print lst[index]
		index += 1

def print_list_with_indices(lst):
	"""Now you try. This time though, print the index of the element, then
	the element

	>>> example = ["mario", "luigi", "wario"]
	>>> print_list_with_indices(example)
	0 mario
	1 luigi
	2 wario

	>>> other = [3, 1, 4, 5, 9, 2]
	>>> print_list_with_indices(other)
	0 3
	1 1
	2 4
	3 5
	4 9
	5 2

	If you're having trouble, do what the professionals do:
	Google it. Someone else has to have had the same problem as you and asked
	online about it. Stack Overflow is a great resource. If you spend more
	than 5 - 10 minutes looking for an answer though, you're probably better
	off just asking one of your friends #kik
	"""
	"Write your code here"

#Your turn - 
def index_match(lst):
	"""Returns whether ANY element of a list matches its index

	>>> test1 = [1, 5, 8, 5, 2, 0]
	>>> index_match(test1)
	False


	# Now add in another element 6, which has the corresponding index of 6
	>>> test1.append(6)
	>>> index_match(test1)
	True

	>>> test2 = [1, 5, 8, 5, 2, 0, 6]
	>>> test1 == test2
	True

	# Each of these elements correspond to their index
	>>> test3 = [0, 1, 2, 3]
	>>> index_match(test3)
	True
	"""
	"Write your code here"

def sum_list(lst):
	"""Returns the sum of all elements in a list

	Each element of lst

	>>> bill = [4, 6, 2, 4]
	>>> print sum_list(bill)
	16

	>>> primes = [2, 3, 5, 8]
	>>> sum_list(primes)
	18
	"""
	"Write your code here"

def combine_strings(lst):
	"""Returns a string that combines all strings in lst but adds spaces

	Note that you'll probably need to do something slightly different for
	the last element of the string.

	>>> sentence = ["Are", "you", "feeling", "it", "now", "Mr.", "Krabs"]
	>>> combine_strings(sentence)
	'Are you feeling it now Mr. Krabs'

	>>> quote = ["Luke,", "I", "am", "your", "father"]
	>>> combine_strings(quote)
	'Luke, I am your father'
	"""
	"Write your code here"

def combine_num_or_string(lst):
	"""Combines a list of either strings of numbers

	BONUS: write a function that can combine either a list of numbers
	or a list of strings

	Hint: try playing around with the initial value of your totaling variable

	There's multiple ways to go about this, so play around, but skip ahead if
	you get stuck

	>>> sentence = ["Are", "you", "feeling", "it", "now", "Mr.", "Krabs"]
	>>> combine_num_or_string(sentence)
	'Are you feeling it now Mr. Krabs'

	>>> primes = [2, 3, 5, 8]
	>>> combine_num_or_string(primes)
	18
	"""
	"Write your code here"

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    print "Tested"
	




