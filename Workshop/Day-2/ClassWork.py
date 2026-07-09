#Sorting.....
#Bubble sort

n=5
arr=[213,23,12,45,345]

for i in range(0,5):
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)

#Selection sort

n=5
arr=[213,23,12,45,345]

print("Original: ",arr)

for i in range(0,5):
    min1=i
    for j in range(i+1,n):
        if arr[j] < arr[min1]:
            min1=j

    arr[i],arr[min1]=arr[min1],arr[i]

print(arr)