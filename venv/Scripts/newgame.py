name = input("enter your name please:")
age = int(input("enter your age please:"))
team = input("enter your team please:")
length_name = len(name)
if length_name<5:
    print("hello",name,"you have a short name")
elif length_name<8:
    print("hello",name,"you have a normal length name")
else:
    print("hello",name,"you have a very long name")
if age<3:
    print("you are a baby")
elif age<12:
    print("you are a child")
elif age<18:
    print("you are teenage")
elif age<70:
    print("you are adult")
elif age<120:
    print("you are old")
else:
    print("im sorry but its impossible for you to still live")











