import csv
a = []

with open("enjoySport.csv", 'r') as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)
print("The total number of training instances are: ", len(a))
num_attribute = len(a[0])-1
print("\n The initial hypothesis is : ")
hypothesis = ['0']*num_attribute

print(hypothesis)

for i in range(len(a)):
    if a[i][num_attribute] == 'yes':
        print("\nInstance ", i+1, " is ", a[i], " and is a positive instance")
        for j in range(num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
    else:
        print("\nInstance ", i+1, " is ",
              a[i], " and is a negative instance hence ignored")
    print("Hypothesis for the training instance ",
          i+1, " is : ", hypothesis, "\n")

print("Most specific hypothsis found by find S algorithm is : ", hypothesis, "\n")
