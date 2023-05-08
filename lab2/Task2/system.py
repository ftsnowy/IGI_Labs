import sys

from user import User

from commands import (
    WELCOME_MSG, INVALID_CMD_MSG, CMDS_INFO, CMDS, LOAD_MSG, SAVE_MSG, EXIT_MSG, LOGIN_MSG, GET_NAME_MSG, get_info,
    CMDS_ARGS
)


class System:
    def __init__(self):
        self.__user = User("")

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, new_user):
        self.user = new_user

    def start(self):
        print(LOGIN_MSG)
        self.switch()
        get_info()
        while True:
            self.proceed_cmd()

    def switch(self):
        if self.user == "":
            print(SAVE_MSG)
            answer = ""
            while True:
                answer = input()
                if answer != 'y' or answer != 'n':
                    print("Invalid answer")
                else:
                    break
            if answer == 'y':
                self.user.data.save(self.user.username)
        print(GET_NAME_MSG)
        name = input()
        print(WELCOME_MSG)
        get_info()
        self.__user = User(name)

    def exit(self):
        print(SAVE_MSG)
        answer = ""
        while True:
            answer = input()
            if answer != 'y' and answer != 'n':
                print("Invalid answer")
            else:
                break
        if answer == 'y':
            self.user.data.save(self.user.username)
        print(EXIT_MSG)
        sys.exit()

    def proceed_cmd(self):
        command = ""
        while True:
            command = input().split()
            if command[0] not in CMDS:
                print(INVALID_CMD_MSG)
                continue
            elif command[0] == 'add' and len(command) > 1:
                break
            elif CMDS_ARGS[command[0]] != len(command):
                print(INVALID_CMD_MSG)
                continue
            else:
                break
        if command[0] == 'add':
            for el in command[1:]:
                self.add(el)
        if command[0] == 'remove':
            self.remove(command[1])
        if command[0] == 'find':
            self.find(command[1])
        if command[0] == 'list':
            self.list()
        if command[0] == 'grep':
            self.grep(command[1])
        if command[0] == 'save':
            self.save()
        if command[0] == 'load':
            self.load()
        if command[0] == 'switch':
            print(SAVE_MSG)
            answer = ""
            while True:
                answer = input()
                if answer != 'y' and answer != 'n':
                    print("Invalid answer")
                else:
                    break
            if answer == 'y':
                self.user.data.save(self.user.username)
            self.switch()
        if command[0] == 'exit':
            self.exit()

    def add(self, *keys):
        self.user.data.add(keys)

    def remove(self, key):
        self.user.data.remove(key)

    def find(self, key):
        print(self.user.data.find(key))

    def list(self):
        print(self.user.data.list())

    def grep(self, pattern):
        print(self.user.data.grep(pattern))

    def save(self):
        self.user.data.save(self.user.username)

    def load(self):
        self.user.data.load(self.user.username)
