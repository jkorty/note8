'''
===================================================
										 makeTab.py 
===================================================
'''
import guitarNotes
import silvetKeys
import math



#==================================================
# 								          noteToBin
#==================================================
# IN:
# OUT:
#-------------------------------------------------- 
def noteToBin(notes):
	stringBin = []
	fretBin = []
	for i in notes:
		[ x, y ] = guitarNotes.potentialNote(i)
		stringBin.append(x)
		fretBin.append(y)
	return [stringBin,fretBin]


#==================================================
# 		   					           noteBinArray
#==================================================
# IN:
# OUT:
#-------------------------------------------------- 
def noteBinArray(potential):
	fb_counter = [0]*72
	count = 0
	for i in potential:
		k = 0
		for j in i:
			n = 0
			for t in j:
				if(count < len(potential)-1):
					# print "Note: ",note_octave[k],";\t < ",potential[count][k][n],", ",potential[count+1][k][n]," >"
					# print "Note Index: ",potential[count][k][n]*12+potential[count+1][k][n]
					fb_counter[potential[count][k][n]*12+potential[count+1][k][n]] += 1
				n += 1
			k += 1
		count += 1
	return fb_counter

#==================================================
# 								         binPercent
#==================================================
# IN:
# OUT: array of fretboard, value = percentage
#-------------------------------------------------- 
def binPercent(fb_counter,totalNotes):
	fb_counter_percent = fb_counter
	n = 0
	for i in fb_counter:
		fb_counter_percent[n] = round(float(float(i)/float(totalNotes)),4)
		# print float(float(i)/float(totalNotes))
		n+=1
	return fb_counter_percent


#==================================================
# 								         calcString
#==================================================
# IN: note
# OUT: string array
#-------------------------------------------------- 
def getSFVectorArray(note):
	stringFound = -1
	# Note Index
	note_ind = guitarNotes.getNoteIndex(note)
	# Potential strings:
	if ( guitarNotes.getPotentialStringList(note_ind) != "None" and guitarNotes.getPotentialFretList(note_ind) != "None"):
		return guitarNotes.getPotentialStringList(note_ind), guitarNotes.getPotentialFretList(note_ind)
	else:
		return "Null"


	# find highest percentage for note
	# strInd = guitarNotes.getHighestPercentString(note)
	# stringFound = guitarNotes.getFretboardStringNote(note_ind,strInd)

	# know note: X(N), use index of this note
	# return stringFound

#==================================================
# 								           featNorm
#==================================================
# IN: list of features
# OUT: normalized list of features
#-------------------------------------------------- 
def featNorm(feat):
	# find min a
	a = min(feat)
	# find max b
	b = max(feat)
	count = 0
	for i in feat:
		feat[count] = (i-a)/(b-a)
		count+=1
	return feat


#==================================================
# 								         timeGather
#==================================================
# IN: total vector, time start, total time
# OUT: timeSliced: list of [ list of indexes of notes in time slice ]
#-------------------------------------------------- 
def timeGather(time, posToTab, totTime):
	totTime = float(totTime)

	timeSliced = []
	sVec = posToTab[0]
	fVec = posToTab[1]
	last = -1
	count = 0
	t = 0
	while ( t < totTime ):
		lineCount = 0
		addList = []
		for line in posToTab:
			if (float(time[lineCount]) <= t and float(time[lineCount]) > last):
				addList.append(lineCount) 
			lineCount+=1
		timeSliced.append([t,addList])
		last = t
		t += 0.023
		count +=1
	return timeSliced

#==================================================
# 								           printTab
#==================================================
# IN: list of vectors, corresponding time vector, total time
# OUT: tab
#-------------------------------------------------- 
def printTab(noteOut,timeSliced,time,totalTime):
	lineHead = [ "e =|", "B =|", "G =|", "D =|", "A =|", "E =|" ]
	tab = [ "","","","","","" ]
	timeSlice = [0]*len(timeSliced)
	last = 0
	# print t
	count = 0
	for t in timeSliced:
		flag = 0
		numberOfNotes = len(t[1])
		addList = []
		k = 0
		for n in noteOut:
			# print "last: ",last," < time[",k,"]: ", time[k]," <= t @ ",count,": ",t[0]
			if( last < float(time[k]) <= t[0] ):
				# print "Slice[",count,"] = string: ",noteOut[k][0]," , fret: ", noteOut[k][1]
				addList.append([ noteOut[k][0], noteOut[k][1] ])
				flag = 1
			else:
				flag = 0
			k += 1
		timeSlice[count] = addList
		count += 1
		last = t[0]

	# count = 0
	# for i in timeSlice:
	# 	print count,i
	# 	count +=1 
	
	count = 0
	for i in timeSlice:
		if (len(i)>0):
			x = 0
			# while( count is smaller than total slices of time )
			while ( x < len(i) ):
				# DEBUG: print "Count ",count,": ",timeSlice[count][x]
				# tab[string] += fret number + "-"
				tab[ 5-timeSlice[count][x][0] ] += str( timeSlice[count][x][1] ) + "-"
				# if ( fret number < 10 ), then add another "-" to the end 
				if ( timeSlice[count][x][1] < 10 ):
					tab[ 5-timeSlice[count][x][0] ] += "-"
				r = 0
				# while r is smaller than the number of strings in tab
				while( r < len(tab) ):
					if( r != 5-timeSlice[count][x][0] ):
						# print "r: ",r," 5-timeSlice[count][x][0]: ", 5-timeSlice[count][x][0]
						tab[r] += "---"
					r+=1
				x+=1
		else:
			k=0
			for s in tab:
				tab[k] += ""
				k+=1
		if ( count%45 == 1 ):
			k=0
			for s in tab:
				tab[k] += "|"
				k+=1
		count += 1  


			
	# skip = 10
	# count = 0
	# for i in tab:
	# 	tab[count] = tab[count].split("|")
	# 	count += 1

	count = 0
	# while( count < len( tab ) ):
	k=0
	for i in lineHead:
		print lineHead[k],tab[k]
		k+=1
	count += 1


	# return timeSlice
		# k = 0
		# for i in t[1]:
		# 	countOfNoteInSlice = 0
		# 	for j in tab:
		# 		print tab[int(t[0][countOfNoteInSlice])]
		# 		countOfNoteInSlice += 1



	# 	for line in noteOut:
	# 		tab[k] = str(tab[k])
	# 		if( last < timeSliced[k][0] < timeSliced[k+1][0] ):
	# 			tab[k] = noteOut[k][1]
	# 		else: 
	# 			tab[k] += "----"

	# 		# if (count%3 == 0):
	# 		# 	tab[k] += "-|-"

	# 		k+=1
	# 	last = t
	# 	count+=1
	# 	if( count >= len(timeSliced)-1):
	# 		break
	
	# count = 0
	# for i in tab:
	# 	print lineHead[count],i
	# 	count += 1


	# # t = minTime
	# t = 0
	# # count = count of while
	# # k = i in total
	# popFlag = 0
	# count = 0
	# while ( t <= float(totalTime) ):
	# 	stringUsed = [ 0,0,0,0,0,0 ]
		
	# 	#print count
	# 	k = 0
	# 	for i in time:
	# 		if ( float(i) <= float(t) ):
	# 			print i, t, k, sfVector[k]
	# 			# if( len(str(sfVector[k][1])) == 2 ):
	# 			# 	tab[sfVector[k][0]] += "-" + str(sfVector[k][1]) + "-"
	# 			# 	stringUsed[ sfVector[k][0] ] = 1
	# 			# 	sfVector.pop(k)
	# 			# 	popFlag = 1
	# 			# else:
	# 			# if( i <= t ):
	# 			tab[sfVector[k][0]] += "-" + str(sfVector[k][1]) + "--"
	# 			stringUsed[ sfVector[k][0] ] = 1
	# 			sfVector.pop()
	# 			popFlag = 1
	# 			k+=1
	# 			if (popFlag == 1):
	# 				if (k<1):
	# 					k = k-1
	# 				else:
	# 					k = 0	
	# 	ctr = 0
	# 	for a in stringUsed:
	# 		if( a != 1 ):
	# 			tab[ ctr ] = "----"
	# 		ctr += 1
	# 	count += 1
	# 	t += 0.023			

	# time slices start at 0
	# count = 0
	# t = 0
	# while (t < totalTime):
	# 	#  and float(time[count]) < t
	# 	stringUsed = [0,0,0,0,0,0]
	# 	sliceCount = count
	# 	while(float(time[count]) == float(time[count + 1])):
	# 		if (sfVector[sliceCount][1] > 9):
	# 			tab[5-sfVector[sliceCount][0]] += "-" + str(sfVector[sliceCount][1]) + "-"
	# 		else:
	# 			tab[5-sfVector[sliceCount][0]] += "-" + str(sfVector[sliceCount][1]) + "--"
	# 		stringUsed[5-sfVector[sliceCount][0]] = 1
	# 		sliceCount += 1
	# 	stringC = 0
		
	# 	for i in stringUsed:
	# 		if (i != 1):
	# 			tab[stringC] += "----"*int(sliceCount-count)

	# 	count = sliceCount + 1

	# 	if (sfVector[count][1] > 9):
	# 		tab[5-sfVector[count][0]] += "-" + str(sfVector[count][1]) + "-"
	# 	else:
	# 		tab[5-sfVector[count][0]] += "-" + str(sfVector[count][1]) + "--"
		
		# count += 1
		# t += 0.023

		





		# Debug Output
		# print "time[",count,"], t = ",float(time[count]), t

		# While the onset time is less than the current time slice
		# while (float(time[count]) < t):
			# print "5-sfVector[count][0]",5-sfVector[count][0],sfVector[count][1]

			# If the this time is the same as the next time
			# if(float(time[count]) == float(time[count+1])):
			# 	# time slice counter
			# 	sliceCount = int(count)

				# while the time is the same as the next time 
		# 		while(float(time[sliceCount]) == float(time[sliceCount+1])):
		# 			# mark whether a string is used
		# 			stringUsed = [0,0,0,0,0,0]
		# 			k=0
		# 				#print sfVector[count][0], sfVector[count][1]
		# 			if(k == int(5-sfVector[sliceCount][0])):
		# 				if (sfVector[sliceCount][1] > 9):
		# 					tab[5-sfVector[sliceCount][0]] += "-" + str(sfVector[sliceCount][1]) + "-"
		# 				else:
		# 					tab[5-sfVector[sliceCount][0]] += "-" + str(sfVector[sliceCount][1]) + "--"
		# 				stringUsed[k] = 1
		# 			k+=1
		# 			sliceCount += 1
		# 		for y in tab:
		# 			for i in stringUsed:
		# 				if(i == 0):
		# 					tab[5-sfVector[sliceCount][0]] += "----"*(sliceCount-count)
		# 		count = sliceCount + 1
		# 	else:
		# 		k=0
		# 		#print sfVector[count][0], sfVector[count][1]
		# 		if(k == int(5-(sfVector[count][0]))):
		# 			if (sfVector[count][1] > 9):
		# 				tab[5-sfVector[count][0]] += "-" + str(sfVector[count][1]) + "-"
		# 			else:
		# 				tab[5-sfVector[count][0]] += "-" + str(sfVector[count][1]) + "--"
		# 		else:
		# 			tab[5-sfVector[count][0]] += "----"
		# 		k+=1
		# 		count +=1
		# # Increment time by time window (0.023, 23 ms for 1024/44100; 4096/44100 would be 0.093)
		# t += 0.023


			