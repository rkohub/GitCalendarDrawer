from datetime import datetime
import os

now = datetime.now()

#links to letters
#https://cdn.shopify.com/s/files/1/0822/1983/articles/pixel-alphabet-pixel-art-letters-alphabet-english.png?v=1474044463
#https://opengameart.org/sites/default/files/boxy_bold_font_5.png

#MAKING THIs
#https://www.piskelapp.com/p/agxzfnBpc2tlbC1hcHByEwsSBlBpc2tlbBiAgKC9w8SDCww/edit
startDay = 82
topVal = 5 #This is the date mod 7 that is at the top of the github calendar
#print(startDay%7) # = topVa

week1  = [1,1,1,1,1,1,1]
#R
week2  = [1,0,0,0,0,0,1]
week3  = week2
week4  = [1,0,1,0,1,1,1]
week5  = week2
week6  = [1,0,0,1,0,0,1]

week7  = week1
#Y
week8  = [1,0,0,1,1,1,1]
week9  = [1,0,0,0,1,1,1]
week10 = [1,1,1,0,0,0,1]
week11 = week10
week12 = week9
week13 = week8

week14 = week1
#A
week15 = week2
week16 = week2
week17 = week4
week18 = week2
week19 = week2

week20 = week1
#N
week21 = week2
week22 = week2
week23 = [1,1,0,0,1,1,1]
week24 = [1,1,1,0,0,1,1]
week25 = week2
week26 = week2
week27 = week1

daysToCommit = [week1,week2,week3,week4,week5,week6,week7,week8,week9,week10,week11,week12,week13,week14,week15,week16,week17,week18,week19,week20,week21,week22,week23,week24,week25,week26,week27]

'''
for i in daysToCommit:
	for j in i:
		print(j)
#'''

writeNew = False

fileR = open("Dates.txt",'r').read()
#print(fileR)
day = str(int(now.strftime("%j"))) # %j just gets the # of days since new years, then int removes 0's 
#day  = "102"

#print(int((int(day) - startDay) /7), int((int(day)-startDay)%7))
drawToday = daysToCommit[int((int(day) - startDay) /7)][int((int(day)-startDay)%7)] == 1 #Getting weather to paint on that day based on the drawing
#print(drawToday)


writeNew = (not (day in fileR)) and (drawToday)
print(writeNew)
print(day)

#'''
if(writeNew):
	file = open("Dates.txt",'a')
	file.write("\n" + day)#make a change to any file so github can commit something
	file.close()
#'''

#rint(str(now.day))