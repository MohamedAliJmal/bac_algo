#Jmal Mohamed Ali
def saisie():
    def verif(x):
        b=True
        if x[0]==" " or x[-1]==" ":
                b=False
        i=0        
        while b and i<len(x):   
            if x[i].isspace() and x[i+1].isspace(): 
                   b=False
            elif x[i].isdecimal():
                b=False       
            i+=1   
        return b              

                
    bl=True
    while bl:
        ph=input("donner la phrase ")
        if verif(ph)==True:
            # print("ok")
            bl=False
    return ph        

def crypter(ph):
    t=ph.split(" ")
    for i in range(len(t)):
        aux=""
        for j in range(len(t[i])):
            if t[i][j]=="Z":
                aux+="A"
            elif t[i][j]=="z":
                aux+="a"
            else:        
                aux+=chr((ord(t[i][j])+i+1))
        t[i]=aux
        
    ph=" ".join(t)
    return ph        

def afficher(ph):
    print(ph)


ph=saisie()
ph=crypter(ph)
afficher(ph)
