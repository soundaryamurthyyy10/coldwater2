import random
count=0
while(count<=100):
    n=input("press r to roll a dice")
    if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("ur random is",r)
        print("ur count is",count)
        if(count>100):
            print("Try again")
            count=count-r
        elif(count==100):
            print("You Win")
    if(count==8):
        count=37
        print("climb the ladder",count)
    elif(count==13):
        count=34
        print("climb the ladder",count)
    elif(count==40):
        count=68
        print("climb the ladder",count)
    elif(count==52):
        count=81
        print("climb the ladder",count)
    elif(count==52):
        count=81
        print("climb the ladder",count)
    elif(count==76):
        count=87
        print("climb the ladder",count)
    elif(count==11):
        count=2
        print("aah snake bite",count)
    elif(count==25):
        count=4
        print("aah snake bite",count)
    elif(count==38):
        count=9
        print("aah snake bite",count)
    elif(count==65):
        count=46
        print("aah snake bite",count)
    elif(count==89):
        count=70
        print("aah snake bite",count)
    elif(count==93):
        count=64
        print("aah snake bite",count)
    elif(count==93):
        count=64
        print("aah snake bite",count)
    
    
    
    
