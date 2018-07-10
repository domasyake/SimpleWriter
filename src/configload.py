

class ConfigLoader:
    def __init__(self):
        with open("config.txt", "r") as f:
            self.data = f.read()

        self.data = self.data.split(",")
        self.data.remove("")

        for item in self.data:
            print(item)
