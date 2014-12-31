'''
===================================================
									  silvetKeys.py 
===================================================
'''
import csv
from operator import itemgetter


#==================================================
# 								          organize
#==================================================
# IN: filepath, min velocity to keep, min duration to keep
# OUT: array of keys, filtered by velocity & duration
#-------------------------------------------------- 
def organize(str, vel_min, dur_min):
	
	# Variables
	keys = []

	# Open Reader
	file = open(str + "_silvet")
	reader = csv.reader(file)
	for line in reader:
		velocity_line = int(line[4])
		duration_line = float(line[2])
		if(velocity_line > vel_min and duration_line > dur_min):
			# if note > D#5, ignore
			lineSp = list(line[5])
			# print lineSp
			if(lineSp[1] == "#"):
				if(lineSp[0] == "E", "F", "G", "A", "B" and int(line[5][2]) >= 5):
					# if(int(line[5](2)) >= 5):
					# 	# Do Nothing, Ignore Line
					zero = 0
			elif(int(line[5][1]) > 5):
				#Do Nothing, Ignore Line
				zero = 0
			else:
				keys.append(line)
			# print line
	# Close Reader
	file.close()
	return keys


def writeFile(out):
	# Open write file
	file = open(out,'w')
	writer = csv.writer(file)
	writer.writerows(out)
	# Close write file
	file.close()


#==================================================
# 								           colToVar
#==================================================
# IN: array to get col from, index of col to get
# OUT: col
#-------------------------------------------------- 
def colToVar(keys,col):
	r = []
	count = 0
	for i in keys:
		r.append(keys[count][col])
		count += 1
	return r



#==================================================
# 								       getTotalTime
#==================================================
# IN: col
# OUT: sum of col
#-------------------------------------------------- 
def getTotalTime(duration):
	return sum(duration)
	# tot = 0
	# for i in duration:
	# 	tot += float(i)
	# return tot



#==================================================
# 								   getOrderDuration
#==================================================
# IN: list of lists, duration col
# OUT: list of lists sorted by longest duration
#-------------------------------------------------- 
def getOrderDuration(keys):
	return sorted(keys, key=itemgetter(2))



#==================================================
# 								      getPercentage
#==================================================
# IN: number, total number
# OUT: number/totalnumber
#-------------------------------------------------- 
def getPercentage(num, tot):
	return float(num)/float(tot)




def getPercentDuration(duration):
	tot = getTotalTime(duration)
	percent = []
	count = 0
	for i in duration:
		percent.append(getPercentage(i, tot))
		# print percent[count]
		count +=1









