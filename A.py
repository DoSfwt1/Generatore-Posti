import random


from RES.UTS import u,k,o


def SWP(LST, IN, OUT):
    idx1 = target_list.index(IN)
    idx2 = target_list.index(OUT)
    target_list[idx1], target_list[idx2] = target_list[idx2], target_list[idx1]
def WIN_XAAB(List):
    pd=list(o)
    for i in u:
        if List.index(i) in k:
            n = random.choice(pd)
            while(List[n] in u):
                n = random.choice(pd)
            SWP(list,i,List[n])
            pd.remove(n)
                
    
            
            
