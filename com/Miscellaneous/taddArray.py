T = [[2, 3, 2], [0, 2, 5], [1, 0, 1]]
for r in T:
    for c in r:
        print(c,end = " ")
    print()

def solve(a): 
    x = [0]*len(a)
    t=0
    for k in range(len(a)):
        i = k;
        j = 0;
        while i >= 0:
            #print(a[i][j])
            x[t]+=a[i][j]
            i=i-1
            j=j+1
        t+=1
    t=len(a)-1
    for k in range(len(a)):
        #print(k)
        i = k;
        j = len(a)-1;
        while j >= 0 and i-1 >= 0:
            #print(a[i][j])
            x[t]+=a[i][j]
            i=i-1
            j=j-1
        t-=1
    relatedArray = []
    for index, value in enumerate(x):
        relatedArray.append((value, a[index][0]))

    relatedArray.sort()
    outputArray = []
    for a, b in relatedArray:
        outputArray.append(b)
    print(outputArray)

solve(T)
