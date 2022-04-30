sts=[0,10,10,1000,0,0]
def close_game():
    path='output.txt'
    f=open(path,'w')
    for i in range(len(sts)):
        f.write(str(sts[sts])+"\n")
    f.close()
def read_file():
    f=open(path,'r')
    text=[]
    for line in f:
        text.append(int(line))
    print(text)
    f.close()
    return text
sts=read_file