WELCOME_MSG = "Hello! That's CLI :)"
LOGIN_MSG = "To continue you need to login first!"
INVALID_CMD_MSG = "Invalid command :("
GET_NAME_MSG = "Enter your name:"

CMDS_INFO = [
    "add <key> or [key....] - add one or more elements to the container",
    "remove <key> – delete key from container;",
    "find <key> – check if the element is presented in the container",
    "list - returns all elements of the container",
    "grep <regex> - checks heck the value in the container by regular expression",
    "save - saves container to file",
    "load - loads container from file",
    "switch - switches to another user",
    "exit - stop program"
]

CMDS = ["add", "remove", "find", "list", "grep", "save", "save", "load", "switch", "exit"]

CMDS_ARGS = {
    "remove": 2,
    "find": 2,
    "list": 1,
    "grep": 2,
    "save": 1,
    "load": 1,
    "switch": 1,
    "exit": 1,
    "add": -1
}


LOAD_MSG = "Would you like to load your container? [y/n]"
SAVE_MSG = "Would you like to save your container? [y/n]"
EXIT_MSG = "Bye, see you again :)"


def get_info():
    for cmd in CMDS_INFO:
        print(cmd)

