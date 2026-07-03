# Definition

# Merge Sort is a Divide and Conquer sorting algorithm. It divides the list into smaller 
# parts, sorts them, and then merges the sorted parts into one final sorted list. The merge 
# step combines two already sorted lists into a single sorted list by comparing their elements.

# In this Problem

# IRCTC has two separately sorted waitlists—one from the mobile app and another from railway counters.
#  Instead of sorting all passengers again, the system merges both sorted waitlists into one sorted list 
# by comparing the front elements of each list one by one. This is exactly the merge step of Merge Sort.


mwl=[1001,1002,1005,1008]
cwl=[1003,1004,1006,1007]
result=[]
i,j,k=0,0,0

#loop for add element with compare
while i<len(mwl) and j<len(cwl):
    if(mwl[i]<cwl[j]):
        result.append(mwl[i])
        i=i+1
    else:
        result.append(cwl[j])
        j=j+1
    k=k+1

#add remaining element 
while i<len(mwl):
    result.append(mwl[i])
    i=i+1
while j<len(cwl):
    result.append(cwl[i])
    j=j+1

print(result)