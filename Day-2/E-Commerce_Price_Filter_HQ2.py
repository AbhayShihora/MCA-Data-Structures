# Definition

# Binary Search is an efficient searching technique that works only on sorted data. 
# It repeatedly divides the search space into two halves until the required element is found. 
# The Lower Bound variation finds the first element that is greater than or equal 
# to the target value (≥ target).

# In this Problem

# The products on Flipkart are sorted by price. When the user searches for products priced 
# ₹50,000 or above, the system finds the first product whose price is greater than or equal to ₹50,000
#  using the Lower Bound Binary Search. This makes the search much faster than checking every product.





#Binary Search
prices = [15000, 25000, 32000, 45000, 50000, 50000, 62000, 75000]

target=int(input("Enter target price : "))
n=len(str(target))

start=0
end=len(prices)-1
ans=-1

while start<=end:
    mid=int((start+end)//2)
    
    if prices[mid]>=target:
        end=mid-1
        ans=mid
        break
    else:
        start=mid+1

if ans!=-1:
    print("First Product :", prices[ans])
    print("Index:", ans)
else:
    print("Product Not Found")