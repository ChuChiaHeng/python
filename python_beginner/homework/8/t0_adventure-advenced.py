import random
import time
magic=2
life=300
money=0
up_attack=0
Defense=0
nirvana=0
def close_game(sts):
    path='output.txt'
    f=open(path,'w')
    for i in range(len(sts)):
        f.write(str(sts[i])+"\n")
    f.close()
def read_file():
    path='output.txt'
    f=open(path,'r')
    text=[]
    for line in f:
        text.append(int(line))
    print(text)
    f.close()
    return text
def update_money(money):
    get_money=random.randint(10000,100000)
    new_money=money+get_money
    print('your get Money=%d Your money%d'%(get_money,new_money))
    return new_money
def update_life(life):
    get_life=random.randint(100,355)
    new_life=life+get_life
    print('your recovery Life=%d Your life%d'%(get_life,new_life))
    return new_life
def update_magic(magic):
    get_magic=random.randint(2,5)
    new_magic=magic+get_magic
    print('your recovery magic=%d Your magic%d'%(get_magic,new_magic))
    return new_magic
def store(life,money,magic,attack,Defense,nirvana):
    status=[0,0,0,0,0,0,0]
    up_life=life
    up_money=money
    up_magic=magic
    up_attack = attack
    up_Defense=Defense
    up_nirvana=nirvana
    while True:
        if (money<10000):
            print("錢不夠")
        else:
            qu=input("Do you want 'rl' life potion 'rm' magic potion 'we' weapon 'de' defense 'ni' nirvana 'q' quit")
            up_money-=10000
            if qu=="q":
                print('88')
                break
            elif qu=="de":
                up_Defense+=random.randint(100,500)
                print("money=%d"%up_money)
                print("up Defense=%d new Defense=%d"%(Defense,up_Defense))
            elif qu=="we":
                up_attack+=random.randint(100,500)
                print("money=%d"%up_money)
                print("up attack=%d new attack=%d"%(attack,up_attack))
            elif qu=="rl":
                up_life+=random.randint(100,1000)
                print("money=%d"%up_money)
                print("life=%d"%up_life)
            elif qu=="rm":
                up_magic+=random.randint(2,5)
                print("money=%d"%up_money)
                print("magic=%d"%up_magic)
            elif qu=="ni":
                up_nirvana+=1
                print("money=%d"%up_money)
                print("nirvana=%d"%up_nirvana)
            else:
                continue
        status[1]=up_life
        status[2]=up_money
        status[3]=up_magic
        status[4]=up_attack
        status[5]=up_Defense
        status[6]=up_nirvana
        return status
def fighting(life,money,magic,attack,Defense,nirvana):
    status=[0,0,0,0,0,0,0]
    up_life=life
    up_money=money
    up_magic=magic
    up_attack = attack
    up_Defense=Defense
    up_nirvana=nirvana
    monster_life=random.randint(200,5000)
    print("Monster Life=%d"%monster_life)
    while True:
        aa=input("Do you want 'ma' 魔法攻擊 'a' 普通攻擊 'nn' 必殺卷軸")
        if aa=="nn":
            if up_nirvana<1:
                print("沒有必殺卷軸")
                continue
            elif up_nirvana>=1:
                up_nirvana-=1
                print("You beast monster")
                up_money+=random.randint(1000,10000)
                status[0]=1
                status[1]=up_life
                status[2]=up_money
                status[3]=up_magic
                status[4]=up_attack
                status[5]=up_Defense
                status[6]=up_nirvana
            return status
        if aa=="a":
            attack=random.randint(100,1000)+up_attack
            print("You make damage%d"%attack)
            monster_life-=attack
            time.sleep(1)
            print("Monster Life%d"%monster_life)
            up_attack=0
        elif aa=="ma":
            if (magic<2):
                print("魔力點數不夠")
                continue
            else:
                magic_attack=random.randint(1000,2000)
                print("You make damage%d"%magic_attack)
                monster_life-=magic_attack
                magic-=2
                time.sleep(1)
                print("Monster Life%d"%monster_life)
        else:
            continue
        if(monster_life<1):
            print("You beast monster")
            up_money+=random.randint(1000,10000)
            status[0]=1
            status[1]=up_life
            status[2]=up_money
            status[3]=up_magic
            status[4]=up_attack
            status[5]=up_Defense
            status[6]=up_nirvana
            return status
        print("Monster Attack")
        time.sleep(1)
        monster_attack=random.randint(100,300)
        if up_Defense>0:
            if up_Defense>monster_attack:
                up_Defense-=monster_attack
                print("Defense steal have%d"%up_Defense)
            elif up_Defense<monster_attack:
                monster_attack-=up_Defense
                up_Defense=0
                print("Your defenses are exhausted")
                up_life-=monster_attack
                print("You get hurt, Life=%d" % up_life)
        elif attack<=0:
            up_life-=monster_attack
            print("You get hurt, Life=%d" % up_life)
        if ( up_life <=1):
            print("You dead \n")
            status[0] = 0
            status[1] = up_life
            status[2] = up_money
            status[3] = magic
            status[4]=up_attack
            status[5]=up_Defense
            status[6]=up_nirvana
            return status
sts=read_file()
while True:
    rev=input("Do you want 'c' continue 'q' quit the game 's' go to the store")
    if (rev=="c"):
        gen_event=random.randint(1,4)
        if (gen_event==1):
            sts[1]=update_life(sts[1])
        if (gen_event==2):
            sts[2]=update_money(sts[2])
        if (gen_event==3):
            sts=fighting(sts[1],sts[2],sts[3],sts[4],sts[5],sts[6])
            if(sts[0]==0):
                print("Game Over")
                break
            print("sts=%s"%sts)
    elif(rev=="q"):
        print("88")
        close_game(sts)
        print(sts)
        break
    elif(rev=="s"):
        sts=store(sts[1],sts[2],sts[3],sts[4],sts[5],sts[6])
    else:
        continue