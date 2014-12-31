import os

def callVamp(str):
	l = len(str)
	filename = ""
	i = 0
	while i < l-4:
		filename += str[i]
		i+=1
	print str, filename
	os.system("./sonic-annotator -d vamp:silvet:silvet:notes " + str + "  -w csv --csv-one-file " + filename + "_silvet")
	os.system("./sonic-annotator -d vamp:nnls-chroma:chordino:simplechord " + str + "  -w csv --csv-one-file " + filename + "_chord")
	os.system("./sonic-annotator -d vamp:libvamp_essentia:OnsetDetection_33:onsets " + str + "  -w csv --csv-one-file " + filename + "_onset")
	return filename
