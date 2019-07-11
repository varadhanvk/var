# Python Program to check character is Alphabet or No
ch = input("Please Enter Your Own Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("The Given Character ", ch, "Alphabet") 
else 
    print("The Given Character ", ch, "No")
