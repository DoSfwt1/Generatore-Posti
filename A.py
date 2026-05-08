import random


from RES.UTS import u,k,o


def SWP(LST, IN, OUT):
    idx1 = LST.index(IN)
    idx2 = LST.index(OUT)
    LST[idx1], LST[idx2] = LST[idx2], LST[idx1]
def WIN_XAAB(List):
    pd=list(o)
    for i in u:
        if List.index(i) in k:
            n = random.choice(pd)
            while(List[n] in u):
                n = random.choice(pd)
            SWP(List,i,List[n])
            pd.remove(n)
                
    
            
            
