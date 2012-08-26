#! /usr/bin/python

#Use this area for testing small pieces of code
#raw_input ('Press Enter key to exit.')
#exit ()

import sys, pygame #Remember: sudo apt-get install python-pygame
pygame.init()


#Create a window.
size = width, height = 600, 400
screen = pygame.display.set_mode(size)


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
	x += 1
	y += 1
	
	


#backup plan for exiting
raw_input ('Press Enter key to exit.')
