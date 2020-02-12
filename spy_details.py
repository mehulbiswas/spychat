from datetime import datetime

#Delcaring class Spy
class Spy:

    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self_is_online = True
        self.chats = []
        self.current_status_message = None

#Declaring class ChatMessage
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('M','Mr.',24,4.7)

friend_one = Spy('V','Mr.',21,4.6)
friend_two = Spy('J','Mr.',24,4.5)
friend_three = Spy('A','Mr.',20,4.4)


friends = [friend_one,friend_two,friend_three]
