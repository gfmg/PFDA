import random as rd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

battles = range(0,1000)
#len(battles)

#To store results
resf= np.zeros((len(battles),2))

for b in battles:
    # Random numbers...Sorted from high to low
    attackers = sorted(rd.sample(range(1,6), 3),reverse=True)
    defenders = sorted(rd.sample(range(1,6), 2),reverse=True)

    #One battle (dice comparison) per row
    res=np.array([[0,0],
                  [0,0]])
    
    # Attackers victories first column defender second column
    if attackers[0] > defenders[0]:
        res[0,0] = 1
    else:
        res[0,1] = 1

    if attackers[1] > defenders[1]:
        res[1,0] = 1
    else:
        res[1,1] = 1

    # Aggregate results   
    resf[b,]=sum(res)
    
print(resf)

df=pd.DataFrame({"Results":sum(resf),
             "Players": ["Attackers","Defenders"]})	

# Making a piechart
fig, ax = plt.subplots(figsize=(4,4)) 

ax.pie(df['Results'],labels=df['Players'], autopct='%1.2f%%', startangle=90,shadow=True,textprops={'fontsize': 14})
plt.title("Risk Battle Winning Percentages", fontweight="bold",fontdict={'fontsize': 20})
plt.show()
# %%
