import random 
import math




base_c=[39,52,43,60,50,65]
base_b=[45, 49, 49, 65, 65, 45]
base_s=[44, 48, 65, 50, 64, 43]
stats1=[]
stats2=[]
stats3=[]
stats="HP: ","ATK: ","DEF: ", "ATK.ESP: ", "DEF.ESP: ","VEL: " 

def aleatorio_ivs():
    ivs=random.randint(1,31)
    return ivs

def calculo_stat(base,lista):
    for i in range(len(base)):
        iv=aleatorio_ivs()
        dato=((2*base[i]+iv)/100*5)+5
        if i==0: 
            dato+=10
        lista.append(int(dato))
        
 
    

calculo_stat(base_c,stats1) 
calculo_stat(base_s,stats2)
calculo_stat(base_b,stats3)

        
        
    


    
