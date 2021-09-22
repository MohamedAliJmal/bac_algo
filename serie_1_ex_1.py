import random 
def saisi():
    bl=True
    while bl==True:
        n=int(input("donner n entre 3 et 20 "))
        if 3<=n<=20:
            bl=False
    return n
def remplir(n):
    
    def verif(ch):
        bol=True
        i=0
        while bol==True:
            test=ch[i].isupper()
            if test==False or i == len(ch)-1:
                bol=False
            i=i+1    
        return test           
    t=[str(x) for x in range(n)]
    
    for i in range(len(t)):
        bl=True
        while bl==True:
            t[i]= input(f"donner t[{i}] longueur de 10 char et majuscule " )
            print(t)
            if len(t[i])==10 and verif(t[i])==True:
                bl=False
                
    return t            
def former(t,n):
    p=random.randint(0,9)
    x=""
    for i in range(n):
        x=x+t[i][p]
    return x
def affichage(ch):
    result=[]
    for i in range(n):
        
        print(n)
        print(ch)
        r=""
        for j in range((len(ch)//2)):
            print(f"len {len(ch)//2}")
            r=r+ch[len(ch)-j-1]+ch[j]    
            if len(ch)%2==1:
                r=r+ch[len(ch)//2]
        ch=r
        result.append(r)
        if i == n-1:
            print(result)                
        
n=saisi()
t=remplir(n)
fm=former(t,n)
affichage(fm)
