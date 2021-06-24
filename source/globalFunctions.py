from globalVariables import *

def findUser(user):
    for u in UsersList:
        if u == user:
            return u
    return None

def getRpgCommandFamily(command):
    if command in rpgCommands:
        return command
    if command in rpgHuntCommands:
        return "hunt"
    if command in rpgAdvCommands:
        return "adventure"
    if command in rpgTrainingCommands:
        return "training"
    if command in rpgQuestCommands:
        return "quest"
    if command in rpgWorkCommands:
        return "work"
    if command in rpgFarmCommands:
        return "farm"
    if command in rpgHorseCommands:
        return "horse_breeding"
    if command in rpgArenaCommands:
        return "arena"
    if command in rpgDungeonCommands:
        return "dungeon"
    return None