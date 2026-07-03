# Definition

# Linear Search is the simplest searching technique in which elements are 
# checked one by one from the beginning until the required element is found 
# or the list ends. It is used when the data is not sorted.

# In this Problem

# A spam filter checks each incoming email sender ID against a blacklist of spam senders. 
# Since the blacklist is not arranged in any order, the system compares the sender ID with each 
# entry one by one until a match is found. Therefore, Linear Search is the most suitable searching technique.

blacklist = ["scam99@gmail.com",
            "skim33@gmail.com",
            "abc@yahoo.com",
            "duplicate@gmail.com",
            "win@lottery.com"]

#method for spam detecter
def spam_det(email):
    for i in blacklist:
        if i==email:
            print(email, "is a Spam Sender.")
            return
    print(email, "is Not a Spam Sender.")

#Dry Run
spam_det("win@lottery.com")