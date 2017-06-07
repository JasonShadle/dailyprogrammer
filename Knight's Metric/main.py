#194 0 doesn't work
xcord = []
ycord = []
xtotal = 0
ytotal = 0
endpoint = input('Enter ending point:')
endcord = endpoint.split()
bflip = False

if abs(int(endcord[0])) > abs(int(endcord[1])):
    b = abs(int(endcord[0]))
    a = abs(int(endcord[1]))
else:
    b = abs(int(endcord[1]))
    a = abs(int(endcord[0]))
    bflip = True

if int(endcord[0]) < 0:
    aneg = True
if int(endcord[1]) < 0:
    bneg = True

while True:

    if (xtotal == int(endcord[0])) & (ytotal == int(endcord[1])):
        break

    if bflip:
        if a - xtotal > b - ytotal:
            bflip = False
        elif (b - ytotal == 3) & (a-xtotal == 1):
            xcord.append(2)
            ycord.append(1)
            xcord.append(-1)
            ycord.append(2)
            xtotal += 1
            ytotal += 3
        elif b - ytotal >= 2:
            if a - xtotal > 0:
                xcord.append(1)
                ycord.append(2)
                xtotal += 1
                ytotal += 2
            else:
                xcord.append(-2)
                ycord.append(1)
                xcord.append(2)
                ycord.append(1)
                xtotal += 0
                ytotal += 2
        else:
            if a - xtotal == 1:
                xcord.append(2)
                ycord.append(-1)
                xcord.append(-1)
                ycord.append(2)
                xtotal += 1
                ytotal += 1
            else:
                xcord.append(1)
                ycord.append(2)
                xcord.append(1)
                ycord.append(-2)
                xcord.append(-2)
                ycord.append(1)
                xtotal += 0
                ytotal += 1
    else:
        if a - ytotal > b - xtotal:
            bflip = True
        elif (b - xtotal == 3) & (a - ytotal == 1):
            ycord.append(2)
            xcord.append(1)
            ycord.append(-1)
            xcord.append(2)
            ytotal += 1
            xtotal += 3
        elif b - xtotal >= 2:
            if a - ytotal > 0:
                ycord.append(1)
                xcord.append(2)
                ytotal += 1
                xtotal += 2
            else:
                xcord.append(2)
                ycord.append(1)
                xcord.append(2)
                ycord.append(-1)
                xtotal += 4
                ytotal += 0
        else:
            if a - ytotal == 1:
                ycord.append(2)
                xcord.append(-1)
                ycord.append(-1)
                xcord.append(2)
                ytotal += 1
                xtotal += 1
            else:
                ycord.append(1)
                xcord.append(2)
                ycord.append(1)
                xcord.append(-2)
                ycord.append(-2)
                xcord.append(1)
                ytotal += 0
                xtotal += 1
print('Total steps: ' + str(len(xcord)))
for x in range(0,len(xcord)):
    print('(' , xcord[x] , ', ' , ycord[x] , ')' )