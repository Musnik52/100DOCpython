import os
from dotenv import load_dotenv
from insta_follower import InstaFollower

load_dotenv()

password = os.getenv("password")
email = os.getenv("email")

insta_profile = InstaFollower()
insta_profile.login(password, email)
insta_profile.find_followers("setupspawn")
insta_profile.follow()
