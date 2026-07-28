# One object changes.

# Many objects get notified.

class Subscriber:

    def update(self, video):
        print(f"New video: {video}")

class Channel:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def upload(self, video):

        for subscriber in self.subscribers:
            subscriber.update(video)

channel = Channel()

s1 = Subscriber()
s2 = Subscriber()

channel.subscribe(s1)
channel.subscribe(s2)

channel.upload("Python OOP")