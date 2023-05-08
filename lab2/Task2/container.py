import os
import re


class Container:
    def __init__(self):
        self.__elements = set()

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, new_elements: set[str]):
        self.__elements = new_elements

    def add(self, new_elements):
        self.elements.update(new_elements)

    def list(self):
        return list(self.elements)

    def find(self, key):
        if key in self.elements:
            return key
        else:
            return "No such elements in the container :("

    def remove(self, key):
        if key in self.elements:
            self.elements.remove(key)
        else:
            print("No such elements in the container :(")

    def grep(self, pattern):
        regex = re.compile(pattern)
        found = []
        for s in self.elements:
            if regex.match(s):
                found.append(s)
        if len(found) == 0:
            return "No such elements in the container :("
        else:
            return found

    def save(self, username):
        if len(self.elements) == 0:
            print("Nothing to save")
            return
        path = "/home/yahallo/Labs/lab2/Task2/Users/" + username + ".txt"
        if not os.path.exists(path):
            fd = os.open(path, os.O_CREAT)
            os.close(fd)
        with open(path, "w") as file:
            for el in self.elements:
                file.write(el + '\n')

    def load(self, username):
        path = "/home/yahallo/Labs/lab2/Task2/Users/" + username + ".txt"
        if not os.path.exists(path):
            print("You haven't saved anything yet to load from :)")
            return
        with open(path, "r") as file:
            lines = file.readlines()
        for line in lines:
            self.elements.add(line[:-1])
