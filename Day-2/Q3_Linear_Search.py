student=['Abhay','Mahesh','Smit','Ravi','Darshan','Riya']

#Linear search
flag=0

nm=input("Enter name you want to find : ")

for i in student:
    if i==nm:
        print(nm," is present in class...")
        flag=1
        break
    else:
        flag=0

if(flag==0):
    print(nm," is not present in class!")