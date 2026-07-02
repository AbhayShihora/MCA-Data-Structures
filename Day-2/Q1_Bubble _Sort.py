n=5
arr=[213,23,12,45,345]

for i in range(0,5):
    for j in range(0,n-i-1):
        if(arr[j]<arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)