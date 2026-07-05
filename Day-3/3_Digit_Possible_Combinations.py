#find three digit every possible combinations......
#Backtracking / permutation problem asked in microsoft/google interviews


digits=[1,2,3]
used=[False]*3

def Possible_Combinations(cur):

    if len(cur)==3:
        print(cur)
        return
    print("Curr : ",cur)

    for i in range(len(digits)):
        if not used[i]:
            used[i]=True
            Possible_Combinations(cur+str(digits[i]))
            used[i]=False      # Backtracking

#Dry run
Possible_Combinations("")