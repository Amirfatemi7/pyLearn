import instaloader
import getpass

oldFollowers = []
with open("follower.txt","r") as f:
    for line in f:
        oldFollowers.append(line)

insta = instaloader.Instaloader()

# userName = input("enter username: ")
# password = getpass.getpass("enter password: ")
userName = "_amir_fatemi"
password = "359874126"

insta.login(userName,password)
print("login successfully")

profile = instaloader.Profile.from_username(insta.context,userName)

newFollowers = []
for follower in profile.get_followers():
    newFollowers.append(follower)


for oldFollower in oldFollowers:
    if oldFollower not in newFollowers:
        print(oldFollower)

with open("follower.txt","w") as f:
    for follower in newFollowers:
        f.write(str(follower)+"\n")
        


