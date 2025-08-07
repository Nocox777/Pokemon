import random 
import math




base_c=[39,52,43,60,50,65]
stats2=[]

stats1="HP: ","ATK: ","DEF: ", "ATK.ESP: ", "DEF.ESP: ","VEL: " 
textos = [
    "HP: 20",
    "Ataque: 15",
    "Defensa: 10",
    "Velocidad: 12",
    "Especial: 18"
]

def aleatorio_ivs():
    ivs=random.randint(1,31)
    return ivs

def calculo_stat(base):
    for i in range(len(base)):
        iv=aleatorio_ivs()
        dato=((2*base[i]+iv)/100*5)+5
        if i==0: 
            dato+=10
        stats2.append(int(dato))
        
        

calculo_stat(base_c) 
        
        
    


    
print(stats2)
