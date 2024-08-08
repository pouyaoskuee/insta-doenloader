import instaloader
L=instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context,"pouyaoskuee")
profile.get_profile_pic_url()

print((profile.get_profile_pic_url()))