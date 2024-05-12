#programme for nested if else:

# email = "rgagan@gmail.com"
# password = "1234"
email = input("email please : ")


if "@" in email:
    password = input("password also : ")
    if email == "rgagan@gmail.com" and password == "1234":
        print("Welcome")
    elif email == "rgagan@gmail.com" and password != "1234":
        print("password galat hai firse try karo : ")
        input(password)
else:
    print("email is wrong")