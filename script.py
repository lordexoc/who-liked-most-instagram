import instaloader

L = instaloader.Instaloader()

username = 'username'
password = 'pass'

profile_username = 'gaben_newell'


try:
    L.context.log("Trying to login with given credentials.")
    L.load_session_from_file(username)
    if L.context.is_logged_in:
        L.context.log("Login successful.")
except FileNotFoundError:
    L.context.log("Session file does not exist yet - Logging in.")
    L.context.log("If you don't want to login, just terminate the script.")
    L.context.log("To save the session after a successful login, press CTRL-Z")
    L.interactive_login(username)

profile = instaloader.Profile.from_username(L.context, profile_username)

for post in profile.get_posts():

    # get only posts
    if not post.is_video:

        # get likes
        try:
            post_likes = post.get_likes()
        except instaloader.exceptions.LoginRequiredException:
            L.interactive_login(username)
            post_likes = post.get_likes()

        # Get the comments of the post
        post_comments = post.get_comments()

        # It will create a file named as profile_username.txt and write all likes to it. You can find your cmd path and open it. ex: if your cmd path is C:\Users\MyPC> then you can find your file in C:\Users\MyPC\profile_username.txt
        like_count = {}
        for likee in post_likes:
            print(likee.username)
            with open(profile_username + ".txt", "a") as f:
                f.write(likee.username + "\n")
