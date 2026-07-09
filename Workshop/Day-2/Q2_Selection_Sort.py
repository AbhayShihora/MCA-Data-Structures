n=5
marks=[45,65,44,57,89]

print("Marks are :",marks)

for i in range(0,5):
    max1=i
    for j in range(i+1,n):
        if marks[j] > marks[max1]:
            max1=j

    marks[i],marks[max1]=marks[max1],marks[i]

print("Marks in sorted order are : ",marks)