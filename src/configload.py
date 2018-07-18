

class ConfigLoader:
    def __init__(self):
        with open("config.txt", "r") as f:
            self.data = f.read()

        self.data = self.data.split(",")
        while True:
            try:
                self.data.remove("")
            except ValueError:
                break

        for item in self.data:
            print(item)
