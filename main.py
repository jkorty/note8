import sys
import callVamp
import silvetKeys
import guitarNotes
import makeTab
import chordLib

filename = sys.argv[1]
keys = []
vmin = 0
dmin = 0.01
splitMin = 0

if __name__ == "__main__":
	
	#filepath = callVamp.callVamp(filename)
	filepath = "/Users/jkorty/Desktop/say"
	
	# Pull info from CSV
	keys = silvetKeys.organize(filepath, vmin, dmin)

	# CSV info to variables
	time = silvetKeys.colToVar(keys,1) # Time note found
	duration = silvetKeys.colToVar(keys,2) # How long note sustained
	frequency = silvetKeys.colToVar(keys,3) # Frequency of note
	velocity = silvetKeys.colToVar(keys,4) # Intensity of note
	note_octave = silvetKeys.colToVar(keys,5) # Note and Octave

	# Combine variables to total
	total = [] # All variables
	count = 0
	for i in time:
		total.append([time[count], duration[count], frequency[count], velocity[count], note_octave[count]])
		count += 1

	# Order notes by duration
	duration_total = []
	duration_total = silvetKeys.getOrderDuration(total)

	# Notes counted to bins
	potential = makeTab.noteToBin(note_octave)
	
	# Notes to array
	fb_counter = makeTab.noteBinArray(potential)

	# Notes / Total Notes
	totalNotes = len(note_octave)
	splitIndex = guitarNotes.splitIndex(note_octave)
	# for i in splitIndex:
	# 	print i
	fb_counter_percent = makeTab.binPercent(fb_counter, totalNotes)
	
	# Add up percentage of notes in values
	stringSum = [] 		# % by string
	fretSum = [0]*12	# % by fret
	
	count = 0
	k = 0
	# print "Length fb_counter_percent: ",len(fb_counter_percent)
	while (count < 6):
		total = 0
		# print "STRING #",count,": "
		s = guitarNotes.getStringValue(count)
		r = 0
		for i in s:
			# print "Note: ",i," = ",fb_counter_percent[k]
			fretSum[r] += fb_counter_percent[k]
			total += fb_counter_percent[k]
			if(r == 11):
				r = 0
			r+=1
			k+=1
		stringSum.append(total)
		count += 1
	# print stringSum
	# print fretSum
	
	# Normalize string likelihoods
	stringSum = makeTab.featNorm(stringSum)
	fretSum = makeTab.featNorm(fretSum)

	# print stringSum
	# print fretSum

	# Note to tab
	notesToTab = []
	# Position of note to tab
	posToTab = []

	# Assign notesToTab and posToTab
	count = 0
	for i in note_octave:
		notesToTab.append(i)
		if (makeTab.getSFVectorArray(i) != "Null"):
			# print "Strings Possible for ",i,": <",makeTab.getSFVectorArray(i),">"
			posToTab.append(makeTab.getSFVectorArray(i))
		# else:

		count += 1

	# Find highest percent String, Fret by percentage
	#
	#						     Note 1               Note 2
	#                       |------------------|  |--------------|
	# For n in notesToTab [ [ [0,0,0], [0,0,0] ], [ [1,1], [1,1] ], ... ]   	level = n (for note); Counter = ctNote
	#
	#                           ctV     ctV+1 
	#					      |-----|  |-----|
	#					      [0,0,0], [0,0,0]								  	level = v (for vector); Counter = ctV
	#
	#					        x1 x2 x3
	#					       |-||-||-|
	#			       		  [ 0, 0, 0 ] 										level = x (for number in v); Counter = ctX
	#
	#
	noteOut = [0,0]*len(note_octave)
	# maxLikeValue = -1
	ctNote = 0
	for n in notesToTab:
		ctV = 0
		maxLikeValue = -1
		while(ctV < 1):
			ctX = 0
			for x in notesToTab[ctNote][ctV]:
				if( (posToTab[ctNote][ctV][ctX] + posToTab[ctNote][ctV+1][ctX]) > maxLikeValue):
					maxLikeValue = posToTab[ctNote][ctV][ctX]+posToTab[ctNote][ctV+1][ctX]
					noteOut[ctNote] = [posToTab[ctNote][ctV][ctX],posToTab[ctNote][ctV+1][ctX]]
				ctX += 1
			ctV += 1
		# print notesToTab[ctNote]," will use: ",noteOut[ctNote]," at time = ",time[ctNote]
		ctNote += 1
	# print "noteOUT:"
	# for i in noteOut:
	# 	print i

	totalTime = float(time[len(time)-1]) + float(duration[len(time)-1])

	# print "Total Time: ", totalTime
	# print "Length Notes: ", len(note_octave)
	minTime = min(time)

	timeSliced = makeTab.timeGather(time, posToTab, totalTime)
	# for i in timeSliced:
	# 	print i

	noteOut = noteOut[0:len(note_octave)]
	# print len(noteOut)
	# for i in noteOut:
	# 	print i

	# print "Size of timeSliced: ",len(timeSliced)
	# makeTab.createTab(timeSliced,posToTab)
	makeTab.printTab(noteOut,timeSliced,time,totalTime)


	testchord = chordLib.getChord("Fmin")
	print testchord

	"""
	TESTING:
	"""
	# print "e: ",fb_counter[60:72]
	# print "B: ",fb_counter[48:60]
	# print "G: ",fb_counter[36:48]
	# print "D: ",fb_counter[24:36]
	# print "A: ",fb_counter[12:24]
	# print "E: ",fb_counter[0:12]

	# print "\n\n"
	# print "e: ",fb_counter_percent[60:72]
	# print "B: ",fb_counter_percent[48:60]
	# print "G: ",fb_counter_percent[36:48]
	# print "D: ",fb_counter_percent[24:36]
	# print "A: ",fb_counter_percent[12:24]
	# print "E: ",fb_counter_percent[0:12]
	# for i in keys:
	# 	print i
	# for i in duration:
	# 	print i

	# print "Total time: ",silvetKeys.getTotalTime(duration),"\n"
	# print "\n\n", guitarNotes.getNoteIndex(note_octave[3])
	# print guitarNotes.getIndexNote(2)
	# silvetKeys.getPercentDuration(duration)




