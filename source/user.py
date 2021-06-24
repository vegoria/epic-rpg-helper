class User(object):
    def __init__(self, user):
        self.user = user
        messagesChannel = None

    def __eq__(self, o: object) -> bool:
        return str(self) == str(o)
    
    def __str__(self) -> str:
        return self.getUsername()

    def getUsername(self):
        return self.user.name
    
    def getFullUsername(self):
        return "#".join([self.user.name, self.user.discriminator])

    def getMessagesChannel(self):
        return self.setMessagesChannel

    def setMessagesChannel(self, channel):
        self.setMessagesChannel = channel