class Youtube:
    def __init__(self, username, subscribers):
        self.username = username
        self.subscribers = subscribers

user1 = Youtube("Elshad", 0)
print(user1.username)
print(user1.subscribers)

user2 = Youtube("Renad", 0)
user2.subscribers = 5
print(user2.username)
print(user2.subscribers)
