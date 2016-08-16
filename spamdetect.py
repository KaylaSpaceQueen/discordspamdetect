spamDict = {}

class spamUserContainer:
    'Class for containing spam information for a user'
    
    #---spam definitions---
    #if numbers of messsages is greater than totalMessages over a period of timePeriod seconds
    #or if number of characters in the messages is greater than totalLength, then increment violations by 1
    #if the total number of violations is greater than or equal to totalViolations then isSpammer() will return True
    timePeriod = 5
    totalMessages = 5
    totalLength = 1024
    totalViolations = 2
    
    def __init__(self,message):
        self.lastMessageTime = message.timestamp
        self.timeStampList = [message.timestamp]
        self.violationCount = 0
    
    def getLastMessageTime(self):
        return self.lastMessageTime

    def upateLastMessageTime(self, message):
        self.lastMessageTime = message.timestamp
        if len(self.timeStampList) >= spamUserContainer.totalMessages:
            self.timeStampList.pop(0)
        self.timeStampList.append(message.timestamp)

    def isSpammer(self,message):
        isASpammer = False
        newestTime = self.timeStampList[0]
        oldestTime = self.timeStampList[-1]     
        timeDifference = (oldestTime-newestTime).total_seconds()
        if len(self.timeStampList) >= spamUserContainer.totalMessages and timeDifference <= spamUserContainer.timePeriod:
            violationCount += 1
        if len(message.content) >= spamUserContainer.totalLength:
            violationCount += 1

        return isASpammer

    def resetViolations(self):
        self.violationCount = 0


async def checkForSpam(message):
    isASpammer = False
    if message.author.id in spamDict:
        spamDict[message.author.id].upateLastMessageTime(message)
    else:
        spamDict[message.author.id] = spamUserContainer(message)

    if spamDict[message.author.id].isSpammer(message):
        isASpammer = True

    return isASpammer

async def resetUserViolations(userid):
    spamDict[userid].resetViolations()
