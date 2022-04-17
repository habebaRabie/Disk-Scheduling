def FCFS(request, initialStart):
    totalHeadMovement = 0
    currentPosition = initialStart
    for req in request:
        totalHeadMovement += abs(req - currentPosition)
        currentPosition = req
        print(currentPosition, " is seeked")

    return totalHeadMovement


def SSTF(request, initialStart):
    totalHeadMovement = 0
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
        else:
            i += 1
            totalHeadMovement += request[j] - request[index]
            index = j
            print(request[index], " is seeked")

        j += 1
        i -= 1

    return totalHeadMovement


if __name__ == '__main__':
    print("The number of requests are: ")
    n = int(input())
    print("The initial head start cylinder is (total number of cylinders are 200): ")
    initialStart = int(input())
    request = []
    print("Enter the sectors of requests")
    for i in range(n):
        req = int(input())
        request.append(req)

    print("Total Head Movement is ", FCFS(request, initialStart), " cylinders")
    print("----------------------------------------")
    print("Total Head Movement is ", SSTF(request, initialStart), " cylinders")

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
