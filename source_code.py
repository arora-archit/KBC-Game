import os
import time
import csv
import random


def question(q_no):
    print(f"Question {ques_no}".center(size[0], "-"))
    time.sleep(1)
    used_ques= ques[q_no]
    print("\t\t",ques[q_no])
    count =0
    for L in opt:
        if count==q_no+1:
            print("\t\t\t1.",L[0],"\n\t\t\t2.",L[1],"\n\t\t\t3.",L[2],"\n\t\t\t4.",L[3])
            break
        count = count+1
    time.sleep(2)
    return used_ques
    

size = os.get_terminal_size()
def printlines():
    for i in range(size[0]):
        print("=",end="")

opt50_50 = []
with open(r"C:\Users\LAB\Desktop\cs project\5050Options.csv",'r') as cF:
    cR = csv.reader(cF)
    for L in cR:
        opt50_50.append(L)

def lifeline50_50(used_ques):
    count =0
    lifelines.remove(1)
    print(used_ques)
    for L in opt50_50:
        if count==q_no+1:
            print("\t\t\t1.",L[0],"\n\t\t\t2.",L[1],"\n\t\t\t3.",L[2],"\n\t\t\t4.",L[3])
            opt50_50.remove(L)
            time.sleep(2)
            break
        count = count+1


def double_dip():
    global c
    c = 0
    lifelines.remove(2)
    ans2= int(input("\nEnter first choice: "))
    if ans2 == answers[q_no]:
        print("Correct answer!".center(size[0]))
        c=1
    else:
        ans2=int(input("Enter second choice: "))
        if ans2 == answers[q_no]:
            print("Correct Answer!".center(size[0]))
            c=1
        else:
            print("Wrong Answer!".center(size[0]))
            time.sleep(2)
    answers.pop(q_no)
    ques.pop(q_no)
    opt50_50.pop(q_no+1)
    opt.pop(q_no+1)

def FlipTheQues():
    global d
    d = 0
    lifelines.remove(3)
    question(q_no)
    anss = int(input("Enter your choice: "))
    if anss == answers[q_no]:
        print("Correct Answer!".center(size[0]))
        d = 1
    else:
        print("Wrong Answer!".center(size[0]))
        time.sleep(2)
    answers.pop(q_no)
    opt.pop(q_no+1)
    ques.pop(q_no)
    opt50_50.pop(q_no+1)
answers = [2, 4, 2, 3, 3, 1, 1, 4, 2, 2, 2, 2, 2, 2, 1, 3, 4, 3, 3, 1, 2, 3, 1, 4, 4, 1, 4, 3, 3, 1, 3, 4, 3]

won = 0

amount_won = [1000, 2000, 3000, 5000, 10000,
			20000, 40000, 80000, 160000,
			320000, 640000, 1250000, 2500000,
			5000000, 10000000, 70000000,0]
#KBC Logo
printlines()
print(''' _   __                   ______                                _____                                _   _ 
| | / /                   | ___ \                              /  __ \                              | | (_)
| |/ /  __ _ _   _ _ __   | |_/ / __ _ _ __   ___  __ _  __ _  | /  \/_ __ ___  _ __ ___ _ __   __ _| |_ _ 
|    \ / _` | | | | '_ \  | ___ \/ _` | '_ \ / _ \/ _` |/ _` | | |   | '__/ _ \| '__/ _ \ '_ \ / _` | __| |
| |\  \ (_| | |_| | | | | | |_/ / (_| | | | |  __/ (_| | (_| | | \__/\ | | (_) | | |  __/ |_) | (_| | |_| |
\_| \_/\__,_|\__,_|_| |_| \____/ \__,_|_| |_|\___|\__, |\__,_|  \____/_|  \___/|_|  \___| .__/ \__,_|\__|_|
                                                   __/ |                                | |                
                                                  |___/                                 |_|                ''')
printlines()
#Welcome to game
print()

name =input("Enter Your Name- ".center(int(size[0])).rstrip())
print(f"Hey {name}! Welcome to KBC".center(int(size[0])))
printlines()
time.sleep(2)
lifelines= [1,2,3]
correct = True
ques_no = 1
with open(r"C:\Users\LAB\Desktop\cs project\Questions.txt","r") as obj:
     ques = obj.readlines()

opt = []
with open(r"C:\Users\LAB\Desktop\cs project\Options.csv",'r') as cF:
    cR = csv.reader(cF)
    for L in cR:
        opt.append(L)



while correct and ques_no <= 16:
    q_no = random.randint(0,len(ques)-1)
    try:
        a = question(q_no)
        ans = int(input("\t\tTo use a lifeline enter 9\n\t\tTo answer the questions enter correct option number\n\t\t\t"))
        if ans == answers[q_no]:
            print("Correct Answer!".center(size[0]))

            answers.pop(q_no) 
            opt50_50.pop(q_no+1)
            ques.pop(q_no)
            opt.pop(q_no+1)
            won = amount_won.pop(0)
        elif ans == 9:
            while len(lifelines) !=0:
                lifeline= int(input("Lifelines are\n1. Fifty Fifty\n2. Double Dip\n3. Flip the Question\n>>>"))
                if lifeline == 1 and 1 in lifelines:
                    lifeline50_50(a)
                    ans50 = int(input("\t\tEnter your choice: "))
                    if ans50 == answers[q_no]:
                        print("Correct Answer!".center(size[0]))
                        won = amount_won.pop(0)

                        opt.pop(q_no+1)
                        answers.pop(q_no)
                        ques.pop(q_no)
                        opt50_50.pop(q_no+1) 
                        break

                    else:
                        print("Wrong Answer!".center(size[0]))
                        correct = False
                        time.sleep(2)
                        answers.pop(q_no)
                        ques.pop(q_no)
                        opt50_50.pop(q_no+1)
                        opt.pop(q_no+1)
                        break
                    
                elif lifeline == 2 and 2 in lifelines:
                    double_dip()
                    if c == 1:
                        won = amount_won.pop(0)
                        break
                    else:
                        correct = False
                        break
                elif lifeline == 3 and 3 in lifelines:
                    answers.pop(q_no)
                    ques.pop(q_no)
                    opt50_50.pop(q_no+1)
                    opt.pop(q_no+1)
                    FlipTheQues()
                    if d == 1:
                        won = amount_won.pop(0)
                        break
                    else:
                        correct = False
                        break
                else:
                    print("INVALID!")
            
            else:
                print("You ran out of lifelines")
                question(q_no)
                ans = int(input("\t\tTo answer the questions enter correct option number\n\t\t\t"))
                if ans == answers[q_no]:
                    print("Correct Answer!".center(size[0]))
                    answers.pop(q_no)
                    ques.pop(q_no)
                    opt50_50.pop(q_no+1)
                    opt.pop(q_no+1)
                    won = amount_won.pop(0)
                else:
                    print("Wrong Answer!".center(size[0]))
                    break
    
        elif ans not in (1,2,3,4):
            print("Invalid option!".center(size[0]))
            break

        else:
            print("Wrong Answer!".center(size[0]))
            time.sleep(2)
            break
        ques_no+=1
      
    except ValueError:
        print("\tPlease enter valid integer values only!")
        break


winn = "You won ₹"+str(won)
print(winn.center(size[0]))
time.sleep(2)