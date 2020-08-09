# Modules
from os import remove
from requests import post
from json import loads, dumps

# Initialization
try:

    WBURL = loads(open("save.json", "r").read())["url"]

except:

    WBURL = input("Webhook URL: ")

    SAVE = input("Save this URL: ").lower()

    if SAVE in ["yes", "yea", "ye", "plz", "pls"]:

        open("save.json", "w+").write(dumps({"url": WBURL}, indent = 4))

# Main loop
while True:

    MESSAGE = ""

    # Fetch the message
    while True:

        x = input("> ")

        if x != "send":

            if not x.lower() in ["cancel", "exit"]:

                MESSAGE += x + "\n"

            elif x == "exit":

                exit()

            elif x == "cancel":

                MESSAGE = ""

                print("\nMessage cleared.\n")

        else:

            break

    # Message sending
    try:

        r = post(WBURL, data = {"content": MESSAGE})

    except:

        print("\nInvalid webhook URL.\n")

        try:

            remove("save.json")

            exit()

        except:

            pass

    # Check if successful
    if r.status_code != 204:

        print("\nSomething went wrong!\n")

    else:

        print("\nCode " + str(r.status_code) + " (OK): Message sent successfully.\n")
