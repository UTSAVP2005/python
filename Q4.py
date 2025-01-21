#REMOVE ONE STRING
main_str=input("enter string")
sub_str=input("enter string to REMOVE")

if sub_str in main_str:
    result=main_str.replace(sub_str,"")
    print(f"new string:{result}")

else:print("no substring found")    
