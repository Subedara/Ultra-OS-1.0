
import datetime as d

print("""Hello to Ultra OS 1.0
In this OS, there are some 
Ultra specific features like
opening mp3, mp4, apk, exe
and many more files.

Many features are still in
development, so you might
have to wait for Ultra OS 1.5
or Ultra OS 2.0.

--Subedara

""")
beginnerprompt = input("Make a new account? ")
if beginnerprompt == "yes":
    username = input("Enter your usename: ")
    password = input("Enter a secure password: ")
    print("Account Created...")
    print("Login with your new account...")
    usercheck = input("Enter your username: ")
    passcheck = input("Enter your password: ")
    if usercheck == username and passcheck == password:
        print("You have Signed in your account. Start writing commands, or write 'help' for a list of commands...")
        while True:
            a = input("Ultra OS 1.0 -> ")
            if a == "help":
                print("""Ultra OS 1.0 has a lot
of commands. Some of these are:
                    --> echo = used to output a statement
                    --> time = used to show the time with
                    the format of YYYY-MM-DD-hh-mm-ss.mm""")
            elif a == "time":
                print("The time is", d.datetime.now())
    else:
        print("Not the same account. EXITING...")
else:
    print("Okay, EXITING...")
