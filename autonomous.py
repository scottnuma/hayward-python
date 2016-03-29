"""Functions for controlling the HaywardBot

Without a driving robot currently, testing this code is difficult. However, 
you can still write up code to be then tested later.

The Application Programming Interface (API) documentation will definitely be
very useful here: 

http://pie-api.readthedocs.org/api.html

It'll tell you about all the functions you can use
"""

# You might find these modules useful
from api.Robot import *
import time
import math

# Note that there are two different ways of importing modules
#
# import module_name
# and
# from module_name import thing
#
# When you use the first method, to use that module you must
# include the module's name ( time.sleep(3) or math.pi )
#
# When you use the second method, it's not necessary to include the module's
# name ( get_axis(argument_1, argument_2) )

def move_forward(speed):
	"""Moves the robot forward

	speed: a float ranging from -1 to 1

	move_forward(1) - move forward as fast as possible
	move_forward(-1) - move backward as fast as possible
	move_forward(0) - do not move
	"""

def turn(degree):
	"""Turns the robot

	degree: any real number

	turn(0) - no effect
	turn(360) - the robot spins once completely clockwise
	turn(-360) - the robot spins once completely counter-clockwise
	turn(90) - the robot turns to the left
	turn(-90) - the robot turns to the right
	turn(270) - the robot turns to the right, the long way
	"""

def turn_radians(radians):
	"""Turns the robot

	Using only one line of code, and reusing the turn function create a
	function that takes radians as input

	turn(3.14 / 2) - turns the robot to the left

	Note: you can use mathmematical constants with the math module, giving you
	the math.pi constant. Notice that I've already imported math at the top

	>>> math.cos(math.pi)
	-1.0
	"""

def travel_in_square():
	"""The robot travels in a square with side length of 1 yd

	This is a good example in which Abstraction can play a powerful role.
	You could program using the PIE-given API, but what if our mechanical crew
	decides to change to completely change how the robot moves? Or, what if
	you'd like to reuse this code next year?

	If for some reason, the code needed to move forward changes, using only
	our own defined functions will allow us to easily update the changes all
	in one place. The alternative would be scanning through our entire program 
	for anywhere we move forward, and updating each segment.

	Thus, even if move_forward() and turn() don't work, we can pretend
	that they do work as they're supposed to. That way, when we do have the
	robot and can successfully implement and test the move forward functions,
	updating our entire program is very easy.
	"""

def move_to_chest_from_start_one():
	"""Move the robot from (starting location outside the ball pit nearest the
	entrance to the ramp) to (next to the enemy chest) as according to
	strategy

	Since you don't have a rolling robot or field yet, this will require some
	guessing that will then have to be corrected later. Use your previous 
	functions where you can.
	"""

def move_to_chest_from_start_one():
	"""Move the robot from (starting location outside the ball pit furthest 
	from the entrance to the ramp) to (next to the enemy chest) as according
	to strategy
	"""

def esacpe_ball_pit():
	"""Moves the robot out of the ball pit

	Suppose the robot is pushed into the ball pit. What can you try to get
	out?
	"""