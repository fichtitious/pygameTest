#! /usr/bin/python

#Use this area for testing small pieces of code
#raw_input ('Press Enter key to exit.')
#exit ()

import sys, pygame #Remember: sudo apt-get install python-pygame
pygame.init()


#Create a window.
size = width, height = 600, 400
screen = pygame.display.set_mode(size)


#Load an image file.
walkingMan1 = pygame.image.load('scratchManWalking1.png') #I tried opening this file when it was located in another directory, but I had a hard time with this.


#Make the image appear on the screen.
screen.blit(walkingMan1, (200, 200)) #Parameters indicate coordinates of top left corner of the image.


pygame.display.flip() #Redraws the screen.
while 1: #Forever loop.

	
	pygame.display.flip() #Redraws the screen.

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit() # Closing the window ends the script.



#backup plan for exiting
raw_input ('Press Enter key to exit.')
