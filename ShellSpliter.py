import os

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


for i in range(len(NeedStep)):

	Instruction = 'sed -n '+ str(BeginLine[i])+','+ str(EndLine[i]) + 'p ' + SourceFile +' > ' + 'data.' + str(NeedStep[i]) 
	print Instruction
	os.system(Instruction)

