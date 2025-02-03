import sys
from instabot import Bot
flute=Bot()

def inchoose():
    print("choose the number\n"  \
           "2.follow\n"  \
           "3.upload photo\n" \
           "4.unfolow\n"  \
           "5.messagrmultiple person\n"  \
           "6.fololower\n"  \
           "7.following"
          )
print("*****************************")
print("==========INSTA ACE==========")
print("*****************************")
print("\t \t by -Abhishek\n")
print("choose the number \n" \
      "1.Login \n"  \
      "8.exit"
      )
select=int(input("choose the number 1,8: "))
if select==1:  
     usr=input("input the user name")
     pas=input("input the password")
     success=flute.login(username=usr,password=pas)
     if success==True:
        print("you have successfuly login")
        inchoose()
        if select==2:
            fol=input("enter the id name which you follow ")
            flute.follow(fol)
        elif select==3:
            path=input("enter the path of picture")
            capt=input("enter the caption")
            flute.upload_photo(path,caption=capt)
        elif select==4:#unfollow the use id
            usrid=input("enter the user id")
            flute.unfollow(usrid)
        elif select==5:#message multi person
            msg=input("enter the message")
            ls=eval(input("lists of user idslist[]/ user name by given commas"))
            flute.send_message(msg,ls)
        elif select==6:#geting list of followers
            ids=input("enter the user id")
            followers=flute.get_user_followers(ids)
            for follower in followers:
                print(bot.get_user_info(follower))
        elif select==7:#fing list of following
            for Following in following:
                print(bot.get_user_info(Following))
        else:
            print("invalid  userid  or password ")
else:   
    sys.exit()

    



    


