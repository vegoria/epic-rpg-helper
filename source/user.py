from reminders import Reminders

class User(object):
    def __init__(self, user):
        self.user = user
        self.messagesChannel = None
        self.reminders = None

    def __eq__(self, o: object) -> bool:
        return str(self) == str(o)
    
    def __str__(self) -> str:
        return self.getUsername()

    def getUsername(self):
        return self.user.name
    
    def getFullUsername(self):
        return "#".join([self.user.name, self.user.discriminator])

    def getMessagesChannel(self):
        return self.messagesChannel

    def setMessagesChannel(self, channel):
        self.messagesChannel = channel

    def enableReminders(self):
        self.reminders = Reminders()
    
    def disableReminders(self):
        self.reminders = None
    
    def setDonorTier(self, tier):
        if self.reminders:
            self.reminders.setCooldownReduction(tier)