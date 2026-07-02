dic=['Adarsh Bharat','Ephemeral','Ikrigay','Krishnashtakam','Yuvan',]

#Binary Search

nm=input("Enter Book name you want to search : ")
n=len(nm)

start=0
end=len(dic)-1

while start<=end:
    print(start,end)
    mid=int((start+end)//2)
    print(dic[mid],"->",nm)
    
    if dic[mid]==nm:
        print(nm," Word found..")
        break

    if ord(dic[mid][0]) < ord(nm[0]):
        start=mid+1

    if ord(dic[mid][0]) > ord(nm[0]):
        end=mid-1
        

if start>end:
    print(nm," Word not found")