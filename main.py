import copy
from tkinter import *
import matplotlib.pyplot as plt

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Disk Scheduling')


def FCFS(request, initialStart):
    print("FCFS Algorithm")
    x = 0
    drawX = []
    drawY = []
    totalHeadMovement = 0
    currentPosition = initialStart
    for req in request:
        totalHeadMovement += abs(req - currentPosition)
        currentPosition = req
        print(currentPosition, " is seeked")
        drawY.append(currentPosition)
        drawX.append(x)
        x+= 3

    print("Total Head Movement is ",totalHeadMovement)
    print("*************************")
    plt.plot(drawX,drawY)
    plt.show()
    return 0



def SSTF(Request, initialStart):
    request = copy.deepcopy(Request)
    print("SSTF Algorithm")
    totalHeadMovement = 0
    drawX = []
    drawY = []
    x = 0
    request.append(initialStart)
    request.sort()
    index = request.index(initialStart)
    i = index - 1  # move left
    j = index + 1  # move right
    while i >= 0 or j < len(request):

        if i >= 0 and (j >= len(request) or request[index] - request[i] < request[j] - request[index]):
            j -= 1
            totalHeadMovement += (request[index] - request[i])
            index = i
            print(request[index], " is seeked")
            drawY.append(request[index])
            drawX.append(x)
            x += 3
        else:
            i += 1
            totalHeadMovement += request[j] - request[index]
            index = j
            print(request[index], " is seeked")
            drawY.append(request[index])
            drawX.append(x)
            x += 3

        j += 1
        i -= 1
    print("Total Head Movement is ",totalHeadMovement)
    print("***************")
    plt.plot(drawX, drawY)
    plt.show()
    return 0

def SCAN(Request, initialStart):
    request = copy.deepcopy(Request)
    print("SCAN Algorithm")
    endOfDisk = 199
    drawX = []
    drawY = []
    x = 0
    totalHeadMovement = 0
    request.append(initialStart)
    request.sort()
    index = request.index(initialStart)
    i = index+1
    while i < len(request):
        totalHeadMovement += (request[i] - request[index])
        print(request[i], " is seeked")
        drawY.append(request[1])
        drawX.append(x)
        x += 3
        index = i
        i+=1
    totalHeadMovement += endOfDisk - request[len(request) - 1]
    print(endOfDisk, " is seeked")
    drawY.append(endOfDisk)
    drawX.append(x)
    x += 3
    index = request.index(initialStart)
    index-=1
    totalHeadMovement += endOfDisk - request[index]
    print(request[index], " is seeked")
    drawY.append(request[index])
    drawX.append(x)
    x += 3
    i = index - 1
    while i >= 0:
        totalHeadMovement += request[index] - request[i]
        print(request[i], " is seeked")
        drawY.append(request[i])
        drawX.append(x)
        x += 3
        index = i
        i-=1

    print("Total Head Movement is ",totalHeadMovement)
    print("********************")
    plt.plot(drawX, drawY)
    plt.show()
    return 0

def LOOK(Request, initialStart):
    request = copy.deepcopy(Request)
    print("LOOK Algorithm")
    drawX = []
    drawY = []
    x = 0
    endOfDisk = 199
    totalHeadMovement = 0
    request.append(initialStart)
    request.sort()
    index = request.index(initialStart)
    i = index+1
    while i < len(request):
        totalHeadMovement += (request[i] - request[index])
        print(request[i], " is seeked")
        drawY.append(request[i])
        drawX.append(x)
        x += 3
        index = i
        i+=1
    index = request.index(initialStart)
    index-=1
    totalHeadMovement += request[len(request) - 1] - request[index]
    print(request[index], " is seeked")
    drawY.append(request[index])
    drawX.append(x)
    x += 3
    i = index - 1
    while i >= 0:
        totalHeadMovement += request[index] - request[i]
        print(request[i], " is seeked")
        drawY.append(request[i])
        drawX.append(x)
        x += 3
        index = i
        i-=1
    print("Total Head Movement is ",totalHeadMovement)
    print("**********************")
    plt.plot(drawX, drawY)
    plt.show()
    return 0



#Cscan-Clook

def CSCAN(RequestArray, initial):
    requestArray = copy.deepcopy(RequestArray)
    print("CSCAN Algorithm")
    drawX = []
    drawY = []
    x = 0
    totalHeadMovement = 0
    requestArray.append(initial)
    requestArray.sort()  # queue = 14,37,53,65,67,98,122,124,183
    i = requestArray.index(initial)
    elementCounter = 1

    while i < len(requestArray) - 1:
        totalHeadMovement += abs(requestArray[i + 1] - requestArray[i])
        print(requestArray[i+1], " is seeked")
        drawY.append(requestArray[i+1])
        drawX.append(x)
        x += 3
        elementCounter += 1
        i += 1

    while elementCounter < len(requestArray):
        if i == len(requestArray) - 1:
            totalHeadMovement += 199 - requestArray[i]  # 199 - 183
            print(199, " is seeked")
            drawY.append(199)
            drawX.append(x)
            x += 3
            totalHeadMovement += 199  # 199 - 0 (start from beginning)
            print(0, " is seeked")
            drawY.append(0)
            drawX.append(x)
            x += 3
            i = 0
        elif i == 0:
            totalHeadMovement += requestArray[0]  # 14 - 0
            print(requestArray[0], " is seeked")
            drawY.append(requestArray[0])
            drawX.append(x)
            x += 3
            elementCounter += 1
            i += 1
        else:
            totalHeadMovement += abs(requestArray[i] - requestArray[i-1])
            print(requestArray[i], " is seeked")
            drawY.append(requestArray[i])
            drawX.append(x)
            x += 3
            elementCounter += 1
            i += 1
    print("Total Head Movement is ",totalHeadMovement)
    print("******************")
    plt.plot(drawX, drawY)
    plt.show()
    return 0

def CLOOK(Requestarray, initial):
    requestArray = copy.deepcopy(Requestarray)
    print("CLOOK Algorithm")
    drawX = []
    drawY = []
    x = 0
    totalHeadMovement = 0
    requestArray.append(initial)
    requestArray.sort()  # queue = 14,37,53,65,67,98,122,124,183
    i = requestArray.index(initial)
    elementCounter = 1

    while i < len(requestArray) - 1:
        totalHeadMovement += abs(requestArray[i + 1] - requestArray[i])
        print(requestArray[i+1], " is seeked")
        drawY.append(requestArray[i+1])
        drawX.append(x)
        x += 3
        elementCounter += 1
        i += 1

    while elementCounter < len(requestArray):
        if i == len(requestArray) - 1:
            totalHeadMovement += requestArray[i] - requestArray[0]
            print(requestArray[0], " is seeked")
            drawY.append(requestArray[0])
            drawX.append(x)
            x += 3
            i = 0
        elif i == 0:
            elementCounter += 1
            i += 1
        else:
            totalHeadMovement += abs(requestArray[i] - requestArray[i - 1])
            print(requestArray[i], " is seeked")
            drawY.append(requestArray[i])
            drawX.append(x)
            x += 3
            elementCounter += 1
            i += 1
    print("Total Head Movement is ",totalHeadMovement)
    print("*******************")
    plt.plot(drawX, drawY)
    plt.show()
    return 0



def improvedAlgo(Request, initialStart):
    request = copy.deepcopy(Request)
    print("Optimized Algorithm function")
    drawX = []
    drawY = []
    x = 0
    endOfDisk = 199
    totalHeadMovement = 0
    request.append(initialStart)
    request.sort()
    index = request.index(initialStart)
    i = index+1
    while i < len(request):
        totalHeadMovement += (request[i] - request[index])
        print(request[i], " is seeked")
        drawY.append(request[i])
        drawX.append(x)
        x += 3
        index = i
        i+=1
    print("Total Head Movement is ",totalHeadMovement)
    print("********************")
    plt.plot(drawX, drawY)
    plt.show()
    return 0



if __name__ == '__main__':
    print("The number of requests are: ")
    n = int(input())
    print("The initial head start cylinder is (total number of cylinders are 199: ")
    initialStart = int(input())
    request = []
    print("Enter the sectors of requests")
    for i in range(n):
        req = int(input())
        request.append(req)
    SSTFList = copy.deepcopy(request)
    SCANList = copy.deepcopy(request)
    LOOKList = copy.deepcopy(request)
    OptimizedList = copy.deepcopy(request)
    Cscan = copy.deepcopy(request)
    Clook = copy.deepcopy(request)
    fcfsButton = Button(tkWindow, text='FCFS', command=lambda : FCFS(request, initialStart))
    fcfsButton.pack()
    sstfButton = Button(tkWindow, text='SSTF', command=lambda : SSTF(SSTFList, initialStart))
    sstfButton.pack()
    lookButton = Button(tkWindow, text='LOOK', command=lambda : LOOK(LOOKList, initialStart))
    lookButton.pack()
    clookButton = Button(tkWindow, text='CLOOK', command=lambda : CLOOK(Clook, initialStart))
    clookButton.pack()
    scanButton = Button(tkWindow, text='SCAN', command=lambda : SCAN(SCANList, initialStart))
    scanButton.pack()
    CscanButton = Button(tkWindow, text='CSCAN', command=lambda : CSCAN(Cscan, initialStart))
    CscanButton.pack()
    optimizedButton = Button(tkWindow, text='Optimized', command=lambda : improvedAlgo(OptimizedList, initialStart))
    optimizedButton.pack()
    tkWindow.mainloop()

# 8
# 53
# 98
# 183
# 37
# 122
# 14
# 124
# 65
# 67