corrPass = "0,1"
corrUser = "hossan"

username= input("username: ")
passowrd= input("password: ")

if (username.lower() == corrUser):
    print ("correct user: " + corrUser)
    if (passowrd == corrPass):
        print ("correct password: " + corrPass)
    else: 
        print("wrong password: " + passowrd)
       
else: 
    print("wrong username: " + username)

