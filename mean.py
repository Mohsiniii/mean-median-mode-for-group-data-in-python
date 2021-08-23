# for group data
groupData = [[150,154,5],[155,159,2],[160,164,6],[165,169,8],[170,174,9],[175,179,11],[180,184,6],[185,189,3]]
x = []
fx = []
sfx = 0
cFrequencies = []
fm = -1
fmIndex = -1
for i in range(len(groupData)):
    x.append((groupData[i][0]+groupData[i][1])/2)
    fx.append(((groupData[i][0]+groupData[i][1])/2)*groupData[i][2])
    sfx += ((groupData[i][0]+groupData[i][1])/2)*groupData[i][2]
    if(i == 0):
        cFrequencies.append(groupData[i][2])
    else:
        cFrequencies.append(cFrequencies[i-1]+groupData[i][2])
    if(groupData[i][2] > fm):
        fm = groupData[i][2]
        fmIndex = i

sf = cFrequencies[-1]
mean = sfx/sf
print("Mean: ", mean)
