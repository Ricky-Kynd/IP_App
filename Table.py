class Table:
    def __init__(self, data=None, headers=None, width=5):
        self.__data = data
        self.width = width
        self.headers = headers

    def draw_table(self):
        print("|", end="")
        for i in self.headers:
            print("{:<{}}".format(i, self.width), end="")
        print("|")
        print("|{:-^{}}|".format("", self.width * len(self.headers)))
        for i in self.__data:
            print("|", end="")
            for j in i:
                print("{:<{}}".format(j, self.width), end="")
            print("|")

    def __str__(self):
        return "headers={}, width={}, data={}".format(self.headers, self.width, self.__data)