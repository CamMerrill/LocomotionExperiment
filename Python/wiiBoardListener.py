import wiiboard
import pygame
import time
import csv

def main():
        fileName = input("Enter file name: ")

	board = wiiboard.Wiiboard()

	pygame.init()
	
	address = board.discover()
	board.connect(address) #The wii board must be in sync mode at this time

	board.setLight(True)
	done = False
        #Wait here for unity signal

        prevTime = time.time()
        initialTime = time.time()
	fileName = "Logs/" + fileName
        with open(fileName, 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    	    while (not done):
                #.0125 80 hz
                # .025 40 hz
    	        #time.sleep(0.025)
	        for event in pygame.event.get():
                    #timeVar = time.time()
		    if event.type == wiiboard.WIIBOARD_MASS:
                        if (event.mass.totalWeight > 10):   #10KG. otherwise you would get alot of useless small events!
                            TR = event.mass.topRight
                            TL = event.mass.topLeft
                            BL = event.mass.bottomLeft
                            BR = event.mass.bottomRight
                            timeVar = event.mass.timeVar
                            ''' 
	    	            print "Total weight: " + `event.mass.totalWeight` 
                            print "Top left: " + str(TL)
                            print "Top right: " + str(TR)
                            print "Bottom left: " + str(BL)
                            print "Bottom right: " + str(BR)
                            '''

                            #Calculate center of pressure
                            boardLength = 433 #mm
                            boardWidth = 228 #mm
                            copX = (boardLength/2)*((TR+BR)-(TL+BL))
                            copX = copX / (TR+BR+TL+BL)
                            copY = (boardWidth/2)*((TR+TL)-(BR+BL))
                            copY = copY / (TR+BR+TL+BL)
                           # '''
                            if timeVar-prevTime >= .0125:
                                writer.writerow([copX, copY,timeVar])
                                prevTime = timeVar
                           # '''
                           # writer.writerow([copX, copY, timeVar])


                            if time.time()-initialTime >= 40:
                                print("Time out")
                                done = True


				
		    elif event.type == wiiboard.WIIBOARD_BUTTON_PRESS:
			    print "Button pressed!"

        	    elif event.type == wiiboard.WIIBOARD_BUTTON_RELEASE:
	        	    print "Button released"
		            done = True
			

            board.disconnect()
            pygame.quit()

#Run the script if executed
if __name__ == "__main__":
	main()
