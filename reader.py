import time 
def read_pass():
    f=open("passwd.txt","r")
    return f.read()

print(read_pass())

time.sleep(200)


