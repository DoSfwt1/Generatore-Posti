import random


from RES.UTS import u,k,o


def SWP(LST, IN, OUT):
    idx1 = LST.index(IN)
    idx2 = LST.index(OUT)
    LST[idx1], LST[idx2] = LST[idx2], LST[idx1]
def len(List):
    pd=list(o)
    for i in u:
        if List.index(i) in k:
            n = random.choice(pd)
            while(List[n] in u):
                n = random.choice(pd)
            SWP(List,i,List[n])
            pd.remove(n)
            
    temp6=List[6]
    temp7=List[7]
    sig=List.index("Signo")
    zan=List.index("Zanoli")
    List[6]="Signo"
    List[7]="Zanoli"
    List[sig]=temp6
    List[zan]=temp7
    
    return 23
                
    
            
            
