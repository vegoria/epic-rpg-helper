from cooldowns import *

class Reminders(object):
    def __init__(self) -> None:
        super().__init__()
        self.reminders = dict(
                                daily=0,
                                weekly=0,
                                lootbox=0,
                                vote=0,
                                hunt=0,
                                adv=0,
                                training=0,
                                duel=0,
                                quest=0,
                                work=0,
                                farm=0,
                                horse_breeding=0,
                                arena=0,
                                dungeon=0)
        self.lastWorkCommand = "CHOP"
        self.timeReduction = Tier0Cooldowns
    
    def secondElapsed():
        availableCommands = []
        for key in self.reminders.keys:
            if self.reminder[key]-1 >= 0:
                self.reminder[key] = self.reminder[key]-1
            if self.reminder[key] == 0:
                availableCommands.append(key)
        return availableCommands

    def commandUsed(self, command):
        if self.reminders[command] > 0:
            return
        if command not in ["daily", "weekly", "lootbox","vote", "duel"]:
            self.reminders[command] = StandardCooldowns[command] * self.timeReduction
        else:
            self.reminders[command] = StandardCooldowns[command]
    
    def setCooldownReduction(self, reduction):
        self.timeReduction = reduction
    
    def getTimeToHunt(self):
        return self.reminders[hunt]