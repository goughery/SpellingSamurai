import re

word = 'bicycle'

lettersCombos = ['[zc]', '[cz]', '[mn]', '[nm]', '[bd]', '[db]', '[td]', '[dt]', '[bp]', '[pb]']

replaceDict = {}
for i in range(len(word)):
    replaceDict[i] = []
    for combo in lettersCombos:
        if word[i] in combo[1]:
            replaceDict[i].append(combo)

for key in replaceDict:
    if not replaceDict[key]:
        replaceDict[key] = word[key]

#print(replaceDict)
regExL = []
for key in replaceDict:
    multCombo = ""
    for combo in replaceDict[key]:
        if replaceDict[key].index(combo) == 0 and len(replaceDict[key])>1:
            combo = combo.replace("]", "")
        elif replaceDict[key].index(combo) != 0 and combo != replaceDict[key][-1]:
            combo = combo.replace("[", "")
            combo = combo.replace("]", "")
        elif len(replaceDict[key]) > 1:
            combo = combo.replace("[", "")
        multCombo += combo
    multComboDD = ""
    for letter in multCombo:
        if letter not in multComboDD:
            multComboDD += letter
    regExL.append(multComboDD)
 

#print(regExL)

regExS = ""
for item in regExL:
    regExS += item
#print(regExS)

rX = re.compile(regExS)


while True:
    inp = input("\ntype: ")
    if rX.match(inp):
        print("You spelled it correctly!")
    else:
        print("Incorrect!")



##    for part in replaceDict[key]:
##        
##        regExL.append(part)



##for i in range(len(regExL)):
##    fuck = 0
##    print(len(regExLL))
##    #if '[' in regExL[0] and '[' in regExL[1]:
##        
##    if (i!=len(regExL)):
##        if ('[' in regExL[i] and '[' in regExL[i+1]):
##            if regExL[i][0] == regExL[i+1][0] or regExL[i][1] == regExL[i+1][0] or regExL[i][0] == regExL[i+1][1] or regExL[i][1] == regExL[i+1][1]:
##                repl = regExL[i].replace('[',"").replace(']',"") + regExL[i+1].replace('[',"").replace(']',"")
##                repldd = ""
##                for letter in repl:
##                    if letter not in repldd:
##                        repldd += letter
##                regExLL.append('['+repldd+']')
##                fuck = 1
##
##    if fuck == 0:
##        regExLL.append(regExL[i])
       

                       
##    elif '[' in regExL[i]:
##        regExLL.append(regExL[i]
##    elif :
##        #print(regExL[i])
##        regExLL.append(regExL[i])

#print(regExLL)


##for combo in lettersCombos:
##    if combo[0] in word or combo[1] in word:
##        match = match.replace(combo[0], '['+combo +']')
##        match = match.replace(combo[1], '['+combo +']')
##        match = match.replace('['+combo[0]+'[', '[')
##        match = match.replace('['+combo[1]+'[', '[')
##        match = match.replace('[[','[')
##        match = match.replace(']]', ']')
##        

#print(match)
##wordIndices = {}

##for i in range(len(word)):
##    for combo in lettersCombos:
##        if word[i] in combo:
##            print(word[i])
##            print(combo)
##            wordIndices[i] = combo
##        else:
##            wordIndices[i] = word[i]
##
##print(wordIndices)


##for combo in lettersCombos:
##    for i in range(len(word)):
##        print(word[i])
##        
##        if word[i] in combo[0]:
##            wordIndices[i] = combo
##            
##        else:
##            wordIndices[i] = word[i]
##
##print(wordIndices)
