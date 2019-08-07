def repeat(x):
    y=len(x)
    repeated=[]
    for i in range(y):
        k=i+1
        for j in range(k,y):
            if(x[i]==x[j] and x[i] not in repeated):
                repeated.append(x[i])
    return repeated
list=[1,2,3,2,3,4,3]
print(repeat(list))
