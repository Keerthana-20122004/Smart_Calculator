import random
option=["rock","paper","scissors"]
nenu=input("enter your choice")
system=random.choice(option)
print("My choice:",nenu)
print("system choice:",system)
if nenu==system:
    print("tie")
elif nenu=="paper" and system=="rock":
    print("I am the winner")
elif nenu=="rock" and system=="scissors":
    print("I am the winner")
elif nenu=="scissors" and system=="paper":
    print("I am the winner")
else:
    print("system won")