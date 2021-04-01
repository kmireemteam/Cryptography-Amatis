import base64,random,os,sys
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
def key_gen():
    def encode_key(key):
        ekey=""
        for i in key:
            if i=="+":
                ekey+="a"
            elif i=="-":
                ekey+="b"
            elif i=="/":
                ekey+="c"
            elif i=="*":
                ekey+="d"
            else:
                ekey+=i
        return ekey
    key=""
    A=["+","-","*","/"]
    for i in range(random.randint(2,6)):
        key+=str(random.randint(1,99))+A[random.randint(0,3)]
    key+=str(random.randint(1,99))
    key=encode_key(key)
    return key
def list_to_str(_list):
    _str=""
    for i in _list:
        if i[len(i)-1]=="\n":
            _str+=i[:len(i)-1]+"$%^"
        else:
            _str+=i
    return _str
def str_to_num(_str):
    key1=True
    while key1:
        t=1
        key=key_gen()
        solve=solver(key)
        if solve<0:
            solve=solve*-1
            t=0
        if solve%95!=0:
            cr=solve%95
            key1=False
    if t==0:
        cr=cr*-1
    num=""
    li=1
    percent=0
    for i in _str:
        h=ord(i)+cr
        if h<32:
            c=126-(32-h-1)
        elif h>126:
            c=(h-126-1)+32
        else:
            c=h
        num+=str(ord(chr(c)))
        if int((li*100)/len(_str))!=percent:
            percent=int((li*100)/len(_str))
            progres="["+((percent//5)*"#")+((20-(percent//5))*" ")+"] "+str(percent)+"%"
            sys.stdout.write(len(progres)*"\b")
            sys.stdout.flush()
            sys.stdout.write(progres)
        li+=1
    print("\nDONE!")
    key=base64.b64encode(bytes(key,"utf-8"))
    return num,key
def num_to_bin(num):
    _bin=""
    num=int(num)
    k=num
    while num//2!=0:
        _bin+=str(num%2)
        num//=2
    _bin+="1"
    _bin1=_bin
    _bin=""
    for i in range(len(_bin1)-1,-1,-1):
        _bin+=_bin1[i]
    return _bin
File_name=input("Input File name:")
output_File_name=input("Output File Name:")
file=open(File_name,"r")
_str=list_to_str(file.readlines())
num=str_to_num(_str)
_bin=str(bin(int(num[0])))
print("Your key=",num[1].decode())
file=open(output_File_name,"w")
file.write(_bin)
file.close()
if File_name!="key.txt" and output_File_name!="key.txt" and os.path.exists("key.txt")==False:
    file=open("key.txt","w")
    key_code=str(num[1].decode())
    file.write(key_code)
    file.close()
else:
    keyn=""
    Key_name=input("Please enter a name for save key:")
    file=open(Key_name,"w")
    key_code=str(num[1].decode())
    file.write(key_code)
    file.close()
