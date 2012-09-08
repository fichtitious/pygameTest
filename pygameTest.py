#! /usr/bin/python

#Use this area for testing small pieces of code
#raw_input ('Press Enter key to exit.')
#exit ()

import sys, pygame #Remember: sudo apt-get install python-pygame
pygame.init()

#Create a window.
size = width, height = 600, 400
manWidth  = 95
manHeight = 161
screen = pygame.display.set_mode(size)

class Dimension(object):
	'''A class that models the vertical and horizontal dimensions,
	keeping track of which way we're going and allowing us to flip.'''
	def __init__(self):
		self.unit = 1
	def flip(self):
		self.unit *= -1

vertical, horizontal = Dimension(), Dimension()

print '''
Welcome to my game. 
To exit, please close the window
in which the animation appears.

'''

#Load an image file.
walkingMan1 = pygame.image.load('scratchManWalking1.png') #I tried opening this file when it was located in another directory, but I had a hard time with this.


x = 0 #horizontal coordinate for where top left of image will apppear
y = 0 #vertical coordinate for where top left of image will apppear

black = 0 , 0 , 0 #a color we'll use when we black out the screen below


pygame.display.flip() #Redraws the screen.
while 1: #Forever loop.

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit() # Closing the window ends the script.


	screen.fill(black) #blacks out the screen using the color we specified above
	

	#Make the image appear on the screen.
	screen.blit(walkingMan1, (x, y)) #Parameters indicate coordinates of top left corner of the image.

	pygame.display.flip() #Redraws the screen.
	
	#Change horizontal and vertical coordinates so that the image moves.
	for position, screenBound, manSize, dimension in (
		(x, width,  manWidth,  horizontal),
		(y, height, manHeight, vertical)):
		# in each dimension, change direction if the man
		# is about to leave the screen
		if position + manSize >= screenBound or \
			 position < 0:
			dimension.flip()

	x += horizontal.unit
	y += vertical.unit

#backup plan for exiting
raw_input ('Press Enter key to exit.')
