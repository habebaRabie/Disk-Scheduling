def CSCAN(requestArray, initial):
    totalHeadMovement = 0
    requestArray.append(initial)
    requestArray.sort()  # queue = 14,37,53,65,67,98,122,124,183
    i = requestArray.index(initial)
    elementCounter = 1

    while i < len(requestArray) - 1:
        totalHeadMovement += abs(requestArray[i + 1] - requestArray[i])
        elementCounter += 1
        i += 1

    while elementCounter < len(requestArray):
        if i == len(requestArray) - 1:
            totalHeadMovement += 199 - requestArray[i]  # 199 - 183
            totalHeadMovement += 199  # 199 - 0 (start from beginning)
            i = 0
        elif i == 0:
            totalHeadMovement += requestArray[0]  # 14 - 0
            elementCounter += 1
            i += 1
        else:
            totalHeadMovement += abs(requestArray[i] - requestArray[i-1])
            elementCounter += 1
            i += 1

    return totalHeadMovement

def CLOOK(requestArray, initial):
    totalHeadMovement = 0
    requestArray.append(initial)
    requestArray.sort()  # queue = 14,37,53,65,67,98,122,124,183
    i = requestArray.index(initial)
    elementCounter = 1

    while i < len(requestArray) - 1:
        totalHeadMovement += abs(requestArray[i + 1] - requestArray[i])
        elementCounter += 1
        i += 1

    while elementCounter < len(requestArray):
        if i == len(requestArray) - 1:
            # totalHeadMovement += 199 - requestArray[i]  # 199 - 183
            # totalHeadMovement += 199  # 199 - 0 (start from beginning)
            totalHeadMovement += requestArray[i] - requestArray[0]
            i = 0
        elif i == 0:
            # totalHeadMovement += requestArray[0]  # 14 - 0
            elementCounter += 1
            i += 1
        else:
            totalHeadMovement += abs(requestArray[i] - requestArray[i - 1])
            elementCounter += 1
            i += 1

    return totalHeadMovement

if __name__ == '__main__':
    print("Number of requests: ")
    n = int(input())
    print("Initial head start cylinder (0-199): ")
    initial = int(input())
    print("Enter Request values (0-199): ")
    requestArray = []
    for req in range(n):
        request = int(input())
        requestArray.append(request)
    print("--------------------------------")
    print("Total Head Movement for C-SCAN: ", CSCAN(requestArray, initial))
    print("--------------------------------")
    print("Total Head Movement for C-LOOK: ", CLOOK(requestArray, initial))
    print("--------------------------------")