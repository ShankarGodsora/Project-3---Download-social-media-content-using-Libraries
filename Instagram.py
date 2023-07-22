import instaloader

profile = instaloader.Instaloader()

user = input("Enter the Instagram Username")

profile.download_profile(user,profile_pic_only=False)









