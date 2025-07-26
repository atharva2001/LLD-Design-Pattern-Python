class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)

from abc import ABC, abstractmethod
class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, event):
        pass
        

class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channel, event):
        print(f"{self.name} received notification from {channel}: {event}")


channel = YoutubeChannel("Tech Channel")
user1 = YoutubeUser("Alice")
user2 = YoutubeUser("Bob")
channel.subscribe(user1)
channel.subscribe(user2)
channel.notify("New video uploaded!")  # Alice and Bob will receive the notification
        