from container import Container


class User:
    def __init__(self, username):
        self.__username = username
        self.__data = Container()

    @property
    def username(self):
        return self.__username

    @property
    def data(self):
        return self.__data

    @username.setter
    def username(self, new_un):
        self.__username = new_un

    @data.setter
    def data(self, new_data):
        self.__data = new_data



