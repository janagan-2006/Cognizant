class Database:

    def query(self):
        print("Running Query")

class DatabaseProxy:

    def __init__(self):
        self.db = Database()

    def query(self):

        print("Checking Permission")

        self.db.query()

proxy = DatabaseProxy()

proxy.query()