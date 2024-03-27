import random as rd
import pickle as pk

def pass_gen():
    source=input("Enter the Website/app name : ")
    
    l_c="abcdefghijklmnopqrstuvwxyz"
    u_c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s="@#$%&*()~`+?/\\{}[]:;<>,.|"
    d="1234567890"

    qu=int(input("How many uppercase letter password must contain??? \n"))
    ql=int(input("How many lowercase letter password must contain??? \n"))
    qs=int(input("How many special case letter password must contain??? \n"))
    qd=int(input("How many numbers password must contain??? \n"))

    p=[]

    for i in range (qu) :
        p.append(u_c[rd.randint(0,25)])

    for j in range (ql) :
        p.append(l_c[rd.randint(0,25)])

    for k in range (qs) :
        p.append(s[rd.randint(0,25)])

    for l in range (qd) :
        p.append(d[rd.randint(0,9)])

    res = source+": "
    
    for z in p :
        z= str(z)
        res = res + z


    return res

sav = pass_gen()
def save_pass(save):
    f=open("passwd.txt","a+")
    f.write(sav+"\n")
    f.close()
    return
print(sav)
save_pass(sav)
