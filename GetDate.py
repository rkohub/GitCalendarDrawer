from datetime import datetime
import os

now = datetime.now()

file = open("Dates.txt",'a')

file.write("\n" + str(now))
file.close()
#print(now)