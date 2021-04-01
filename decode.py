import base64,sys
def solver(x):
    def decode_key(key):
        dkey=""
        for i in key:
            if i=="a":
                dkey+="+"
            elif i=="b":
                dkey+="-"
            elif i=="c":
                dkey+="/"
            elif i=="d":
                dkey+="*"
            else:
                dkey+=i
        return dkey
    x=decode_key(x)
    solve=0
    A=[]
    p=False
    k=0
    for i in range(len(x)):
        if x[i]=="+" or x[i]=="-" or x[i]=="/" or x[i]=="*":
            if p==False:
                k=i
                A+=[x[:i]]
                p=True
            else:
                A+=[x[k:i]]
                k=i
    A+=[x[k:]]
    for j in A:
        if j[0]=="+":
            solve+=int(j[1:])
        elif j[0]=="-":
            solve-=int(j[1:])
        elif j[0]=="/":
            solve/=int(j[1:])
        elif j[0]=="*":
            solve*=int(j[1:])
        else:
            solve=int(j)
    solve=int(solve)
    return solve
file=open(input("Input File Name:"),"r")
num=file.readlines()
num=str(int(num[0],2))
key=input("your key:")
key=str(base64.b64decode(key.encode()).decode())
solve=solver(key)
solve%=95
solve*=-1
_str=""
j=0
run=True
while j<len(num) and run:
    A=num[j]+num[j+1]
    if int(A)<32:
        A=num[j]+num[j+1]+num[j+2]
        if int(A)>126:
            print("Error!")
            run=False
        else:
            _str+=chr(int(A))
            j+=3
    else:
        _str+=chr(int(A))
        j+=2
unum=""
li=1
percent=0
for i in _str:
    h=ord(i)+solve
    if h<32:
        c=126-(32-h-1)
    elif h>126:
        c=(h-126-1)+32
    else:
        c=h
    unum+=chr(c)
    if int((li*100)/len(_str))!=percent:
        percent=int((li*100)/len(_str))
        progres="["+((percent//5)*"#")+((20-(percent//5))*" ")+"] "+str(percent)+"%"
        sys.stdout.write(len(progres)*"\b")
        sys.stdout.flush()
        sys.stdout.write(progres)
    li+=1
print("\nDONE!")
unum=unum.split("$%^")
out=open(input("Output File Name:"),"w")
for k in unum:
    out.write(k+"\n")
out.close()
