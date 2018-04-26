# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 19:57:45 2018

@author: aagre
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:31:08 2018

@author: aagre
"""

# Create a class to hold the values of the spaceship.
class Spaceship:
    def __init__(self, idin=0, startTime=0, endTime=0, score=0, index=0):
        self.idin = idin
        self.startTime = startTime
        self.endTime = endTime
        self.score = score

# Functions to validate the inputs       
def validN(N):
    if (N >= 0 and N <= 70000):
        return True
    else:
        return False

def validID(idin):
    if (idin >= 0 and idin <= pow(10,9)):
        return True
    else:
        return False

def validTime(sTime, eTime):
    if (sTime >= 0 and sTime < eTime and eTime <= pow(10,18)):
        return True
    else:
        return False

def isDuplicate(listSpaceShip, idin, sTime, eTime):
    for i in listSpaceShip:
        if (i.idin == idin and i.startTime == sTime and i.endTime == eTime):
            return False
    return True

# Function to calculate the score for the spaceship.
def calcScore(listSpaceShip):
    for i in range(len(listSpaceShip)):
        score = 0
        j=0
        for idx in indexDict.keys():
            if listSpaceShip[i].startTime >= idx[0] and listSpaceShip[i].startTime <= idx[1]:
                j = indexDict[idx]

        if len(scoredListSpaceShip[j]) > 0:
            for ele in scoredListSpaceShip[j]:
                if ele.startTime > listSpaceShip[i].startTime:
                    score += 1

        for k in range(j+1,101):
            score= score + len(scoredListSpaceShip[k])

        listSpaceShip[i].score = score
        scoredListSpaceShip[j].append(listSpaceShip[i])


def calcPercentile(inlist):
    res = []
    for i in range(1,101):
        if i == 0:
            res.append(inlist[0])
        elif i == 100:
            res.append(inlist[-1])
        else:
            res.append(inlist[int(round((i/100)*len(inlist) + 0.5))-1])
    
    return res



#---------------------------------------------------------------------------------
# Main code Execution starts here
#---------------------------------------------------------------------------------
#
fhandle = open('input004.txt','r')

for i in fhandle:
    N = int(i)
    break

#N = int(input())   # accept the number of spaceships competing

if not validN(N):  # check if N is a valid number
    exit()

scoredListSpaceShip = []   # define a list to store the buckets
indexDict = {}             # define a dict to hold tuple of bucket start and end time as keys and index of the bucket as values

for i in range(101):
    scoredListSpaceShip.append([])  # create buckets in the list.


listSpaceShip = []        # list to accept the input spaceship logs

# Accept inputs


for i in range(N):
    idin, sTime, eTime = input().split()
    idin = int(idin)
    sTime = int(sTime)
    eTime = int(eTime)

    # check the validity of the input
    if(validID(idin) and validTime(sTime, eTime) and isDuplicate(listSpaceShip, idin, sTime, eTime)):
        listSpaceShip.append(Spaceship(idin, sTime, eTime))     # if valid accept the input by creating the object of class Spaceship    

# Sort the spaceship list in sorted start time.
listSpaceShip.sort(key=lambda x:x.startTime)

startTimes = [x.startTime for x in listSpaceShip]

# Any two consecutive percentiles have equal number of samples between them.
# Hence, using percentiles on start time to define the bucket boundries.
a = calcPercentile(startTimes)

# Create indexes for the buckets.
j=0
for i in range(len(a)-1):
    indexDict[(a[i], a[i+1])] = j
    j += 1

# sort the inputs based on the end times of each spaceship in ascending order.
listSpaceShip.sort(key=lambda x:x.endTime)

# invoke the function calcScore to calculate the score for each spaceship
calcScore(listSpaceShip)

finalList = []    # list to hold the final score updated data.

for bucket in scoredListSpaceShip:
    finalList.extend(bucket)

finalList.sort(key=lambda x:(x.score, x.idin))

for ele in finalList:
    print("%d %d" %(ele.idin, ele.score))