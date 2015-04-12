SourceFile = '4e5Ice223Temp260.lammpstrj'
BeginLine = []
EndLine = []

NeedStep = [0,1,10]
HONum = 27648
PtNum = 1782
LinesNumPerStep = 9 + HONum + PtNum

for Steps in NeedStep:
	Begin = Steps * LinesNumPerStep + 1
	End   = (Steps+1) * LinesNumPerStep
	BeginLine.append(Begin)
	EndLine.append(End)

f = open(SourceFile,'r')

w = []
for i in range(len(NeedStep)):
	FileName = 'data.' + str(NeedStep[i])
	print FileName
	w.append(open(FileName,'w'))


i = 0
while True:
	line = f.readline()
	i += 1
	if not line:break
	for j in range(len(NeedStep)):
		if (i>=BeginLine[j] and i<=EndLine[j]):
			w[j].write(line)

for i in w:
	i.close()

f.close()
	