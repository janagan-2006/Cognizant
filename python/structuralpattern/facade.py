#same like adapter but calling many function inside one function is called facade pattern

class Application:

    def start(self):

        print("Database Started")

        print("Cache Started")

        print("Logger Started")

app = Application()

app.start()
