# mylist = ["apple","Cherry",24,10,"Banana","Grapes"]


mylist = list(("Apple","Cherry","Banana","Watermelon","Blackcherry"))
# print(type(mylist))
# print(mylist[1])

tropical_fruit = ["Mango","Jamun"]


'''X = str(input("Enter fruit : ").capitalize())

if X in mylist:
    print("Yes "+ X.upper() +" is in list")'''

mylist.append("Grapes")
# print(mylist)

'''mylist.extend(tropical_fruit)
print(mylist)'''




# mylist[1:3]=["Blackcurrant","Watermelon"]
# print(mylist)




mylist.insert(1,"Mango")
print(mylist)

del mylist[1]
print(mylist)