import instaloader

ig = instaloader.Instaloader()
dp = input("Enter instagram username: ")
img = ig.download_profile(dp, profile_pic_only=True)
