SuccList = {
    'S': [['A', 3], ['B', 6], ['C', 5]],
    'A': [['E', 8], ['D', 9]],
    'B': [['G', 14], ['F', 12]],
    'C': [['H', 7]],
    'H': [['J', 6], ['I', 5]],
    'I': [['M', 2], ['L', 10], ['K', 1]]
}
Start = input("Enter Source node >> ").upper()
Goal = input("Enter Goal node >> ").upper()

Closed = list()
SUCCESS = True
FAILURE = False
State = FAILURE


def GoalTest(N):
    if N == Goal:
        return True
    else:
        return False


def MovGen(N):
    New_list = list()
    if N in SuccList.keys():
        New_list = SuccList[N]
    return New_list


def Append(L1, L2):
    New_list = list(L1)+list(L2)
    return New_list


def Sort(L):
    L.sort(key=lambda x: x[1])
    return L


def BestFirstSearch():
    OPEN = [[Start, 5]]
    CLOSED = list()
    global State
    global Closed
    i = 1
    while len(OPEN) != 0 and (State != SUCCESS):
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<{}>>>>>>>>>>>>>>>>>>>".format(i))
        N = OPEN[0]
        print("N : ", N)
        del OPEN[0]
        if GoalTest(N[0]) == True:
            State = SUCCESS
            CLOSED = Append(CLOSED, [N])
            print("CLOSED : ", CLOSED)
        else:
            CLOSED = Append(CLOSED, [N])
            print("CLOSED : ", CLOSED)
            CHILD = MovGen(N[0])
            print("Child ", CHILD)

            for val in OPEN:
                if val in CLOSED:
                    CHILD.remove(val)
            for val in CLOSED:
                if val in CHILD:
                    CHILD.remove(val)
            OPEN = Append(CHILD, OPEN)
            print("Unsorted OPEN : ", OPEN)
            Sort(OPEN)
            print("Sorted OPEN : ", OPEN)
            Closed = CLOSED
            i += 1
    return State


result = BestFirstSearch()
print("Best First Search>>>>>>{}<<<<<{}>>>>>>>".format(Closed, result))
