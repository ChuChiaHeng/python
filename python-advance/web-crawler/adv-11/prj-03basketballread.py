import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def createLable(data):
    for item in data:
        height=item.get_height()
        plt.text(
            item.get_x()+item.get_width()/2,
            height,
            str(height),
            ha="center",
        )
df=pd.read_csv("adv-11/basketball.csv",encoding="utf8")
print(df)
game_date=df.loc[:,"date"]
home_win_list=df.loc[:,"home_win"]
cust_win_list=df.loc[:,"cu_win"]
index = np.arange(len(game_date))
fig, ax = plt.subplots()
A = ax.bar(index, home_win_list, label="主場勝",  width=0.25)
B = ax.bar(index +0.25, cust_win_list, label="客場勝",  width=0.25)
ax.set_xticks(index)
ax.set_xticklabels(game_date)
createLable(A)
createLable(B)
plt.legend(loc=1)
plt.show()