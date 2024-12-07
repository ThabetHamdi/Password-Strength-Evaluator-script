# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:20:20 2024

@author: ThabetHamdi
"""
import string as s

def countUppercase(password):
    count=0
    up= s.ascii_uppercase
    
    for char in password:
        if char in up:
            count+=1
    return count

"""password="PassWOrd"
x=countUppercase(password)
print(x)"""

######################################

def countLowercase(password):
    count=0
    low=s.ascii_lowercase
    
    for char in password:
        if char in low:
            count+=1
    return count


"""x=countLowercase(password)
print(x)"""
#########################################
def specialCharCount(password):
    count=0
    for char in password:
       if char not in s.ascii_letters:
           count+=1
    return count
    
    
    
    #testspecialcarcount
"""password="##!ah!'(]~~~~é"
x=specialCharCount(password)
print(x)"""
    
    ###########lengthofUppercaselettersseq#####

def Upseq(password):
    length = len(password)
    l = []
    
    for k in range(length - 1):
        if password[k].isupper() and password[k + 1].isupper():
            l.append(password[k])

    count = 0
    currentseq = 1

    for i in range(1, length):
        if password[i].isupper() and password[i - 1].isupper():
            currentseq += 1
        else:
            if currentseq > count:
                count = currentseq
            currentseq = 1

    if currentseq > count:
        count = currentseq

    return count
    
####test#####
"""password="PPPPaaaaMMoooAAAAAAAALLLLLLLL MMMMMM"
x=Upseq(password)
print(x)"""
    
    
    
    
    ###############################
def lowseq(password):
    length = len(password)
    l = []
    
    for k in range(length - 1):
        if password[k].islower() and password[k + 1].islower():
            l.append(password[k])

    count = 0
    currentseq = 1

    for i in range(1, length):
        if password[i].islower() and password[i - 1].islower():
            currentseq += 1
        else:
            if currentseq > count:
                count = currentseq
            currentseq = 1

    if currentseq > count:
        count = currentseq

    return count


    
####test#####
"""
password="PPPPaaaaMMoooAAAAAAAALLLLLLLL MMMMMM"
x=lowseq(password)
print(x)
"""

#############scorefunction#########
def Score(password):
    nbofupletter = countUppercase(password)
    nboflowletter = countLowercase(password)
    nbspecialchar = specialCharCount(password)
    sequp = Upseq(password)
    seqlow = lowseq(password)
    totalnb = len(password)
    penaltyup = sequp * 3
    penaltylow = seqlow * 2
    formula = totalnb * 4 + (totalnb - nbofupletter) * 2 + (totalnb - nboflowletter) * 4 + nbspecialchar * 5
    if seqlow > 2 and sequp < 3:
        formula -= penaltylow
    elif sequp > 3 and seqlow < 2:
        formula -= penaltyup
    elif sequp > 3 and seqlow > 2:
        formula -= (penaltylow + penaltyup)
        
 
    return formula


###test####
"""
password = "_"
x = Score(password)
print(x)
     
"""







def passwordstrength(password): ##main function 
   
    try :
        if  password =='':
              raise ValueError("empty password not accepted")
            
        x=Score(password)
    
        if x < 20:
           return "very weak password "
        elif x < 40:
           return "weak password"        
        elif x < 80:
           return "strong password"
        else:
           return "very strong password"
       
    except ValueError as e :
            return str(e)
    
    

"""password=''
x=passwordstrength(password)
print(x)"""



def main():
    import time
    while True:
        print("Welcome to Password Evaluator")
        print("************ Menu ************")
        print("1 - Enter password")
        print("2 - Type 'exit' to quit")
        choice = input("Please enter your choice: ")
        if choice == "1":
            password = input("Enter your password: ")
            print(passwordstrength(password)) 
            time.sleep(2)
        elif choice.lower() == "2" or choice.lower() == "exit":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()

    
    
