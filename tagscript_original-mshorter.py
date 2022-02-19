#!/usr/bin/python
#http://www.astro.ufl.edu/~warner/prog/python.html  - Python Basics if you want to learn some Pythong
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
fields=10 # number of fields 
documentWidth = rowwidth*fields +50 #maximum width the document should be
documentHeight = 2250 #this is  guess since we need to make the document before we know the file size, doesn't really matter anyway
direction = 'r' #which direction the tag is facing, staring out with labels on the right
offset=0 #this is where we start, for the left we will start on the right side of the page
previoustext = 0 #for text function, defines how much text we have already written so we know where to start
textheight=17 #how much we add each time we add a line of text
textstart=100 #where a block of text will start (y axis), this will be set in the code
myfile="ProMini" #file read in to be parsed
fontsize=12
imagewidth=250
imageheight=250
indent = 1

################################################# FUNCTIONS ###################################################

#Writes plain text from the text section
def writeText(i,value,row):
  
  text = dwg.add(dwg.text(str(value), insert=(0,textstart),font_size=12, font_family='Montserrat', fill='black'))
  #print ("Printing " + str(value) + " at " + str(textstart))
  global previoustext
  previoustext = previoustext + textheight  
  #end writeText

#Creates colored blocks and text for fields
def writeField(type,value,row,spot):
  #print("Type: " + str(type) + "  Value: " + value)
  if (type==0): #Pin name on board
    box0 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='black', opacity=0.3, fill='white'))
    text0 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='black'))
    #print("Box0, in white with " + value + " written in black")
	
  elif(type==1): #Power
    box1 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='red', opacity=0.8, fill='red'))
    text1 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='black'))
    #print("Box1, in red with " + value + " written in black")
	
  elif(type==2): #GND
    box2 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='black', opacity=0.9, fill='black'))
    text2 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='white'))
    #print("Box2, in black with " + value + " written in white")
	
  elif(type==3):#Control
    box3 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='yellow', opacity=0.8, fill='yellow'))
    text3 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize-1, font_family='Montserrat',  fill='black'))
    #print("Box3 in red with " + value + " written in black")
	
  elif(type==4):#Arduino Pin number
    box4 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='green', opacity=0.3, fill='green'))
    text4 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='black'))
    #print("Box4 in green with " + value + " written in black")
	
  elif(type==5):#Port
    box5 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='blue', opacity=0.4, fill='blue'))
    text5 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='black'))
    #print("Box5 in blue with " + value + " written in black")
	
  elif(type==6):#Analog Pin
    box6 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='purple', opacity=0.3, fill='purple'))
    text6 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize-2, font_family='Montserrat',  fill='black'))
    #print("Box6 in purple with " + value + " written in black")
	
  elif(type==7):#PWM
    box7 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='yellow', opacity=0.2, fill='yellow'))
    text7 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize-2, font_family='Montserrat',  fill='black'))
    #print("Box7 in yellow with " + value + " written in black")
	
  elif(type==8):#Serial
    box8 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='grey', opacity=0.3, fill='grey'))
    text8 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='black'))
    #print("Box8 in grey with " + value + " written in black")
	
  elif(type==9):#External Interupt
    box9 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='blue', opacity=0.1, fill='blue'))
    text9 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='black'))
    #print("Box9 in purple with " + value + " written in black")
	
  elif(type==10):#Pin Chg Int
    box10 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='pink', opacity=0.5, fill='pink'))
    text10 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='black'))
    #print("Box10 in orange with " + value + " written in black")
	
  elif(type==11):#Misc
    box11 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='green', opacity=0.1, fill='green'))
    text11 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='black'))
    #print("Box11 in blue with " + value + " written in black")
	
  elif(type==12):#Misc2
    box12 = dwg.add(dwg.rect((rowwidth*spot+offset,row*rowheight), (width,height), 1, 1, stroke='blue', opacity=0.1, fill='blue'))
    text12 = dwg.add(dwg.text(str(value), insert=(spot*rowwidth+offset+indent,row*rowheight+height),font_size=fontsize, font_family='Montserrat',  fill='black'))
    #print("Box12 in blue with " + value + " written in black")
	#to add more, change elif statement, stroke color, fill color, text color, variable names (box and text) and print statement, also change 'fields' global variable
#end writeField


#adds images to end of document, currently not used as pngs don't work as well as I'd like and it is easier to just drag and drop the files I want into the final file.
def writeImages(i,value,row):
  global previoustext
  currentimage = "Images/" + value + ".png"
  if os.access(currentimage, os.R_OK):
    print ("Adding " + currentimage)
    image = dwg.add(dwg.image(href=("../" +  currentimage), insert=(i*imagewidth,textstart)))
  else:
    print ("Could not find " + currentimage)  
#end writeImages




#open file with read access
myfile = input("Enter file name minus .csv extension ()ex. ESP8266/Thing): ")
if os.access(myfile +".csv", os.R_OK):
  file = open(myfile +".csv","r")
  print ("File opened")
else:
  print ("File not found, please try again, there should be a comma deliminated csv file with the data in it.  See script for more details")
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
    print ("Done")
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



