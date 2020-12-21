# !/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import requests
import datetime
from datetime import date
from openpyxl import load_workbook
from openpyxl import Workbook
import json

app = Flask(__name__)

executors = {
    'default': ThreadPoolExecutor(16),
    'processpool': ProcessPoolExecutor(4)
}

wb = Workbook()

ws = wb.active

dataChatIds = ["77764497092-1607055302@g.us","77764497092-1607055242@g.us","77764497092-1607055182@g.us","77764497092-1607055122@g.us","77764497092-1607055063@g.us","77764497092-1607055002@g.us","77764497092-1607054942@g.us","77764497092-1607054883@g.us","77764497092-1607054824@g.us","77764497092-1607054764@g.us"
]

dataInviteLinks = ["https://chat.whatsapp.com/IUEDsa1eLRcCavmHqLs38c","https://chat.whatsapp.com/H09cgpDt9yuGhlMxtcGPJm","https://chat.whatsapp.com/LwWNwGEWi4M2Uyq1yBQknp","https://chat.whatsapp.com/KM1UTVXwNLL58fIBGHHqp4","https://chat.whatsapp.com/FYjHY4yMKCnIM8DFbOmF9S","https://chat.whatsapp.com/CwaHSZBGwFtDCTlNwb48hy","https://chat.whatsapp.com/EzPJ1OvCV6eInsXPPuI7on","https://chat.whatsapp.com/I9BhGRcAVIiBIqiNo4clcE","https://chat.whatsapp.com/LiJn43o92SK3zf97cUSHc5","https://chat.whatsapp.com/BJTh3b8gaSmJ2ECzJAzVrw"
]

sched = BackgroundScheduler(timezone='Asia/Almaty', executors=executors)

createdChatIds = ["77764497092-1607055302@g.us","77764497092-1607055242@g.us"]
createdInviteLinks = ["https://chat.whatsapp.com/IUEDsa1eLRcCavmHqLs38c","https://chat.whatsapp.com/H09cgpDt9yuGhlMxtcGPJm"]

createdChatIds17 = ["77764497092-1608210014@g.us",
                    "77764497092-1608210085@g.us",
                    "77764497092-1608210144@g.us",
                    "77764497092-1608210202@g.us",
                    "77764497092-1608210262@g.us",
                    "77764497092-1608210322@g.us",
                    "77764497092-1608210383@g.us",
                    "77764497092-1608210442@g.us",
                    "77764497092-1608210503@g.us",
                    "77764497092-1608455536@g.us",
                    "77764497092-1608455636@g.us"]
createdInviteLinks17 = ['https://chat.whatsapp.com/J8TnhYatkGVHITQY6Sl1zS',
                        'https://chat.whatsapp.com/K22nDxQeugN8yQn2Qix2EA',
                        'https://chat.whatsapp.com/HgEggPVP3OWFT05Joo6nwD',
                        'https://chat.whatsapp.com/F6RVFL42A30Awg1qHAwm1N',
                        'https://chat.whatsapp.com/Kp75Sbup5KGJA2LOuk7wNI',
                        'https://chat.whatsapp.com/DqtA2ecPj4NAO4UmxTg9Qb',
                        'https://chat.whatsapp.com/FsyPP2M6dKGJzFfMhctpln',
                        'https://chat.whatsapp.com/IShLAu7wQy7GMws8gqrh6d',
                        'https://chat.whatsapp.com/DL1IZAPkjLXLZPb4LS8HIg',
                        "https://chat.whatsapp.com/KElpZEnpe1kDkCWB5swUAz",
                        "https://chat.whatsapp.com/F6DO1FzRf5Y5LFWhrDfmws"]

newestChatIds = ["77764497092-1607055302@g.us","77764497092-1607055242@g.us","77764497092-1607055182@g.us","77764497092-1607055122@g.us","77764497092-1607055063@g.us","77764497092-1607055002@g.us","77764497092-1607054942@g.us","77764497092-1607054883@g.us","77764497092-1607054824@g.us","77764497092-1607054764@g.us"]
newestInviteLinks = ["https://chat.whatsapp.com/IUEDsa1eLRcCavmHqLs38c","https://chat.whatsapp.com/H09cgpDt9yuGhlMxtcGPJm","https://chat.whatsapp.com/LwWNwGEWi4M2Uyq1yBQknp","https://chat.whatsapp.com/KM1UTVXwNLL58fIBGHHqp4","https://chat.whatsapp.com/FYjHY4yMKCnIM8DFbOmF9S","https://chat.whatsapp.com/CwaHSZBGwFtDCTlNwb48hy","https://chat.whatsapp.com/EzPJ1OvCV6eInsXPPuI7on","https://chat.whatsapp.com/I9BhGRcAVIiBIqiNo4clcE","https://chat.whatsapp.com/LiJn43o92SK3zf97cUSHc5","https://chat.whatsapp.com/BJTh3b8gaSmJ2ECzJAzVrw"]

olderChatIds = []
olderInviteLinks = []

allChatIds = []

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
filledArrayIndex = len(createdChatIds17) - 1

# date_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"14"+":"+"40"), '%Y-%m-%dT%H:%M')

def createGruop1(chatNumber):
    creatGroup = "{\r\n\t\"groupName\": \"ТЕГІН мастер-класс\",\r\n    \"chatIds\": [\r\n        \"%s\"\r\n\t]\r\n}\r\n" % (
        whatsappId)

    print(creatGroup.encode('utf8'))

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
        global dataChatIds
        global dataInviteLinks
        dataChatIds.append(y['chatId'])
        dataInviteLinks.append(y['groupInviteLink'])
        # global chatId
        global countCharNumber
        # chatId = y['chatId']
        countCharNumber = chatNumber + 1
    else:
        print("Suka bliat zhasamait minau CreateGroup")

def createTimelyGroup():
    creatGroup = "{\r\n\t\"groupName\": \"ТЕГІН мастер-класс\",\r\n    \"chatIds\": [\r\n        \"%s\"\r\n\t]\r\n}\r\n" % (
        whatsappId)

    print(creatGroup.encode('utf8'))

    creatGroupResponse = requests.request("POST", creatGroupUrl, headers=headers, data=creatGroup.encode('utf8'))

    y = json.loads(creatGroupResponse.text.encode('utf8'))

    print(creatGroupResponse.text.encode('utf8'))

    if y['created']:
        global filledArrayIndex
        filledArrayIndex += 1
        print(y['chatId'])
        global chatIds
        print(str(y['chatId']) + " chatId")
        chatIds.append(y['chatId'])
        print(str(y['groupInviteLink']) + " groupInviteLink")
        global chatInviteLinksToday
        chatInviteLinksToday.append(y['groupInviteLink'])
        print(chatInviteLinksToday)
        print(creatGroupResponse.text.encode('utf8'))
        global dataChatIds
        global dataInviteLinks
        dataChatIds.append(y['chatId'])
        dataInviteLinks.append(y['groupInviteLink'])
        createdChatIds17.append(y['chatId'])
        createdInviteLinks17.append(y['groupInviteLink'])
        # global chatId
        global countCharNumber
        # chatId = y['chatId']
    else:
        print("Suka bliat zhasamait minau CreateGroup")


def createGruopSecond():
    global whatsappId
    global chatIds
    global chatInviteLinksToday
    global createdChatIds
    global createdInviteLinks
    print("I'm working createGruopSecond")
    for i in createdChatIds:
        chatIds.append(i)
    for j in createdInviteLinks:
        chatInviteLinksToday.append(j)



def sendMessageAt1850():
    global sendMessageIndex
    global chatIds

    print(str(sendMessageIndex)+" sendMessageIndex")

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ЖАЛПЫ ҚҰНЫ 1.000.000 тг ТҰРАТЫН САБАҚТЫ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты мастер-классы бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇 https://u.to/jqPgGQ?utm_source=wh&utm_medium=first&utm_campaign=invite\"\r\n}" % (
        chatIds[sendMessageIndex])

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1851():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"2 САҒАТ КИНО КӨРГЕНШЕ, ҚУАНЫШ ШОНБАЙДАН ТЕГІН БІЛІМ АЛ😍\\n\\nСен бүгін Алматы уақыты бойынша 19.00-21.00 аралығында не істейсің?Әрине, Қуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты ТЕГІН мастер-классын көресің 💸❤\\n\\nАл қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥 https://u.to/jqPgGQ?utm_source=wh&utm_medium=second&utm_campaign=invite\"\r\n}" % (
            createdChatIds[sendMessageIndex])

        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"2 САҒАТ КИНО КӨРГЕНШЕ, ҚУАНЫШ ШОНБАЙДАН ТЕГІН БІЛІМ АЛ😍\\n\\nСен бүгін Алматы уақыты бойынша 19.00-21.00 аралығында не істейсің?Әрине, Қуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты ТЕГІН мастер-классын көресің 💸❤\\n\\nАл қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥 https://u.to/jqPgGQ?utm_source=wh&utm_medium=second&utm_campaign=invite\"\r\n}" % (
            createdChatIds[sendMessageIndex])

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1852():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ОСЫ ГРУППДАҒЫ БАРЛЫҚ АДАМДЫ ӨЗ ҮЙІМЕ ҚОНАҚҚА ШАҚЫРАМЫН😍🔥\\n\\nЕлдің бәрі тегін сабаққа кіріп, құнды білім алып жатыр. Ал сен әлі не істеріңді білмей отырсың 😑👎🏻\\n\\nЕлден қалмай, сен де қатыс. Дәл қазір мына сілтеме бойынша өт https://u.to/jqPgGQ?utm_source=wh&utm_medium=third&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ОСЫ ГРУППДАҒЫ БАРЛЫҚ АДАМДЫ ӨЗ ҮЙІМЕ ҚОНАҚҚА ШАҚЫРАМЫН😍🔥\\n\\nЕлдің бәрі тегін сабаққа кіріп, құнды білім алып жатыр. Ал сен әлі не істеріңді білмей отырсың 😑👎🏻\\n\\nЕлден қалмай, сен де қатыс. Дәл қазір мына сілтеме бойынша өт https://u.to/jqPgGQ?utm_source=wh&utm_medium=third&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1853():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ҚҰНЫ 1.000.000 тг ТҰРАТЫН САБАҚТЫ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты мастер-классы Алматы қаласы бойынша бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇 https://u.to/jqPgGQ?utm_source=wh&utm_medium=fours&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])
        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ҚҰНЫ 1.000.000 тг ТҰРАТЫН САБАҚТЫ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты мастер-классы Алматы қаласы бойынша бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇 https://u.to/jqPgGQ?utm_source=wh&utm_medium=fours&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])
        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1854():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ОСЫ ГРУППДАҒЫ БАРЛЫҚ АДАМДЫ ҚОНАҚҚА ШАҚЫРАМЫН😍🔥\\n\\nБірақ карантин болғандықтан, үйіме онлайн қонақ боласыз. Келгендерге арнайы бонус-сарқыт дайындап қойдым. Бүгін Алматы уақыты бойынша 19.00-да күтем. Кешікпеңіз🥳🔥 https://u.to/jqPgGQ?utm_source=wh&utm_medium=fives&utm_campaign=invite\\n\\n(С) ҚУАНЫШ ШОНБАЙ\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ОСЫ ГРУППДАҒЫ БАРЛЫҚ АДАМДЫ ҚОНАҚҚА ШАҚЫРАМЫН😍🔥\\n\\nБірақ карантин болғандықтан, үйіме онлайн қонақ боласыз. Келгендерге арнайы бонус-сарқыт дайындап қойдым. Бүгін Алматы уақыты бойынша 19.00-да күтем. Кешікпеңіз🥳🔥 https://u.to/jqPgGQ?utm_source=wh&utm_medium=fives&utm_campaign=invite\\n\\n(С) ҚУАНЫШ ШОНБАЙ\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1855():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"2 САҒАТЫҢДЫ КИНОҒА ҚҰРТҚАНША, ҚУАНЫШ ШОНБАЙДАН ТЕГІН БІЛІМ АЛ😍\\n\\nБүгін Алматы уақыты бойынша 19.00-21.00 аралығында не істейсің? Әрине, Қуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты ТЕГІН мастер-классын көресің 💸\\n\\nДәл қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sixes&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"2 САҒАТЫҢДЫ КИНОҒА ҚҰРТҚАНША, ҚУАНЫШ ШОНБАЙДАН ТЕГІН БІЛІМ АЛ😍\\n\\nБүгін Алматы уақыты бойынша 19.00-21.00 аралығында не істейсің? Әрине, Қуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты ТЕГІН мастер-классын көресің 💸\\n\\nДәл қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sixes&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1856():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ЖАЛПЫ ҚҰНЫ 1.000.000 тг ТҰРАТЫН БІЛІМДІ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты мастер-классы бүгін Алматы уақыты бойынша 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sevens&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ЖАЛПЫ ҚҰНЫ 1.000.000 тг ТҰРАТЫН БІЛІМДІ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты мастер-классы бүгін Алматы уақыты бойынша 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sevens&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1857():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ҚУАНЫШ ШОНБАЙДАН ТЕГІН САБАҚ😍\\n\\nҚуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты мастер-классы Алматы қаласы бойынша бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=eights&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])
        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ҚУАНЫШ ШОНБАЙДАН ТЕГІН САБАҚ😍\\n\\nҚуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты мастер-классы Алматы қаласы бойынша бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=eights&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])
        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1858():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"2 САҒАТЫҢДЫ КИНОҒА ҚҰРТҚАНША, ҚУАНЫШ ШОНБАЙДАН БІЛІМ АЛ 😍\\n\\nАлматы уақыты бойынша 19.00-21.00 аралығында не істейсің? Әрине, Қуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты ТЕГІН мастер-классын көресің 💸\\n\\nТура қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=nines&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])
        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"2 САҒАТЫҢДЫ КИНОҒА ҚҰРТҚАНША, ҚУАНЫШ ШОНБАЙДАН БІЛІМ АЛ 😍\\n\\nАлматы уақыты бойынша 19.00-21.00 аралығында не істейсің? Әрине, Қуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты ТЕГІН мастер-классын көресің 💸\\n\\nТура қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=nines&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])
        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1859():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ЖАЛПЫ ҚҰНЫ 1.000.000 тг ТҰРАТЫН САБАҚТЫ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты мастер-классы бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=tens&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

    elif(sendMessageIndex != 20000):
        sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ЖАЛПЫ ҚҰНЫ 1.000.000 тг ТҰРАТЫН САБАҚТЫ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “2021 жылы интернеттен айына 1000$ алып келетін 5 қабілет” атты мастер-классы бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=tens&utm_campaign=invite\"\r\n}" % (
            chatIds[sendMessageIndex])

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1

def sendMessageAt1910():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"БАСТАЛЫП КЕТТІ\\n\\nҚайда жүрсің? 😵\\n\\nМастер-класс 10 минут бұрын басталып кетті. Дәл қазір мына сілтеме бойынша өтпесең, бонуссыз қаласың:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=first&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex +=1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1911():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ҚАЛҚАМ-АУ, ҚАЙДА ЖҮРСІҢ?\\n\\nЕлдің бәрі тегін сабаққа кіріп, құнды білім алып жатыр. Ал сен әлі не істеріңді білмей отырсың 😑👎🏻\\n\\nЕлден қалмай, сен де қатыс. Дәл қазір мына сілтеме бойынша өт\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=second&utm_campaign=invite \"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1912():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"АДАМДЫ ОСЫЛАЙ КҮЙДІРЕСІҢДЕР, БАР ҒОЙ😵\\n\\nШақырған қонақтың бәрі келді! Сен ғана қалдың. Сағат 19.12 болды ғой🥺\\n\\nЕлден қалмай, сен де кел. Дәл қазір мына сілтеме бойынша өт\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=third&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1913():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"БАСТАЛДЫ🔥💸\\n\\nҚайда жүрсің? 😵\\n\\nМастер-класс 10 минут бұрын басталып кетті. Дәл қазір мына сілтеме бойынша өтпесең, бонуссыз қаласың:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=fours&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1914():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"АДАМДЫ ОСЫЛАЙ КҮЙДІРЕСІҢДЕР 😵\\n\\nШақырған қонақтың бәрі келді! Сен ғана қалдың. Уақыт 19.14 болды ғой🥺\\n\\nЕлден қалмай, сен де кел. Дәл қазір мына сілтеме бойынша өт\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=fives&utm_campaign=invite\\n\\n(С) ҚУАНЫШ ШОНБАЙ\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1915():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ҚАЙДАСЫҢ???\\n\\nЕлдің бәрі тегін сабаққа кіріп, білім алып жатыр. Ал сен әлі не істеріңді білмей отырсың 😑👎🏻\\n\\nДәл қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥\\n\\nЕлден қалмай, сен де қатыс. Дәл қазір мына сілтеме бойынша өт\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sixes&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1916():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ТЕГІН МАСТЕР-КЛАСС БАСТАЛДЫ\\n\\nҚайда жүрсің? 😵\\n\\nМастер-класс 10 минут бұрын басталып кетті. Дәл қазір мына сілтеме бойынша өтпесең, бонуссыз қаласың:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sevens&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1917():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"АЙНАЛАЙЫН, ҚАЙДАСЫҢ???🔥💸\\n\\nМастер-класс 17 минут бұрын басталып кетті. Дәл қазір мына сілтеме бойынша өтпесең, бонуссыз қаласың:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=eights&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1918():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"КҮТІП ТҰРМЫН\\n\\nЕлдің бәрі тегін сабаққа кіріп, білім алып жатыр. Ал сен әлі не істеріңді білмей отырсың 😑👎🏻\\n\\nЕлден қалмай, сен де қатыс. Дәл қазір мына сілтеме бойынша өт\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=nines&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1919():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"БАСТАЛЫП КЕТТІ\\n\\nҚайда жүрсің? 😵\\n\\nМастер-класс 10 минут бұрын басталып кетті. Дәл қазір мына сілтеме бойынша өтпесең, бонуссыз қаласың:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=tens&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex = 0

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1930():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"МОЩНО БОП ЖАТЫР! 🚀💸\\n\\nДәл қазір мастер-класстың ?? минутына келдім. Алғашқы 1000$ табудың 3-ші қабілетті тура 3 минуттан кейін айтамын😍\\n\\nОсы уақытқа 3-ші қадамды қолданған адамдар ақша тауып бастады. Сен де құр қалма! Дәл қазір мына сілтеме бойынша өт:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=first&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex +=1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1931():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"УФ, МАСТЕР-КЛАСС 🔥 БОП ЖАТЫР\\n\\nМастер-класстағы атмосфераны сөзбен айтып жеткізу мүмкін емес😍 Дәл қазір мына сілтеме бойынша өт те, сен де табыс табудың нақты 7 қадамын үйреніп ал:\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=second&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1932():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"МАСТЕР-КЛАССТЫҢ ЕҢ ҚЫЗЫҚ ЖЕРІНЕ КЕЛДІМ🔥\\n\\nМастер-класстағы атмосфераны сөзбен айтып жеткізу мүмкін емес😍 Қазір 4-ші қадамды талдайын деп жатырмын. Сондықтан мына сілтеме бойынша өт:\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=third&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1933():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"МОЩНО 🔥🔥🔥💸\\n\\nДәл қазір мастер-класстың ?? минутына келдім. Алғашқы 1000$ табудың 3-ші қадамын тура 3 минуттан кейін айтамын😍\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=fours&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1934():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"МАСТЕР-КЛАССТЫҢ ЕҢ ҚЫЗЫҚ ЖЕРІНЕ КЕЛДІМ🔥\\n\\nАтмосфераны сөзбен айтып жеткізу мүмкін емес😍 Қазір 4-ші қадамды талдаймын. Сондықтан мына сілтеме бойынша өт:\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=fives&utm_campaign=invite\\n\\n(С) ҚУАНЫШ ШОНБАЙ\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1935():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"МАСТЕР-КЛАСС 🔥 БОП ЖАТЫР\\n\\nМастер-класстағы атмосфераны сөзбен айтып жеткізу мүмкін емес😍 Дәл қазір мына сілтеме бойынша өт те, сен де табыс табудың нақты 7 қадамын үйреніп ал:\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sixes&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1936():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"МЫҚТЫ САБАҚ БОП ЖАТЫР! 🚀💸\\n\\nДәл қазір мастер-класстың ?? минутына келдім. Алғашқы 1000$ табудың 3-ші қадамын тура 3 минуттан кейін айтамын😍\\n\\nОсы уақытқа 3-ші қадамды қолданған адамдар ақша тауып бастады. Сен де құр қалма! Дәл қазір мына сілтеме бойынша өт:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sevens&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1937():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"АҚША ТАУЫП ҮЛГЕРДІ🔥💸\\n\\nДәл қазір мастер-класстың ?? минутына келдім. Алғашқы 1000$ табудың 3-ші қадамын тура 3 минуттан кейін айтамын😍\\n\\nОсы уақытқа 3-ші қадамды қолданған адамдар ақша тауып бастады. Сен де құр қалма! Дәл қазір мына сілтеме бойынша өт:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=eights&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1938():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ТЕГІН САБАҚ 🔥 БОП ЖАТЫР\\n\\nМастер-класстағы атмосфераны сөзбен айтып жеткізу мүмкін емес. Дәл қазір мына сілтеме бойынша өт те, сен де табыс табудың нақты 7 қадамын үйреніп ал:\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=nines&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendMessageAt1939():
    global sendMessageIndex
    global chatIdsYesterday

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"МОЩНО БОП ЖАТЫР! 🚀💸\\n\\nДәл қазір мастер-класстың ?? минутына келдім. Алғашқы 1000$ табудың 3-ші қадамын тура 3 минуттан кейін айтамын😍\\n\\nОсы уақытқа 3-ші қадамды қолданған адамдар ақша тауып бастады. Сен де құр қалма! Дәл қазір мына сілтеме бойынша өт:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=tens&utm_campaign=invite\"\r\n}" % (
        chatIdsYesterday[sendMessageIndex])

    sendMessageIndex = 0

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at 18-50")

def sendToOldMessageAt2113():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2113")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2113 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"ПРЯМО САТАМЫН!😱\\n\\nҚысқасы, мен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\nСенде “Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2113")

def sendToOldMessageAt2114():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2114")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2114 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"2 МИЛЛИОН ТҰРАТЫН 43 КУРСҚА ДОСТУП АЛ😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, мына БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2114")

def sendToOldMessageAt2115():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2115")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2115 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \" SHONBAY BUSINESS SCHOOL - дан 70% ГРАНТ ҰТЫП АЛ😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, мына БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2115")

def sendToOldMessageAt2116():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2116")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2116 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"ПРЯМО САТАМЫН!😱\\n\\nҚысқасы, мен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\nСенде “Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2116")

def sendToOldMessageAt2117():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2117")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2117 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"70% ГРАНТ ҰТЫП АЛ😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2117")

def sendToOldMessageAt2118():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2118")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2118 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"2 МИЛЛИОН ТҰРАТЫН КУРСТАРҒА ДОСТУП АЛ😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, мына БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2118")

def sendToOldMessageAt2119():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2119")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2119 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"БІР МҮМКІНДІК БЕРЕМІН!😱\\n\\nМен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2119")

def sendToOldMessageAt2120():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2120")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2120 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"ШЫДАСАҢ ҒАНА ҚАЛ😱\\n\\nҚысқасы, мен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\nСенде “Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2120")

def sendToOldMessageAt2121():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2121")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2121 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"2.000.000 ТЕҢГЕ ТҰРАТЫН КУРСТАРҒА ДОСТУП АЛ 😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, мына БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2121")

def sendToOldMessageAt2122():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2122")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2122 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"ПРЯМО САТАМЫН!😱\\n\\nҚысқасы, мен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\nСенде “Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2122")

def sendToOldMessageUrl2113():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2113")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2113 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=first&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex += 1

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2113")

def sendToOldMessageUrl2114():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2114")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2114 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=second&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex += 1

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2114")

def sendToOldMessageUrl2115():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2115")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2115 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=third&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex += 1

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2115")

def sendToOldMessageUrl2116():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2116")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2116 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=fours&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex += 1

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2116")

def sendToOldMessageUrl2117():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2117")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2117 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=fives&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex += 1

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2117")

def sendToOldMessageUrl2118():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2118")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2118 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=sixes&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex += 1

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2118")

def sendToOldMessageUrl2119():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2119")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2119 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=sevens&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex += 1

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2119")

def sendToOldMessageUrl2120():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2120")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2120 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=eighth&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex += 1

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2120")

def sendToOldMessageUrl2121():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2121")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2121 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=nines&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex += 1

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2121")

def sendToOldMessageUrl2122():
    global sendMessageIndex
    global chatIdsYesterday

    print(str(sendMessageIndex)+" sendMessageIndex")

    print(str(chatIdsYesterday) + " sendToOldMessageAt2122")

    print(str(chatIdsYesterday[sendMessageIndex])+" sendToOldMessageAt2122 with sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://u.to/_lhoGg?utm_source=wh&utm_medium=tens&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    sendMessageIndex = 0

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2122")

def createGroupSecond():
    createGruopSecond()

def createGroup():
    global countCharNumber
    createGruop1(countCharNumber)

def jobsendMessageAt1850():
    sendMessageAt1850()
def jobsendMessageAt1851():
    sendMessageAt1851()
def jobsendMessageAt1852():
    sendMessageAt1852()
def jobsendMessageAt1853():
    sendMessageAt1853()
def jobsendMessageAt1854():
    sendMessageAt1854()
def jobsendMessageAt1855():
    sendMessageAt1855()
def jobsendMessageAt1856():
    sendMessageAt1856()
def jobsendMessageAt1857():
    sendMessageAt1857()
def jobsendMessageAt1858():
    sendMessageAt1858()
def jobsendMessageAt1859():
    sendMessageAt1859()

def jobsendMessageAt1910():
    sendMessageAt1910()
def jobsendMessageAt1911():
    sendMessageAt1911()
def jobsendMessageAt1912():
    sendMessageAt1912()
def jobsendMessageAt1913():
    sendMessageAt1913()
def jobsendMessageAt1914():
    sendMessageAt1914()
def jobsendMessageAt1915():
    sendMessageAt1915()
def jobsendMessageAt1916():
    sendMessageAt1916()
def jobsendMessageAt1917():
    sendMessageAt1917()
def jobsendMessageAt1918():
    sendMessageAt1918()
def jobsendMessageAt1919():
    sendMessageAt1919()

def jobsendMessageAt1930():
    sendMessageAt1930()
def jobsendMessageAt1931():
    sendMessageAt1931()
def jobsendMessageAt1932():
    sendMessageAt1932()
def jobsendMessageAt1933():
    sendMessageAt1933()
def jobsendMessageAt1934():
    sendMessageAt1934()
def jobsendMessageAt1935():
    sendMessageAt1935()
def jobsendMessageAt1936():
    sendMessageAt1936()
def jobsendMessageAt1937():
    sendMessageAt1937()
def jobsendMessageAt1938():
    sendMessageAt1938()
def jobsendMessageAt1939():
    sendMessageAt1939()

def jobsendToOldMessageAt2113():
    sendToOldMessageAt2113()
def jobsendToOldMessageAt2114():
    sendToOldMessageAt2114()
def jobsendToOldMessageAt2115():
    sendToOldMessageAt2115()
def jobsendToOldMessageAt2116():
    sendToOldMessageAt2116()
def jobsendToOldMessageAt2117():
    sendToOldMessageAt2117()
def jobsendToOldMessageAt2118():
    sendToOldMessageAt2118()
def jobsendToOldMessageAt2119():
    sendToOldMessageAt2119()
def jobsendToOldMessageAt2120():
    sendToOldMessageAt2120()
def jobsendToOldMessageAt2121():
    sendToOldMessageAt2121()
def jobsendToOldMessageAt2122():
    sendToOldMessageAt2122()

def jobsendToOldMessageUrlAt2113():
    sendToOldMessageUrl2113()
def jobsendToOldMessageUrlAt2114():
    sendToOldMessageUrl2114()
def jobsendToOldMessageUrlAt2115():
    sendToOldMessageUrl2115()
def jobsendToOldMessageUrlAt2116():
    sendToOldMessageUrl2116()
def jobsendToOldMessageUrlAt2117():
    sendToOldMessageUrl2117()
def jobsendToOldMessageUrlAt2118():
    sendToOldMessageUrl2118()
def jobsendToOldMessageUrlAt2119():
    sendToOldMessageUrl2119()
def jobsendToOldMessageUrlAt2120():
    sendToOldMessageUrl2120()
def jobsendToOldMessageUrlAt2121():
    sendToOldMessageUrl2121()
def jobsendToOldMessageUrlAt2122():
    sendToOldMessageUrl2122()

def sendFirstMessageToFilledGroup(charIdIndex):
    global chatIds

    print(str(charIdIndex)+" sendMessageIndex")
    print(str(chatIds[charIdIndex]) + "chatIds sendMessageIndex")

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"Сәлем, байланыста Қуаныш Шонбай!\\n\\nҚұттықтаймын! Сен мастер-классқа сәтті тіркелдің!🥳\\n\\nБүгінгі тегін мастер-класс сілтемесін осы топқа жіберемін. Мастер-класста көріскенше🙌🏻\"\r\n}}".format(chatIds[charIdIndex])

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIds[charIdIndex])

    print(charIdIndex)

    print("I'm working at sendFirstMessageToFilledGroup")

def changeGroupInviteLinks():
    global chatInviteLinksToday
    global chatInviteLinksYesterday
    global inviteLinksIndex
    global dataChatIds
    global dataInviteLinks
    inviteLinksIndex = 0
    global sendMessageIndex
    sendMessageIndex = 0
    global countCharNumber
    countCharNumber = 1
    global number
    number = 0
    ws.append(dataChatIds)
    ws.append(dataInviteLinks)
    wb.save(str(month)+str(day)+"data"+".xlsx")
    print(str(chatInviteLinksYesterday) + " before chatInviteLinksYesterday")
    print(str(chatInviteLinksToday) + " before chatInviteLinksToday")
    for j in chatInviteLinksToday:
        chatInviteLinksYesterday.append(j)
    print(str(chatInviteLinksToday) + " after chatInviteLinksToday")
    print(str(chatInviteLinksYesterday) + " after chatInviteLinksYesterday")
    chatInviteLinksToday.clear()
    print(str(chatInviteLinksToday) + " after clear chatInviteLinksToday")
    global chatIds
    global chatIdsYesterday
    print(str(chatIds) + " before chatIds")
    print(str(chatIdsYesterday) + " before chatIdsYesterday")
    for i in chatIds:
        chatIdsYesterday.append(i)
    print(str(chatIds) + " after chatIds")
    print(str(chatIdsYesterday) + " after chatIdsYesterday")
    chatIds.clear()
    print(str(chatIds) + " after clear chatIds")

# ChangeGroupInviteLinksTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"18"+":"+"30"), '%Y-%m-%dT%H:%M')
#
# sched.add_job(changeGroupInviteLinks, trigger='date', next_run_time=ChangeGroupInviteLinksTime)

# sched.add_job(createGruopSecond, trigger='date', next_run_time=JustOnes)
sched.add_job(createGruopSecond, 'date', run_date='2020-12-21 20:00:00')

def sendMessageAtExample():
    global sendMessageIndex
    global chatIds
    if(len(chatIds)-1 == sendMessageIndex):
        print(str(sendMessageIndex) + " sendMessageIndex")
        print(str(chatIds[sendMessageIndex]) + "chatIds sendMessageIndex")
        sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"“ИНТЕРНЕТ-МАРКЕТОЛОГ” КУРСЫН КҮНІНЕ 408 ТЕҢГЕГЕ АЛ😎🤯\\n\\nShonbay Business School ұсынған “Интернет-маркетолог” курсына қатысу енді бұрынғыдан да қол жетімді. Өйткені сенде 31 желтоқсанға дейін курсты еш пайызсыз 12 айға бөліп төлеу мүмкіндігі бар😍\\n\\nДемек, “Интернет-маркетолог” курсын қазір алу арқылы сен күнделікті білім алуға бар болғаны 408 теңге жұмсайсың🙌🏻\\n\\nКурс барысында 3 ай көлемінде сен толық циклді интернет-маркетолог атанып, айына кем дегенде 200.000 теңге табыс табу мүмкіндігіне ие боласың. Оған қоса, сені үнемі қадағалауда ұстатайтын куратор, дамушы орта мен практик спикерлер күтеді😍\\n\\nБөліп төлеу туралы толық ақпарат алу үшін дәл қазір мына сілтеме бойынша өт: 👇🏻\"\r\n}}".format(
            chatIds[sendMessageIndex])

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")
    elif(sendMessageIndex != 20000):
        print(str(sendMessageIndex) + " sendMessageIndex")
        print(str(chatIds[sendMessageIndex]) + "chatIds sendMessageIndex")
        sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"“ИНТЕРНЕТ-МАРКЕТОЛОГ” КУРСЫН КҮНІНЕ 408 ТЕҢГЕГЕ АЛ😎🤯\\n\\nShonbay Business School ұсынған “Интернет-маркетолог” курсына қатысу енді бұрынғыдан да қол жетімді. Өйткені сенде 31 желтоқсанға дейін курсты еш пайызсыз 12 айға бөліп төлеу мүмкіндігі бар😍\\n\\nДемек, “Интернет-маркетолог” курсын қазір алу арқылы сен күнделікті білім алуға бар болғаны 408 теңге жұмсайсың🙌🏻\\n\\nКурс барысында 3 ай көлемінде сен толық циклді интернет-маркетолог атанып, айына кем дегенде 200.000 теңге табыс табу мүмкіндігіне ие боласың. Оған қоса, сені үнемі қадағалауда ұстатайтын куратор, дамушы орта мен практик спикерлер күтеді😍\\n\\nБөліп төлеу туралы толық ақпарат алу үшін дәл қазір мына сілтеме бойынша өт: 👇🏻\"\r\n}}".format(
            chatIds[sendMessageIndex])

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

def sendMessageAtExampleUrl():
    global sendMessageIndex
    global chatIds

    if(len(chatIds)-1 == sendMessageIndex):
        print(str(sendMessageIndex) + " sendMessageIndex")
        print(str(chatIds[sendMessageIndex]) + "chatIds sendMessageIndex")

        sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://shonbay.school/bt\"\r\n}}".format(
            chatIds[sendMessageIndex])

        sendMessageIndex = 20000

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")
    elif(sendMessageIndex != 20000):
        print(str(sendMessageIndex) + " sendMessageIndex")
        print(str(chatIds[sendMessageIndex]) + "chatIds sendMessageIndex")

        sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"https://shonbay.school/bt\"\r\n}}".format(
            chatIds[sendMessageIndex])

        sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                               data=sendMessageAt1850.encode('utf8'))

        y = json.loads(sendMessageResponse.text.encode('utf8'))

        print(y["idMessage"])

        print(sendMessageResponse.text.encode('utf8'))

        print(sendMessageIndex)

        print("I'm working at 18-50")

        sendMessageIndex += 1
def ExampleMessageJob():
    sendMessageAtExample()

def ExampleMessageUrlJob():
    sendMessageAtExampleUrl()

def my_job(text):
    print(text, str(datetime.datetime.now()))

sched.add_job(func=my_job, args=['job running'], trigger='interval', id='job', minutes=1)

# FirstMessageTime =
    # datetime.datetime.strptime(str("15"+":"+"21"+":"+"10"), '%H:%M:%S')
# SecondMessageTime =
    # datetime.datetime.strptime(str("15"+":"+"21"+":"+"20"), '%H:%M:%S')
# ThirdMessageTime =
    # datetime.datetime.strptime(str("15"+":"+"22"+":"+"10"), '%H:%M:%S')
# FoursMessageTime =
    # datetime.datetime.strptime(str("15"+":"+"22"+":"+"20"), '%H:%M:%S')
# FivesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"16"+":"+"04"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# SixesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"16"+":"+"05"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# EightsMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"16"+":"+"06"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# SevensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"16"+":"+"07"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# NinesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"16"+":"+"08"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# TensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"16"+":"+"09"+":"+"20"), '%Y-%m-%dT%H:%M:%S')

# sched.add_job(ExampleMessageJob, trigger='cron', hour=12, minute=20, second=10)
# sched.add_job(ExampleMessageUrlJob, trigger='cron', hour=12, minute=20, second=20)
# sched.add_job(ExampleMessageJob, trigger='cron', hour=12, minute=21, second=10)
# sched.add_job(ExampleMessageUrlJob, trigger='cron', hour=12, minute=21, second=20)

# def createGroupTimely():
#     createTimelyGroup()
#
# def yesterdayChatIdsCheck():
#     print("I'm working at yesterdayChatIdsCheck")
#     if (len(chatIdsYesterday) != 0):
#         print("I'm working at yesterdayChatIdsCheck len")
#         sched.add_job(jobsendMessageAt1910, trigger='cron', hour=15, minute=29, second=30)
#         sched.add_job(jobsendMessageAt1911, trigger='cron', hour=15, minute=29, second=40)
#     # else:
#     #     print("I'm working at yesterdayChatIdsCheck not len")
#     #     changeGroupInviteLinks()
#
# sched.add_job(changeGroupInviteLinks, trigger='cron', hour=15, minute=29, second=10)
# sched.add_job(yesterdayChatIdsCheck, trigger='cron', hour=15, minute=29, second=20)

sched.add_job(jobsendMessageAt1850, trigger='cron', hour=20, minute=1, second=0)
sched.add_job(jobsendMessageAt1851, trigger='cron', hour=20, minute=2, second=0)
sched.add_job(jobsendMessageAt1852, trigger='cron', hour=20, minute=3, second=0)
sched.add_job(jobsendMessageAt1853, trigger='cron', hour=20, minute=4, second=0)
sched.add_job(jobsendMessageAt1854, trigger='cron', hour=20, minute=5, second=0)
sched.add_job(jobsendMessageAt1855, trigger='cron', hour=20, minute=6, second=0)
sched.add_job(jobsendMessageAt1856, trigger='cron', hour=20, minute=7, second=0)
sched.add_job(jobsendMessageAt1857, trigger='cron', hour=20, minute=8, second=0)
sched.add_job(jobsendMessageAt1858, trigger='cron', hour=20, minute=9, second=0)
sched.add_job(jobsendMessageAt1859, trigger='cron', hour=20, minute=10, second=0)

# sched.add_job(changeGroupInviteLinks, trigger='cron', hour=18, minute=26, second=00)

# sched.add_job(changeGroupInviteLinks, trigger='cron', hour=19, minute=00, second=00)

# sched.add_job(yesterdayChatIdsCheck, trigger='cron', hour=19, minute=0, second=30)

# sched.add_job(createTimelyGroup, trigger='cron', hour=19, minute=01, second=0)
# sched.add_job(createTimelyGroup, trigger='cron', hour=19, minute=02, second=0)
# sched.add_job(createTimelyGroup, trigger='cron', hour=19, minute=03, second=0)
# sched.add_job(createTimelyGroup, trigger='cron', hour=19, minute=04, second=0)
# sched.add_job(createTimelyGroup, trigger='cron', hour=19, minute=05, second=0)
# sched.add_job(createTimelyGroup, trigger='cron', hour=19, minute=06, second=0)
# sched.add_job(createTimelyGroup, trigger='cron', hour=19, minute=07, second=0)
# sched.add_job(createTimelyGroup, trigger='cron', hour=19, minute=08, second=0)
# sched.add_job(createTimelyGroup, trigger='cron', hour=19, minute=09, second=0)

# sched.add_job(jobsendMessageAt1910, trigger='cron', hour=19, minute=10, second=0)
# sched.add_job(jobsendMessageAt1911, trigger='cron', hour=19, minute=11, second=0)
# sched.add_job(jobsendMessageAt1912, trigger='cron', hour=19, minute=12, second=0)
# sched.add_job(jobsendMessageAt1913, trigger='cron', hour=19, minute=13, second=0)
# sched.add_job(jobsendMessageAt1914, trigger='cron', hour=19, minute=14, second=0)
# sched.add_job(jobsendMessageAt1915, trigger='cron', hour=19, minute=15, second=0)
# sched.add_job(jobsendMessageAt1916, trigger='cron', hour=19, minute=16, second=0)
# sched.add_job(jobsendMessageAt1917, trigger='cron', hour=19, minute=17, second=0)
# sched.add_job(jobsendMessageAt1918, trigger='cron', hour=19, minute=18, second=0)
# sched.add_job(jobsendMessageAt1919, trigger='cron', hour=19, minute=19, second=0)

# sched.add_job(jobsendMessageAt1930, trigger='cron', hour=19, minute=30, second=0)
# sched.add_job(jobsendMessageAt1931, trigger='cron', hour=19, minute=31, second=0)
# sched.add_job(jobsendMessageAt1932, trigger='cron', hour=19, minute=32, second=0)
# sched.add_job(jobsendMessageAt1933, trigger='cron', hour=19, minute=33, second=0)
# sched.add_job(jobsendMessageAt1934, trigger='cron', hour=19, minute=34, second=0)
# sched.add_job(jobsendMessageAt1935, trigger='cron', hour=19, minute=35, second=0)
# sched.add_job(jobsendMessageAt1936, trigger='cron', hour=19, minute=36, second=0)
# sched.add_job(jobsendMessageAt1937, trigger='cron', hour=19, minute=37, second=0)
# sched.add_job(jobsendMessageAt1938, trigger='cron', hour=19, minute=38, second=0)
# sched.add_job(jobsendMessageAt1939, trigger='cron', hour=19, minute=39, second=0)

# sched.add_job(jobsendToOldMessageAt2113, trigger='cron', hour=21, minute=13, second=0)
# sched.add_job(jobsendToOldMessageAt2114, trigger='cron', hour=21, minute=14, second=0)
# sched.add_job(jobsendToOldMessageAt2115, trigger='cron', hour=21, minute=15, second=0)
# sched.add_job(jobsendToOldMessageAt2116, trigger='cron', hour=21, minute=16, second=0)
# sched.add_job(jobsendToOldMessageAt2117, trigger='cron', hour=21, minute=17, second=0)
# sched.add_job(jobsendToOldMessageAt2118, trigger='cron', hour=21, minute=18, second=0)
# sched.add_job(jobsendToOldMessageAt2119, trigger='cron', hour=21, minute=19, second=0)
# sched.add_job(jobsendToOldMessageAt2120, trigger='cron', hour=21, minute=20, second=0)
# sched.add_job(jobsendToOldMessageAt2121, trigger='cron', hour=21, minute=21, second=0)
# sched.add_job(jobsendToOldMessageAt2122, trigger='cron', hour=21, minute=22, second=0)

# sched.add_job(jobsendToOldMessageUrlAt2113, trigger='cron', hour=21, minute=13, second=10)
# sched.add_job(jobsendToOldMessageUrlAt2114, trigger='cron', hour=21, minute=14, second=10)
# sched.add_job(jobsendToOldMessageUrlAt2115, trigger='cron', hour=21, minute=15, second=10)
# sched.add_job(jobsendToOldMessageUrlAt2116, trigger='cron', hour=21, minute=16, second=10)
# sched.add_job(jobsendToOldMessageUrlAt2117, trigger='cron', hour=21, minute=17, second=10)
# sched.add_job(jobsendToOldMessageUrlAt2118, trigger='cron', hour=21, minute=18, second=10)
# sched.add_job(jobsendToOldMessageUrlAt2119, trigger='cron', hour=21, minute=19, second=10)
# sched.add_job(jobsendToOldMessageUrlAt2120, trigger='cron', hour=21, minute=20, second=10)
# sched.add_job(jobsendToOldMessageUrlAt2121, trigger='cron', hour=21, minute=21, second=10)
# sched.add_job(jobsendToOldMessageUrlAt2122, trigger='cron', hour=21, minute=22, second=10)



#
# ChangeGroupInviteLinksTime2 = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"00"+":"+"00"), '%Y-%m-%dT%H:%M:%S')
# #
# sched.add_job(changeGroupInviteLinks, trigger='date', next_run_time=ChangeGroupInviteLinksTime2)
#
# FirstGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"00"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# SecondGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"01"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# ThirdGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"02"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# FoursGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"03"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# FivesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"04"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# SixesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"05"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# SevensGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"06"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# EighthsGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"07"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# NinesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"08"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# TensGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"09"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# #
# sched.add_job(createGroup, trigger='date', next_run_time=FirstGroupCreationDate_time)
# sched.add_job(createGroup, trigger='date', next_run_time=SecondGroupCreationDate_time)
# sched.add_job(createGroup, trigger='date', next_run_time=ThirdGroupCreationDate_time)
# sched.add_job(createGroup, trigger='date', next_run_time=FoursGroupCreationDate_time)
# sched.add_job(createGroup, trigger='date', next_run_time=FivesGroupCreationDate_time)
# sched.add_job(createGroup, trigger='date', next_run_time=SixesGroupCreationDate_time)
# sched.add_job(createGroup, trigger='date', next_run_time=SevensGroupCreationDate_time)
# sched.add_job(createGroup, trigger='date', next_run_time=EighthsGroupCreationDate_time)
# sched.add_job(createGroup, trigger='date', next_run_time=NinesGroupCreationDate_time)
# sched.add_job(createGroup, trigger='date', next_run_time=TensGroupCreationDate_time)
# # sched.add_job(createGroupSecond, trigger='date', next_run_time=ElevensGroupCreationDate_time)
# # sched.add_job(createGroupSecond, trigger='date', next_run_time=ThirdGroupCreationDate_time)
# # sched.add_job(createGroupSecond, trigger='date', next_run_time=FourteenthGroupCreationDate_time)
# # sched.add_job(createGroupSecond, trigger='date', next_run_time=FifteensGroupCreationDate_time)
#
# sFirstMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"10"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# sSecondMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"11"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# sThirdMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"12"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# sFoursMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"13"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# sFivesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"14"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# sSixesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"15"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# sSevensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"16"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# sEightsMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"17"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# sNinesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"18"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# sTensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"19"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
#
# sched.add_job(jobsendMessageAt1910, trigger='date', next_run_time=sFirstMessageTime)
# sched.add_job(jobsendMessageAt1911, trigger='date', next_run_time=sSecondMessageTime)
# sched.add_job(jobsendMessageAt1912, trigger='date', next_run_time=sThirdMessageTime)
# sched.add_job(jobsendMessageAt1913, trigger='date', next_run_time=sFoursMessageTime)
# sched.add_job(jobsendMessageAt1914, trigger='date', next_run_time=sFivesMessageTime)
# sched.add_job(jobsendMessageAt1915, trigger='date', next_run_time=sSixesMessageTime)
# sched.add_job(jobsendMessageAt1916, trigger='date', next_run_time=sSevensMessageTime)
# sched.add_job(jobsendMessageAt1917, trigger='date', next_run_time=sEightsMessageTime)
# sched.add_job(jobsendMessageAt1918, trigger='date', next_run_time=sNinesMessageTime)
# sched.add_job(jobsendMessageAt1919, trigger='date', next_run_time=sTensMessageTime)
#
# tFirstMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"30"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# tSecondMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"31"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# tThirdMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"32"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# tFoursMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"33"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# tFivesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"34"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# tSixesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"35"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# tSevensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"36"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# tEightsMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"37"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# tNinesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"38"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# tTensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"19"+":"+"39"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
#
# sched.add_job(jobsendMessageAt1930, trigger='date', next_run_time=tFirstMessageTime)
# sched.add_job(jobsendMessageAt1931, trigger='date', next_run_time=tSecondMessageTime)
# sched.add_job(jobsendMessageAt1932, trigger='date', next_run_time=tThirdMessageTime)
# sched.add_job(jobsendMessageAt1933, trigger='date', next_run_time=tFoursMessageTime)
# sched.add_job(jobsendMessageAt1934, trigger='date', next_run_time=tFivesMessageTime)
# sched.add_job(jobsendMessageAt1935, trigger='date', next_run_time=tSixesMessageTime)
# sched.add_job(jobsendMessageAt1936, trigger='date', next_run_time=tSevensMessageTime)
# sched.add_job(jobsendMessageAt1937, trigger='date', next_run_time=tEightsMessageTime)
# sched.add_job(jobsendMessageAt1938, trigger='date', next_run_time=tNinesMessageTime)
# sched.add_job(jobsendMessageAt1939, trigger='date', next_run_time=tTensMessageTime)
# #
# FirstMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"13"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
# SecondMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"14"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
# ThirdMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"15"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
# FivesMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"16"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
# FoursMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"17"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
# SixesMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"18"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
# SevensMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"19"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
# EightsMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"20"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
# NinesMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"21"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
# TensMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"22"+":"+"10"), '%Y-%m-%dT%H:%M:%S')
#
# sched.add_job(jobsendToOldMessageAt2113, trigger='date', next_run_time=FirstMessageTimeOld)
# sched.add_job(jobsendToOldMessageAt2114, trigger='date', next_run_time=SecondMessageTimeOld)
# sched.add_job(jobsendToOldMessageAt2115, trigger='date', next_run_time=ThirdMessageTimeOld)
# sched.add_job(jobsendToOldMessageAt2116, trigger='date', next_run_time=FoursMessageTimeOld)
# sched.add_job(jobsendToOldMessageAt2117, trigger='date', next_run_time=FivesMessageTimeOld)
# sched.add_job(jobsendToOldMessageAt2118, trigger='date', next_run_time=SixesMessageTimeOld)
# sched.add_job(jobsendToOldMessageAt2119, trigger='date', next_run_time=SevensMessageTimeOld)
# sched.add_job(jobsendToOldMessageAt2120, trigger='date', next_run_time=EightsMessageTimeOld)
# sched.add_job(jobsendToOldMessageAt2121, trigger='date', next_run_time=NinesMessageTimeOld)
# sched.add_job(jobsendToOldMessageAt2122, trigger='date', next_run_time=TensMessageTimeOld)
# #
# FirstMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"13"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
# SecondMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"14"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
# ThirdMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"15"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
# FoursMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"16"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
# FivesMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"17"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
# SixesMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"18"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
# SevensMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"19"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
# EightsMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"20"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
# NinesMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"21"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
# TensMessageTimeUrl = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"21"+":"+"22"+":"+"40"), '%Y-%m-%dT%H:%M:%S')
#
# sched.add_job(jobsendToOldMessageUrlAt2113, trigger='date', next_run_time=FirstMessageTimeUrl)
# sched.add_job(jobsendToOldMessageUrlAt2114, trigger='date', next_run_time=SecondMessageTimeUrl)
# sched.add_job(jobsendToOldMessageUrlAt2115, trigger='date', next_run_time=ThirdMessageTimeUrl)
# sched.add_job(jobsendToOldMessageUrlAt2116, trigger='date', next_run_time=FoursMessageTimeUrl)
# sched.add_job(jobsendToOldMessageUrlAt2117, trigger='date', next_run_time=FivesMessageTimeUrl)
# sched.add_job(jobsendToOldMessageUrlAt2118, trigger='date', next_run_time=SixesMessageTimeUrl)
# sched.add_job(jobsendToOldMessageUrlAt2119, trigger='date', next_run_time=SevensMessageTimeUrl)
# sched.add_job(jobsendToOldMessageUrlAt2120, trigger='date', next_run_time=EightsMessageTimeUrl)
# sched.add_job(jobsendToOldMessageUrlAt2121, trigger='date', next_run_time=NinesMessageTimeUrl)
# sched.add_job(jobsendToOldMessageUrlAt2122, trigger='date', next_run_time=TensMessageTimeUrl)

@app.route('/')
def index():
    global number
    number += 1
    global chatInviteLinksToday
    global chatIds
    global createdChatIds17
    global createdInviteLinks17
    global filledArrayIndex
    global inviteLinksIndex
    print(str(number)+" this is number")
    print(str(inviteLinksIndex) + " this is inviteLinksIndex")
    print(str(len(chatInviteLinksToday)) + " this is len chatInviteLinksToday")
    if number >= 256:
        if inviteLinksIndex == len(chatInviteLinksToday) - 1:
            number = 0
            chatInviteLinksToday.append(createdInviteLinks17[filledArrayIndex])
            chatIds.append(createdChatIds17[filledArrayIndex])
            sendFirstMessageToFilledGroup(inviteLinksIndex)
            if filledArrayIndex == 0:
                createGroup()
            else:
                print(str(filledArrayIndex) + " this is filledArrayIndex before")
                filledArrayIndex -= 1
                print(str(filledArrayIndex) + " this is filledArrayIndex after")
            print(str(inviteLinksIndex) + " this is inviteLinksIndex before")
            inviteLinksIndex = len(chatInviteLinksToday) - 1
            print(str(inviteLinksIndex) + " this is inviteLinksIndex after")
        else:
            number = 0
            sendFirstMessageToFilledGroup(inviteLinksIndex)
            print(str(inviteLinksIndex) + " this is inviteLinksIndex before")
            inviteLinksIndex += 1
            print(str(inviteLinksIndex) + " this is inviteLinksIndex after")
        print(str(inviteLinksIndex) + " this is inviteLinksIndex redirect")
        return redirect(chatInviteLinksToday[inviteLinksIndex])
    else:
        print(str(inviteLinksIndex) + " this is inviteLinksIndex redirect")
        if(len(chatIds) == 0):
            createGroup()
            inviteLinksIndex = 0
        return redirect(chatInviteLinksToday[inviteLinksIndex])

if __name__ == "__main__":
    sched.start()
    # app.run(debug=True, use_reloader=False)
    app.run(host="45.149.128.147",port=80, debug=True, use_reloader=False)
