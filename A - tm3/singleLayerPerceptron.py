def OR():
    w1 = 0
    w2 = 0
    a = 0.5
    t = 0
    x = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [0, 1, 1, 1]
    while True:
        ActualOutput = []
        count = 0
        for i in x:
            print(
                "---------------------------------------------------------------------------------")
            print(i)
            print(w1, w2)
            print(
                "---------------------------------------------------------------------------------")
            step = w1*i[0]+w2*i[1]
            if step <= t:
                O = 0
                if O == y[count]:
                    ActualOutput.append(O)
                    count += 1
                else:
                    w1 = w1+a*(y[count]-O)*i[0]
                    w2 = w2+a*(y[count]-O)*i[1]
                    print(w1, w2)
            else:
                O = 1
                if O == y[count]:
                    ActualOutput.append(O)
                    count += 1
                else:
                    w1 = w1+a*(y[count]-O)*i[0]
                    w2 = w2+a*(y[count]-O)*i[1]
                    print(w1, w2)
        print("----->")

        if ActualOutput[0:] == y[0:]:
            print("Final Output of OR: \n")
            print("weights : w1={} and w2={}>>>>>>{}".format(w1, w2, ActualOutput))
            break


def And():
    w1 = 0
    w2 = 0
    a = 0.5
    t = 0.98
    x = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [0, 0, 0, 1]
    while True:
        ActualOutput = []
        count = 0
        for i in x:
            step = w1*i[0]+w2*i[1]
            if step <= t:
                O = 0
                if O == y[count]:
                    ActualOutput.append(O)
                    count += 1
                    print(w1, w2, ActualOutput)
                else:
                    w1 = w1+a*i[0]*(y[count]-O)
                    w2 = w2+a*i[0]*(y[count]-O)
                    print(w1, w2)
            else:
                O = 1
                if O == y[count]:
                    ActualOutput.append(O)
                    count += 1
                    print(w1, w2, ActualOutput)
                else:
                    w1 = w1+a*i[0]*(y[count]-O)
                    w2 = w2+a*i[0]*(y[count]-O)
                    print(w1, w2)
        print("----->")
        if ActualOutput[0:] == y[0:]:
            print("Final Output of And: \n")
            print("w1={} w2={}>>>>>>>>>>>{}".format(w1, w2, ActualOutput))
            break


def Not():
    x = [0, 1]
    y = [1, 0]
    weight = -1
    bias = 1
    ActualOutput = []
    for i in x:
        j = weight*i+bias
        ActualOutput.append(j)
    for i in x:
        print("NOT Gate {}--->{}".format(x[i], ActualOutput[i]))


Not()
