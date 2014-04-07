import pygame
import math
import random

pygame.init()
width, height = 50,50
screen = pygame.display.set_mode((width,height))
dot = pygame.image.load("dot.png");

class Lifecell:
	x=0
	y=0
	alive = 0
	def __init__(self,x,y,alive):
		self.x = x
		self.y = y
		self.alive = alive

def checkCellsAround(cells):
	count = L.index(cells)
	sum = 0
	if((cells.x ==1) and (cells.y==1)):#---------top left corner
		
		if(L[count+height].alive ==1):
			sum = sum + 1
		if(L[count+1].alive ==1):
			sum = sum + 1
		if(L[count+height+1].alive ==1):
			sum = sum+1
		return sum
	elif((cells.x==width) and (cells.y==height)):#-----bottom right corner
		if(L[count-1].alive == 1):
			sum = sum + 1
		if(L[count-height].alive == 1):
			sum = sum + 1
		if(L[count-height-1].alive==1):
			sum = sum + 1
		return sum
	elif((cells.x==1) and (cells.y==height)):#---------top right corner
		if(L[count-1].alive==1):
			sum = sum+1
		if(L[count+height].alive==1):
			sum = sum+1
		if(L[count+height-1].alive==1):
			sum = sum+1
		return sum
	elif((cells.x==width) and (cells.y==1)):#-------bottom left corner
		if(L[count+1].alive==1):
			sum = sum+1
		if(L[count-height].alive==1):
			sum = sum + 1
		if(L[count-height+1].alive==1):
			sum = sum + 1
		return sum
	elif((cells.x==1) and (cells.y<height)):#------------------------top
		if(L[count+1].alive==1):
			sum = sum+1
		if(L[count+height].alive==1):
			sum = sum + 1
		if(L[count+height+1].alive==1):
			sum = sum + 1
		if(L[count+height-1].alive==1):
			sum = sum + 1
		if(L[count-1].alive==1):
			sum = sum + 1
		return sum
	elif((cells.x==width) and (cells.y<height)):#----------------------bottom
		if(L[count+1].alive==1):
			sum = sum+1
		if(L[count-height].alive==1):
			sum = sum + 1
		if(L[count-height+1].alive==1):
			sum = sum + 1
		if(L[count-height-1].alive==1):
			sum = sum + 1
		if(L[count-1].alive==1):
			sum = sum + 1
		return sum
	elif((cells.x <width) and (cells.y==1)):#--------------------left side
		if(L[count+height].alive==1):
			sum = sum + 1
		if(L[count-height].alive ==1):
			sum = sum+1
		if(L[count+1].alive ==1):
			sum = sum + 1
		if(L[count-height+1].alive==1):
			sum = sum + 1
		if(L[count+height+1].alive==1):
			sum = sum + 1
		return sum
	elif((cells.x<width) and (cells.y==height)):#-----------------right side
		if(L[count-1].alive==1):
			sum = sum +1
		if(L[count-height].alive ==1):
			sum = sum + 1
		if(L[count+height].alive ==1):
			sum = sum + 1
		if(L[count+height-1].alive==1):
			sum = sum+1
		if(L[count-height-1].alive==1):
			sum = sum + 1
		return sum
	else:
		if(L[count+1].alive==1):#right cell
			sum = sum + 1
		if(L[count-1].alive==1):#left cell
			sum = sum +1
		if(L[count-height].alive ==1):#top cell
			sum = sum + 1
		if(L[count+height].alive ==1):#bottom cell
			sum = sum + 1
		if(L[count+height-1].alive==1):#bottom left cell
			sum = sum+1
		if(L[count-height-1].alive==1):#top left cell
			sum = sum + 1
		if(L[count-height+1].alive==1):#top right cell
			sum = sum + 1
		if(L[count+height+1].alive==1):#bottom right cell
			sum = sum + 1
		return sum
	return sum

def gameLogic():

	for i in L:
		if((i.alive==1) and (checkCellsAround(i) is not (2 or 3))):#rule 1,2,3
			i.alive = 0
		if((i.alive==0) and (checkCellsAround(i) == 3)):#rule 4
			i.alive = 1
			
def dotFunction():#try not to generate with 50% of cells being alive with randin(0,1)
	if(random.randint(1,100)>60):
		return 1
	else: return 0
	
L = [Lifecell(xcoor,ycoor,dotFunction()) for xcoor in range(1,width+1) for ycoor in range(1,height+1)]


while 1:
	screen.fill(0)
	
	for eachDot in L:
		if(eachDot.alive==1):
			screen.blit(dot,(eachDot.x,eachDot.y));
	pygame.display.flip();
	gameLogic()
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)		