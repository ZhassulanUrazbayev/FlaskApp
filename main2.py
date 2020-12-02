# !/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import requests
import datetime
import schedule
import time
import json

app = Flask(__name__)

executors = {
    'default': ThreadPoolExecutor(16),
    'processpool': ProcessPoolExecutor(4)
}

sched = BackgroundScheduler(timezone='Asia/Almaty', executors=executors)

# cron = BackgroundScheduler(daemon=True)
# # Explicitly kick off the background thread
# cron.start()

waInstance = "waInstance9345"

apiToken = "b227b815d5a5badbc09e7f903f2ae17952f77a420de0f11d1f"

creatGroupUrl = "https://api.green-api.com/" + waInstance + "/createGroup/" + apiToken

sendMessageUrl = "https://api.green-api.com/" + waInstance + "/sendMessage/" + apiToken

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().strftime("%m")
year = datetime.datetime.now().strftime("%Y")

countCharNumber = 1
number = 0

whatsappId = "77764497092@c.us"

headers = {
    'Content-Type': 'application/json'
}

print(countCharNumber)
chatIds = []
chatIdsYesterday = []
chatInviteLinksToday = []
chatInviteLinksYesterday = []
inviteLinksIndex = 0
sendMessageIndex = 0

# date_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"14"+":"+"40"), '%Y-%m-%dT%H:%M')

def createGruop1(chatNumber):
    creatGroup = "{\r\n\t\"groupName\": \"Қуаныш Шонбайдың %d\",\r\n    \"chatIds\": [\r\n        \"%s\"\r\n\t]\r\n}\r\n" % (
        chatNumber, whatsappId)

    print(creatGroup)

    creatGroupResponse = requests.request("POST", creatGroupUrl, headers=headers, data=creatGroup.encode('utf8'))

    y = json.loads(creatGroupResponse.text.encode('utf8'))

    print(creatGroupResponse.text.encode('utf8'))

    if y['created']:
        print(y['chatId'])
        global chatIds
        print(str(y['chatId']) + " chatId")
        chatIds.append(y['chatId'])
        print(str(y['groupInviteLink']) + " groupInviteLink")
        global chatInviteLinksToday
        chatInviteLinksToday.append(y['groupInviteLink'])
        print(chatInviteLinksToday)
        print(creatGroupResponse.text.encode('utf8'))
        # global chatId
        global countCharNumber
        # chatId = y['chatId']
        countCharNumber = chatNumber + 1
    else:
        print("Suka bliat zhasamait minau CreateGroup")


def createGruopSecond(chatNumber):
    creatGroup = "{\r\n\t\"groupName\": \"Қуаныш Шонбайдың %d\",\r\n    \"chatIds\": [\r\n        \"%s\"\r\n\t]\r\n}\r\n" % (
        chatNumber, whatsappId)

    print(creatGroup)

    creatGroupResponse = requests.request("POST", creatGroupUrl, headers=headers, data=creatGroup.encode('utf8'))

    y = json.loads(creatGroupResponse.text.encode('utf8'))

    print(creatGroupResponse.text.encode('utf8'))

    if y['created']:
        print(y['chatId'])
        global chatIds
        print(str(y['chatId']) + " chatId")
        chatIds.append(y['chatId'])
        print(str(y['groupInviteLink']) + " groupInviteLink")
        global chatInviteLinksToday
        chatInviteLinksToday.append(y['groupInviteLink'])

        print(creatGroupResponse.text.encode('utf8'))

        # global chatId
        global countCharNumber
        # global inviteLinksIndex
        # chatId = y['chatId']
        countCharNumber = chatNumber + 1
        # print(str(inviteLinksIndex) + " inviteLinksIndex before change")
        # inviteLinksIndex += 1
        # print(str(inviteLinksIndex) + " inviteLinksIndex after change")
    else:
        print("Suka bliat zhasamait minau CreateGroup")


def sendMessageAt1850():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use Green-API to send this to you 18-50 !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex +=1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1851():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use to send this Green-API  to you 18-50 !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1852():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use Green-API to to you send this Green-API !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1853():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this to you 18-50 !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1854():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this 18-50 !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1855():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this to you message you you !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1856():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I you you use you this to you 18-50 !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1857():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this to you 18-50 this to you 18-50 this to you 18-50 !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1858():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this this this this to you 18-50 !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1859():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use you you you you to you 18-50 !\"\r\n}" % (
        chatIds[sendMessageIndex])

    sendMessageIndex = 0

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1900():
    sendMessageAt1900 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use Green-API to send this http://stackoverflow.com to you 19-00 !\"\r\n}" % (
        chatIds[inviteLinksIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1900.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print("I'm working at 19-00")

def sendToOldMessageAt1850():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use Green-API to send this to you 18-50 !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex +=1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1851():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use to send this Green-API  to you 18-50 !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1852():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use Green-API to to you send this Green-API !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1853():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this to you 18-50 !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1854():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this 18-50 !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1855():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this to you message you you !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1856():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I you you use you this to you 18-50 !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1857():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this to you 18-50 this to you 18-50 this to you 18-50 !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1858():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use this this this this to you 18-50 !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1859():
    global sendMessageIndex

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use you you you you to you 18-50 !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex = 0

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt1900():
    global sendMessageIndex

    sendMessageAt1900 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use Green-API to send this http://stackoverflow.com to you 19-00 !\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex = 0

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1900.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print("I'm working at 19-00")


def createGroupSecond():
    global countCharNumber
    createGruopSecond(countCharNumber)


def createGroup():
    global countCharNumber
    createGruop1(countCharNumber)


def jobsendMessageAt1850():
    global chatId
    sendMessageAt1850()
def jobsendMessageAt1851():
    global chatId
    sendMessageAt1851()
def jobsendMessageAt1852():
    global chatId
    sendMessageAt1852()
def jobsendMessageAt1853():
    global chatId
    sendMessageAt1853()
def jobsendMessageAt1854():
    global chatId
    sendMessageAt1854()
def jobsendMessageAt1855():
    global chatId
    sendMessageAt1855()
def jobsendMessageAt1856():
    global chatId
    sendMessageAt1856()
def jobsendMessageAt1857():
    global chatId
    sendMessageAt1857()
def jobsendMessageAt1858():
    global chatId
    sendMessageAt1858()
def jobsendMessageAt1859():
    global chatId
    sendMessageAt1859()
def jobsendMessageAt1900():
    global chatId
    sendMessageAt1900()

def jobsendToOldMessageAt1850():
    global chatId
    sendToOldMessageAt1850()
def jobsendToOldMessageAt1851():
    global chatId
    sendToOldMessageAt1851()
def jobsendToOldMessageAt1852():
    global chatId
    sendToOldMessageAt1852()
def jobsendToOldMessageAt1853():
    global chatId
    sendToOldMessageAt1853()
def jobsendToOldMessageAt1854():
    global chatId
    sendToOldMessageAt1854()
def jobsendToOldMessageAt1855():
    global chatId
    sendToOldMessageAt1855()
def jobsendToOldMessageAt1856():
    global chatId
    sendToOldMessageAt1856()
def jobsendToOldMessageAt1857():
    global chatId
    sendToOldMessageAt1857()
def jobsendToOldMessageAt1858():
    global chatId
    sendToOldMessageAt1858()
def jobsendToOldMessageAt1859():
    global chatId
    sendToOldMessageAt1859()
def jobsendToOldMessageAt1900():
    global chatId
    sendToOldMessageAt1900()

# @cron.interval_schedule(hours=1)
def changeGroupInviteLinks():
    global chatInviteLinksToday
    global chatInviteLinksYesterday
    global inviteLinksIndex
    inviteLinksIndex = 0
    global sendMessageIndex
    sendMessageIndex = 0
    global countCharNumber
    countCharNumber = 1
    global number
    number = 0
    print(str(chatInviteLinksYesterday) + " before chatInviteLinksYesterday")
    print(str(chatInviteLinksToday) + " before chatInviteLinksToday")
    chatInviteLinksYesterday = chatInviteLinksToday
    print(str(chatInviteLinksToday) + " after chatInviteLinksToday")
    print(str(chatInviteLinksYesterday) + " after chatInviteLinksYesterday")
    chatInviteLinksToday.clear()
    print(str(chatInviteLinksToday) + " after clear chatInviteLinksToday")
    global chatIds
    global chatIdsYesterday
    print(str(chatIds) + " before chatIds")
    print(str(chatIdsYesterday) + " before chatIdsYesterday")
    chatIdsYesterday = chatIds
    print(str(chatIds) + " after chatIds")
    print(str(chatIdsYesterday) + " after chatIdsYesterday")
    chatIds.clear()
    print(str(chatIds) + " after clear chatIds")

ChangeGroupInviteLinksTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"00"), '%Y-%m-%dT%H:%M')

sched.add_job(changeGroupInviteLinks, trigger='date', next_run_time=ChangeGroupInviteLinksTime)

FirstGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"01"), '%Y-%m-%dT%H:%M')
SecondGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"02"), '%Y-%m-%dT%H:%M')
ThirdGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"03"), '%Y-%m-%dT%H:%M')
FoursGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"04"), '%Y-%m-%dT%H:%M')
FivesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"05"), '%Y-%m-%dT%H:%M')
SixesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"06"), '%Y-%m-%dT%H:%M')
SevensGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"07"), '%Y-%m-%dT%H:%M')
EighthsGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"08"), '%Y-%m-%dT%H:%M')
NinesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"09"), '%Y-%m-%dT%H:%M')
TensGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"10"), '%Y-%m-%dT%H:%M')
ElevensGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"11"), '%Y-%m-%dT%H:%M')
TwelvesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"12"), '%Y-%m-%dT%H:%M')
ThirdsGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"13"), '%Y-%m-%dT%H:%M')
FourteenthGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"14"), '%Y-%m-%dT%H:%M')
FifteensGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"15"), '%Y-%m-%dT%H:%M')
# sched.add_job(jobsendMessageAt1900, trigger='date', next_run_time=EighthsGroupCreationDate_time)

sched.add_job(createGroup, trigger='date', next_run_time=FirstGroupCreationDate_time)
sched.add_job(createGroupSecond, trigger='date', next_run_time=SecondGroupCreationDate_time)
sched.add_job(createGroupSecond, trigger='date', next_run_time=ThirdGroupCreationDate_time)
sched.add_job(createGroupSecond, trigger='date', next_run_time=FoursGroupCreationDate_time)
sched.add_job(createGroupSecond, trigger='date', next_run_time=FivesGroupCreationDate_time)
sched.add_job(createGroupSecond, trigger='date', next_run_time=SixesGroupCreationDate_time)
sched.add_job(createGroupSecond, trigger='date', next_run_time=SevensGroupCreationDate_time)
sched.add_job(createGroupSecond, trigger='date', next_run_time=EighthsGroupCreationDate_time)
sched.add_job(createGroupSecond, trigger='date', next_run_time=NinesGroupCreationDate_time)
sched.add_job(createGroupSecond, trigger='date', next_run_time=TensGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=ElevensGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=ThirdGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=FourteenthGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=FifteensGroupCreationDate_time)

FirstMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"16"), '%Y-%m-%dT%H:%M')
SecondMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"17"), '%Y-%m-%dT%H:%M')
ThirdMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"18"), '%Y-%m-%dT%H:%M')
FoursMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"19"), '%Y-%m-%dT%H:%M')
FivesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"20"), '%Y-%m-%dT%H:%M')
SixesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"21"), '%Y-%m-%dT%H:%M')
SevensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"22"), '%Y-%m-%dT%H:%M')
EightsMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"23"), '%Y-%m-%dT%H:%M')
NinesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"24"), '%Y-%m-%dT%H:%M')
TensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"25"), '%Y-%m-%dT%H:%M')

sched.add_job(jobsendMessageAt1850, trigger='date', next_run_time=FirstMessageTime)
sched.add_job(jobsendMessageAt1851, trigger='date', next_run_time=SecondMessageTime)
sched.add_job(jobsendMessageAt1852, trigger='date', next_run_time=ThirdMessageTime)
sched.add_job(jobsendMessageAt1853, trigger='date', next_run_time=FoursMessageTime)
sched.add_job(jobsendMessageAt1854, trigger='date', next_run_time=FivesMessageTime)
sched.add_job(jobsendMessageAt1855, trigger='date', next_run_time=SixesMessageTime)
sched.add_job(jobsendMessageAt1856, trigger='date', next_run_time=SevensMessageTime)
sched.add_job(jobsendMessageAt1857, trigger='date', next_run_time=EightsMessageTime)
sched.add_job(jobsendMessageAt1858, trigger='date', next_run_time=NinesMessageTime)
sched.add_job(jobsendMessageAt1859, trigger='date', next_run_time=TensMessageTime)

ChangeGroupInviteLinksTime2 = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"26"), '%Y-%m-%dT%H:%M')

sched.add_job(changeGroupInviteLinks, trigger='date', next_run_time=ChangeGroupInviteLinksTime2)

FirstMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"26"), '%Y-%m-%dT%H:%M')
SecondMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"27"), '%Y-%m-%dT%H:%M')
ThirdMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"28"), '%Y-%m-%dT%H:%M')
FoursMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"29"), '%Y-%m-%dT%H:%M')
FivesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"30"), '%Y-%m-%dT%H:%M')
SixesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"31"), '%Y-%m-%dT%H:%M')
SevensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"32"), '%Y-%m-%dT%H:%M')
EightsMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"33"), '%Y-%m-%dT%H:%M')
NinesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"34"), '%Y-%m-%dT%H:%M')
TensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"17"+":"+"35"), '%Y-%m-%dT%H:%M')

sched.add_job(jobsendToOldMessageAt1850, trigger='date', next_run_time=FirstMessageTime)
sched.add_job(jobsendToOldMessageAt1851, trigger='date', next_run_time=SecondMessageTime)
sched.add_job(jobsendToOldMessageAt1852, trigger='date', next_run_time=ThirdMessageTime)
sched.add_job(jobsendToOldMessageAt1853, trigger='date', next_run_time=FoursMessageTime)
sched.add_job(jobsendToOldMessageAt1854, trigger='date', next_run_time=FivesMessageTime)
sched.add_job(jobsendToOldMessageAt1855, trigger='date', next_run_time=SixesMessageTime)
sched.add_job(jobsendToOldMessageAt1856, trigger='date', next_run_time=SevensMessageTime)
sched.add_job(jobsendToOldMessageAt1857, trigger='date', next_run_time=EightsMessageTime)
sched.add_job(jobsendToOldMessageAt1858, trigger='date', next_run_time=NinesMessageTime)
sched.add_job(jobsendToOldMessageAt1859, trigger='date', next_run_time=TensMessageTime)

@app.route('/')
def index():
    global number
    number += 1
    global chatInviteLinksToday
    global inviteLinksIndex
    print(str(number)+" this is number")
    if number >= 256:
        if inviteLinksIndex == len(chatInviteLinksToday) - 1:
            inviteLinksIndex = inviteLinksIndex
        else:
            inviteLinksIndex += 1
        return redirect(chatInviteLinksToday[inviteLinksIndex])
    else:
        return redirect(chatInviteLinksToday[inviteLinksIndex])
    # app.run(host="45.149.128.147",port=80)


if __name__ == "__main__":
    sched.start()
    app.run(host="45.149.128.147",port=80, debug=True, use_reloader=False)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
