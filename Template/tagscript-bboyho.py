#!/usr/bin/python
#http://www.astro.ufl.edu/~warner/prog/python.html  - Python Basics if you want to learn some Python
#https://pypi.python.org/pypi/svgwrite/  - Library this script uses
#install Python27, download svgwrite, from svgwrite folder run "C:\Python27\python setup.py install"

# This script starts by asking for a file, this name is saved as 'myfile'
# Input file is a 'myfile'.csv and is referred to as file
# Be careful what characters you use.  This is a comma deliminated file, so using a comma in your text will cause problems.  
# Also, some applications will change characters to non-standard characters you will get an error (" - " is often to a larger dash that is non standard)
# Output file is a 'myfile'.svg and is defined before the while loop
# The script is setup for 13 fields, to add more change the global fields variable and add another section to the writeField function with the colors you want.
# If the following words are in field 1 of a line it will change the structure of the output blocks to fit that heading "Left, Right, Top, Text, Extras"
# Text will not make a box, but make a new row of text for each field, each line will be a different section of text, this section must be after blocks
# Extras will look for a file in the folder /Images called value.png and add it to the svg, useful for things like ISP headers graphic, etc. (I'm not actually using this)
# File is read until field 1 is "EOF"

import os
import svgwrite
import time

################################################## GLOBAL VARIABLES ########################################



row=0 #row starts at the top
height=12 #height of a box
width=55 #width of a box
rowheight=15 #height of a row (leaving enough space between rows to move)
rowwidth=width+3 #width of a 'spot', basically width plus a few
fields=19 # number of fields 
documentWidth = rowwidth*fields +50 #maximum width the document should be
documentHeight = 2250 #this is a guess since we need to make the document before we know the file size, doesn't really matter anyway
direction = 'r' #which direction the tag is facing, staring out with labels on the right
offset=0 #this is where we start, for the left we will start on the right side of the page
previoustext = 0 #for text function, defines how much text we have already written so we know where to start
textheight=17 #how much we add each time we add a line of text
textstart=100 #where a block of text will start (y axis), this will be set in the code
myfile="template" #file read in to be parsed
fontsize=12
imagewidth=250
imageheight=250
indent = 1

################################################# FUNCTIONS ###################################################

#Writes plain text from the text section
def writeText(i,value,row):
  
  text = dwg.add(dwg.text(str(value), insert=(0,textstart),font_size=12, font_family='Droid Sans', fill='black'))
  #print ("Printing " + str(value) + " at " + str(textstart))
  global previoustext
  previoustext = previoustext + textheight  
  #end writeText

#Creates colored blocks and text for fields
def writeField(type,value,row,spot):
  #print("Type: " + str(type) + "  Value: " + value)
  


  ########## PIN NAME ON BOARD ##########
  if (type==0):
    box0 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#b3b3b3', opacity=1, fill='#ffffff'))
    text0 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box0, in white with " + value + " written in black")
  
  ########## ARDUINO PIN NUMBER ##########
  elif(type==1):
    box1 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#b3d9b2', opacity=1, fill='#b3d9b2'))
    text1 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='ocra',  fill='black'))
    #print("Box1 in light green with " + value + " written in black")
	
  ########## IC Port (e.g. PC, PA, PB, etc.) ##########
  elif(type==2):
    box2 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#b3b3b3', opacity=1, fill='#b3b3b3'))
    text2 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box2 in light green with " + value + " written in black")

  ########## INTERRUPT ##########
  elif(type==3):
    box3 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#34a853', opacity=1, fill='#34a853'))
    text3 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box3 in dark green with " + value + " written in black")

  ########## PULSE WIDTH MODLATION (PWM) ##########
  elif(type==4):
    box4 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#fffeb1', opacity=1, fill='#fffeb1'))
    text4 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box4 in light yellow with " + value + " written in black")

  ########## Analog PIN (ADC) ##########
  elif(type==5):
    box5 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#cb99cc', opacity=1, fill='#cb99cc'))
    text5 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box5 in lavender with " + value + " written in black")

  ########## SERIAL UART ##########
  elif(type==6):
    box6 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#4286f5', opacity=1, fill='#4286f5'))
    text6 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box6 in dark blue with " + value + " written in black")
  
  ########## I2C ##########
  elif(type==7):
    box7 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#ff7007', opacity=1, fill='#ff7007'))
    tex7 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box7 in purple with " + value + " written in black")

  ########## SPI ##########
  elif(type==8):
    box8 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#fabd03', opacity=1, fill='#fabd03'))
    text8 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box8 in orange with " + value + " written in black")
  
  ########## SDIO ##########
  elif(type==9):
    box9 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#34a853', opacity=1, fill='#fabd03'))
    text9 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box9 in orange fill and dark green stroke with " + value + " written in black")

  ########## USB ##########
  elif(type==10):
    box10 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#005544', opacity=1, fill='#005544'))
    text10 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='white'))
    #print("Box10 in hunter green with " + value + " written in black")

  ########## CAN ##########
  elif(type==11):
    box11 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#ffdfe5', opacity=1, fill='#ffdfe5'))
    text11 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box11 in pink with " + value + " written in black")

  ########## CAMERA ##########
  elif(type==12):
    box12 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#76a5af', opacity=1, fill='#ffcc00'))
    text12 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box12 in blue with " + value + " written in black")
  
  ########## AUDIO ##########
  elif(type==13):
    box13 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#46bdc6', opacity=1, fill='#46bdc6'))
    text13 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box13 in blue with " + value + " written in black")

  ########## CONTROL ##########
  elif(type==14):
    box14 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#ffff4d', opacity=1, fill='#ffff4d'))
    text14 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box14 in yellow with " + value + " written in black")
  
  ########## SWD ##########
  elif(type==15):
    box15 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#cfe2f3', opacity=1, fill='#ffff4d'))
    text15 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box15 in yellow with " + value + " written in black")
      
  ########## POWER ##########
  elif(type==16): 
    box16 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#ff4949', opacity=1, fill='#ff4949'))
    text16 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box16, in red with " + value + " written in black")
	
  ########## GND ##########
  elif(type==17): 
    box17 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#000000', opacity=1, fill='#000000'))
    text17 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='white'))
    #print("Box17, in black with " + value + " written in white")
  
  ########## Micellaneous (Misc) ##########
  elif(type==18):
    box18 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='#cdcefe', opacity=1, fill='#cdcefe'))
    text18 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Droid Sans',  fill='black'))
    #print("Box18 in blue with " + value + " written in black")

	#NOTE: To add more, change elif statement, stroke color, fill color, text color, variable names (box and text) and print statement, also change 'fields' global variable

#end writeField




#adds images to end of document, currently not used as pngs don't work as well as I'd like and it is easier to just drag and drop the files I want into the final file.
def writeImages(i,value,row):
  global previoustext
  currentimage = "Images/" + value + ".png"
  if os.access(currentimage, os.R_OK):
    print "Adding " + currentimage
    image = dwg.add(dwg.image(href=("../" +  currentimage), insert=(i*imagewidth,textstart)))
  else:
    print "Could not find " + currentimage  
#end writeImages




#open file with read access
myfile = raw_input("Enter file name minus .csv extension ()ex. ESP8266/Thing): ")
if os.access(myfile +".csv", os.R_OK):
  file = open(myfile +".csv","r")
  print "File opened"
else:
  print "File not found, please try again, there should be a comma deliminated csv file with the data in it.  See script for more details"
  time.sleep(10)
  os._exit(0)





#read in each line parse, and send each field to writeField  
rawline="not empty"
dwg = svgwrite.Drawing(filename=str(myfile+".svg"), profile='tiny', size=(documentWidth,documentHeight))
while (rawline!=""):
  rawline  = file.readline()
  line = rawline.split(",") #Split into fields separated by ","
  row=row+1
  spot=0
  if (line[0] == "Left"):
    direction = "l"
    offset = documentWidth - rowwidth
    line[0] = ""
  if (line[0] == "Right"):
    direction = "r"
    offset = 0
    line[0] = ""
  if (line[0] == "Top"):
    direction = "r"
    offset = 0
    line[0] = ""
  if (line[0] == "Text"):
    offset = 0
    line[0] = ""
    direction = "text"
  if(line[0] == "Extras"):
    offset=0
    line[0]=""
    direction = "extras"
  if (line[0] == "EOF"): #if we are done
    print "Done"
    dwg.save()
    break
  for i in range(0,fields): #go through total number of fields

      if(line[i]!="" and direction=='r'):
        writeField(i,line[i],row, spot)#call function to add that field to the svg file
        spot=spot+1 #move 'cursor' one spot to the right
		
      if(line[i]!="" and direction=='l'):
        writeField(i,line[i],row, spot)#call function to add that field to the svg file
        spot=spot-1 #move 'cursor' one spot to the left
		
      if (line[i]!="" and direction == "text"):
         textstart = row*rowheight+previoustext
         writeText(i,line[i],row)
		      
      if (line[i]!="" and direction == "extras"):
        writeImages(i,line[i],row)
#end of while


print ("End of File, the output is located at " + myfile + ".svg")
file.close()



