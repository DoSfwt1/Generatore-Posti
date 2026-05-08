import random


from RES.UTS import u,k,o


def SWP(LST, IN, OUT):
    idx1 = target_list.index(IN)
    idx2 = target_list.index(OUT)
    target_list[idx1], target_list[idx2] = target_list[idx2], target_list[idx1]
def WIN_XAAB(list):
    pd=list(o)
    for i in u:
        if list.index(i) in k:
            n = random.choice(pd)
            while(list[n] in u):
                n = random.choice(pd)
            SWP(list,i,list[n])
            pd.remove(n)
                
    
            
            
