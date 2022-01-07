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
elif age<130:
    print("you are old")
else:
    print("im sorry but its impossible for you to still live")

if team == "GS":
    print('his team is very good stay with this team')
elif team == "FB":
    print('you made a big mistake keeping this team in my opinion')
elif team == "BJK":
    print('what are you waiting for to get out of that exact person?')
elif team == "TS":
    print('I hope you dont know anything about TS otherwise you wouldnt have hired that team!')
else:
    print("no problem you can stay on that team")