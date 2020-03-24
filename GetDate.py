from datetime import datetime

now = datetime.now()

file = open("Dates.txt",'a')

file.write("\n" + str(now))
file.close()
print(now)