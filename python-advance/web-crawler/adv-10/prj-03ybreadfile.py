import pandas as pd
import matplotlib.pyplot as plt
def createLable(data):
    for item in data:
        height=item.get_height()
        plt.text(
            item.get_x()+item.get_width()/2,
            height,
            str(height),
            ha="center",
        )
df=pd.read_csv("adv-10/Youbike_Info.csv",encoding="utf8")
print(df)
Position=df.loc[:,"Position"]
Total=df.loc[:,"Total"]
Remain=df.loc[:,"Remain"]
A=plt.bar(Position[:8],Total[:8],label="全部停車格")
B=plt.bar(Position[:8],Remain[:8],label="剩下車輛")
createLable(A)
createLable(B)
plt.legend(loc=1)
plt.show()