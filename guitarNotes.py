'''
===================================================
									 guitarNotes.py 
===================================================
'''
import sys
#import chord.py
from music21 import *

#==================================================
# 								   Labels for Notes
#==================================================
keybins = ["E2","F2","F#2","G2","G#2","A2",
		   "A#2","B2","C3","C#3","D3","D#3",
		   "E3","F3","F#3","G3","G#3","A3",
		   "A#3","B3","C4","C#4","D4","D#4",
		   "E4","F4","F#4","G4","G#4","A4",
		   "A#4","B4","C5","C#5","D5","D#5"]

# String position in corresponding keybin index key
key_st_pos = [[0], [0], [0], [0], [0], [0,1], [0,1], [0,1], [0,1], [0,1], [0,1,2], 
		   [0,1,2], [1,2], [1,2], [1,2], [1,2,3], [1,2,3], [2,3],[2,3],[2,3,4],
		   [2,3,4], [2,3,4], [3,4],[3,4],[3,4,5],[3,4,5], [3,4,5], [4,5],[4,5],
		   [4,5], [4,5], [5],[5],[5],[5], [5] ]

# Fret position in corresponding keybin index key
key_fr_pos =   [[0], [1], [2], [3], [4], [5,0], [6,1], [7,2], [8,3], [9,4], [10,5,0],
           [11,6,1],[7,2], [8,3], [9,4], [10,5,0],[11,6,1],[7,2],[8,3],[9,4,0],
           [10,5,1],[11,6,2],[7,3],[8,4],[9,5,0],[10,6,1],[11,7,2],[8,3],[9,4],
           [10,5],[11,6],[7],[8],[9],[10],[11] ]

#==================================================
# 									   Build Guitar
#==================================================
string = [0,1,2,3,4,5]
fret = [0,1,2,3,4,5,6,7,8,9,10,11]
c = [0, 5, 10, 15, 19, 24] # Keybin index starting point

# Fretboard
fretboard = []
for s in string:
	k = c[s]
	for f in fret:
		fretboard.append(keybins[k])
		k+=1

# Strings
string0 = fretboard[0:12]
string1 = fretboard[12:24]
string2 = fretboard[24:36]
string3 = fretboard[36:48]
string4 = fretboard[48:60]
string5 = fretboard[60:72]

stringValue = [fretboard[0:12],fretboard[12:24],fretboard[24:36],fretboard[36:48],fretboard[48:60],fretboard[60:72]]
# print "e: ",string5
# print "B: ",string4
# print "G: ",string3
# print "D: ",string2
# print "A: ",string1
# print "E: ",string0

#==================================================
# 								 			  Scale
#==================================================



#==================================================
# 								 Find Note or Index
#==================================================
# IN: note
# OUT: index
def getNoteIndex(note):
	count = 0
	for i in keybins:
		if (i == note):
			return count
			break
		count += 1

# IN: index 
# OUT: note
def getNote(ind):
	count = 0
	if(ind > len(keybins)):
		return "\n ** Out of index\n"

	count = 0
	for i in keybins:
		if (count == ind):
			return i
			break
		count += 1

# IN: x = index of key, y = index of string
# OUT: string pos
def getFretboardStringNote(x,y):
	return key_st_pos[int(x)][int(y)]

# IN: x = index of key, y = index of fret
# OUT: string pos
def getFretboardStringFret(x,y):
	return key_fr_pos[int(x)][int(y)]

# IN: stringValue index 
# OUT: Array of notes in
def getStringValue(stringNumber):
	return stringValue[stringNumber]
#==================================================
# 								potentialStringList
#==================================================
# IN: index
# OUT: list of potential strings at index
#-------------------------------------------------- 
def getPotentialStringList(ind):
	count = 0
	if(ind > len(keybins)):
		return "\n invalid index"
	for i in key_st_pos:
		if (count == ind):
			return i
			break
		count += 1

#==================================================
# 								potentialFretList
#==================================================
# IN: index
# OUT: list of potential fret at index
#-------------------------------------------------- 
def getPotentialFretList(ind):
	count = 0
	if(ind > len(keybins)):
		return "\n invalid index"
	for i in key_fr_pos:
		if (count == ind):
			return i
			break
		count += 1


#==================================================
# 							getHighestPercentString
#==================================================
# IN: ind_in
# OUT: ind_out for max key_st_pos[ind_in][ind_out]
#-------------------------------------------------- 
def getHighestPercentString(ind):
	count = 0
	m = 0
	# if(ind > len(keybins)):
	# 	return "\n invalid index"
	check = key_st_pos[ind]
	for i in check:
		if (m < i):
			m = count
		count += 1
	return m


#==================================================
# 									Potential Notes
#==================================================
# IN: note
# OUT: [ List of Strings, List of Frets ]
def potentialNote(note):
	count = 0
	s = []
	f = []
	# print getNoteIndex(note)

	# E String - string0
	for i in string0:
		if (note == i):
			s.append(0)
			f.append(count)
		count += 1

	# A String - string1
	count = 0
	for i in string1:
		if (note == i):
			s.append(1)
			f.append(count)
		count += 1

	# D String - string2
	count = 0
	for i in string2:
		if (note == i):
			s.append(2)
			f.append(count)
		count += 1

	# G String - string3
	count = 0
	for i in string3:
		if (note == i):
			s.append(3)
			f.append(count)
		count += 1

	# B String - string4
	count = 0
	for i in string4:
		if (note == i):
			s.append(4)
			f.append(count)
		count += 1

	# e String - string5
	count = 0
	for i in string5:
		if (note == i):
			s.append(5)
			f.append(count)
		count += 1

	return [s, f]

#==================================================
# 										 splitIndex
#==================================================
# IN: total
# OUT: if note = E2, F2, F#2, G2, G#2 return index where note is
#-------------------------------------------------- 
def splitIndex(total):
	splitIndexAt = []
	for i in total:
		if (i == "E2", "F2", "F#2", "G2", "G#2"):
			splitIndexAt.append(1)
		else:
			splitIndexAt.append(0)
	return splitIndexAt












