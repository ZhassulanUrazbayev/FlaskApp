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

createdChatIds = ["77764497092-1607055302@g.us","77764497092-1607055242@g.us","77764497092-1607055182@g.us","77764497092-1607055122@g.us","77764497092-1607055063@g.us","77764497092-1607055002@g.us","77764497092-1607054942@g.us","77764497092-1607054883@g.us","77764497092-1607054824@g.us","77764497092-1607054764@g.us"]
createdInviteLinks = ["https://chat.whatsapp.com/IUEDsa1eLRcCavmHqLs38c","https://chat.whatsapp.com/H09cgpDt9yuGhlMxtcGPJm","https://chat.whatsapp.com/LwWNwGEWi4M2Uyq1yBQknp","https://chat.whatsapp.com/KM1UTVXwNLL58fIBGHHqp4","https://chat.whatsapp.com/FYjHY4yMKCnIM8DFbOmF9S","https://chat.whatsapp.com/CwaHSZBGwFtDCTlNwb48hy","https://chat.whatsapp.com/EzPJ1OvCV6eInsXPPuI7on","https://chat.whatsapp.com/I9BhGRcAVIiBIqiNo4clcE","https://chat.whatsapp.com/LiJn43o92SK3zf97cUSHc5","https://chat.whatsapp.com/BJTh3b8gaSmJ2ECzJAzVrw"]

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
        # global chatId
        global countCharNumber
        # chatId = y['chatId']
        countCharNumber = chatNumber + 1
    else:
        print("Suka bliat zhasamait minau CreateGroup")


def createGruopSecond():
    global whatsappId
    global chatIds
    global chatInviteLinksToday
    global createdChatIds
    global createdInviteLinks
    for i in createdChatIds:
        chatIds.append(i)
    for j in createdInviteLinks:
        chatInviteLinksToday.append(j)



def sendMessageAt1850():
    global sendMessageIndex
    global chatIds

    print(str(sendMessageIndex)+" sendMessageIndex")

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ЖАЛПЫ ҚҰНЫ 1.000.000 тг ТҰРАТЫН САБАҚТЫ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “Интернет-маркетинг арқылы алғашқы 1000$ табудың нақты 7 қадамы” атты мастер-классы бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇 https://u.to/jqPgGQ?utm_source=wh&utm_medium=first&utm_campaign=invite\"\r\n}" % (
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
    global chatIds

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"2 САҒАТ КИНО КӨРГЕНШЕ, ҚУАНЫШ ШОНБАЙДАН ТЕГІН БІЛІМ АЛ😍\\n\\nСен бүгін Алматы уақыты бойынша 19.00-21.00 аралығында не істейсің?Әрине, Қуаныш Шонбайдың “Интернет-маркетинг арқылы алғашқы 1000$ табудың нақты 7 қадамы” атты ТЕГІН мастер-классын көресің 💸❤\\n\\nАл қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥 https://u.to/jqPgGQ?utm_source=wh&utm_medium=second&utm_campaign=invite\"\r\n}" % (
        createdChatIds[sendMessageIndex])

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
    global chatIds

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ОСЫ ГРУППДАҒЫ БАРЛЫҚ АДАМДЫ ӨЗ ҮЙІМЕ ҚОНАҚҚА ШАҚЫРАМЫН😍🔥\\n\\nЕлдің бәрі тегін сабаққа кіріп, құнды білім алып жатыр. Ал сен әлі не істеріңді білмей отырсың 😑👎🏻\\n\\nЕлден қалмай, сен де қатыс. Дәл қазір мына сілтеме бойынша өт https://u.to/jqPgGQ?utm_source=wh&utm_medium=third&utm_campaign=invite\"\r\n}" % (
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
    global chatIds

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ҚҰНЫ 1.000.000 тг ТҰРАТЫН САБАҚТЫ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “Интернет-маркетинг арқылы алғашқы 1000$ табудың нақты 7 қадамы” атты мастер-классы Алматы қаласы бойынша бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇 https://u.to/jqPgGQ?utm_source=wh&utm_medium=fours&utm_campaign=invite\"\r\n}" % (
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
    global chatIds

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ОСЫ ГРУППДАҒЫ БАРЛЫҚ АДАМДЫ ҚОНАҚҚА ШАҚЫРАМЫН😍🔥\\n\\nБірақ карантин болғандықтан, үйіме онлайн қонақ боласыз. Келгендерге арнайы бонус-сарқыт дайындап қойдым. Бүгін Алматы уақыты бойынша 19.00-да күтем. Кешікпеңіз🥳🔥 https://u.to/jqPgGQ?utm_source=wh&utm_medium=fives&utm_campaign=invite\\n\\n(С) ҚУАНЫШ ШОНБАЙ\"\r\n}" % (
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
    global chatIds

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"2 САҒАТЫҢДЫ КИНОҒА ҚҰРТҚАНША, ҚУАНЫШ ШОНБАЙДАН ТЕГІН БІЛІМ АЛ😍\\n\\nБүгін Алматы уақыты бойынша 19.00-21.00 аралығында не істейсің? Әрине, Қуаныш Шонбайдың “Интернет-маркетинг арқылы алғашқы 1000$ табудың нақты 7 қадамы” атты ТЕГІН мастер-классын көресің 💸\\n\\nДәл қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sixes&utm_campaign=invite\"\r\n}" % (
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
    global chatIds

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ЖАЛПЫ ҚҰНЫ 1.000.000 тг ТҰРАТЫН БІЛІМДІ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “Интернет-маркетинг арқылы алғашқы 1000$ табудың нақты 7 қадамы” атты мастер-классы бүгін Алматы уақыты бойынша 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=sevens&utm_campaign=invite\"\r\n}" % (
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
    global chatIds

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ҚУАНЫШ ШОНБАЙДАН ТЕГІН САБАҚ😍\\n\\nҚуаныш Шонбайдың “Интернет-маркетинг арқылы алғашқы 1000$ табудың нақты 7 қадамы” атты мастер-классы Алматы қаласы бойынша бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=eights&utm_campaign=invite\"\r\n}" % (
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
    global chatIds

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"2 САҒАТЫҢДЫ КИНОҒА ҚҰРТҚАНША, ҚУАНЫШ ШОНБАЙДАН БІЛІМ АЛ 😍\\n\\nАлматы уақыты бойынша 19.00-21.00 аралығында не істейсің? Әрине, Қуаныш Шонбайдың “Интернет-маркетинг арқылы алғашқы 1000$ табудың нақты 7 қадамы” атты ТЕГІН мастер-классын көресің 💸\\n\\nТура қазір не істейтініңді білесің бе? Мына сілтеме бойынша өтіп, ТЕГІН бонустарға ие боласың😍🔥\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=nines&utm_campaign=invite\"\r\n}" % (
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
    global chatIds

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ЖАЛПЫ ҚҰНЫ 1.000.000 тг ТҰРАТЫН САБАҚТЫ ТЕГІН АЛ 😍\\n\\nҚуаныш Шонбайдың “Интернет-маркетинг арқылы алғашқы 1000$ табудың нақты 7 қадамы” атты мастер-классы бүгін 19.00-де өтеді. Тегін мастер-классқа қатысу үшін мына сілтеме бойынша өт: 👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=tens&utm_campaign=invite\"\r\n}" % (
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

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"МОЩНО БОП ЖАТЫР! 🚀💸\\n\\nДәл қазір мастер-класстың ?? минутына келдім. Алғашқы 1000$ табудың 3-ші қадамын тура 3 минуттан кейін айтамын😍\\n\\nОсы уақытқа 3-ші қадамды қолданған адамдар ақша тауып бастады. Сен де құр қалма! Дәл қазір мына сілтеме бойынша өт:👇\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=first&utm_campaign=invite\"\r\n}" % (
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

    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"ТЕГІН САБАҚ 🔥 БОП ЖАТЫР\\n\\nМастер-класстағы атмосфераны сөзбен айтып жеткізу мүмкін емес🤩Дәл қазір мына сілтеме бойынша өт те, сен де табыс табудың нақты 7 қадамын үйреніп ал:\\n\\nhttps://u.to/jqPgGQ?utm_source=wh&utm_medium=nines&utm_campaign=invite\"\r\n}" % (
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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"ПРЯМО САТАМЫН!😱\\n\\nҚысқасы, мен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\nСенде “Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=first&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex +=1

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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"2 МИЛЛИОН ТҰРАТЫН 43 КУРСҚА ДОСТУП АЛ😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, мына БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=second&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \" SHONBAY BUSINESS SCHOOL - дан 70% ГРАНТ ҰТЫП АЛ😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, мына БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=third&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"ПРЯМО САТАМЫН!😱\\n\\nҚысқасы, мен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\nСенде “Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=fours&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"70% ГРАНТ ҰТЫП АЛ😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=fives&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"2 МИЛЛИОН ТҰРАТЫН КУРСТАРҒА ДОСТУП АЛ😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, мына БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=sixes&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"БІР МҮМКІНДІК БЕРЕМІН!😱\\n\\nМен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=sevens&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"ШЫДАСАҢ ҒАНА ҚАЛ😱\\n\\nҚысқасы, мен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\nСенде “Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=eighth&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"2.000.000 ТЕҢГЕ ТҰРАТЫН КУРСТАРҒА ДОСТУП АЛ 😍🔥\\n\\n“Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға 72 сағат бар 🚀\\n\\nҚазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалғанын 72 сағат ішінде төлесең, мына БОНУСТАРДЫ аласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=nines&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex += 1

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

    sendMessageAt1850 = "{{\r\n\t\"chatId\": \"{}\",\r\n\t\"message\": \"ПРЯМО САТАМЫН!😱\\n\\nҚысқасы, мен қазір прямо сатамын. Продажаға көнбеймін десең, сразу шығып кетсең болады. Қаламын десең, саған 🔥 бонустар беремін👇\\n\\nСенде “Интернет-маркетолог” курсының VIP пакетін ГАРАНТИЯМЕН алуға тура 72 сағат бар 🚀\\n\\nДәл қазір 15.000 теңге көлемінде алдын ала төлем жасап, орныңды сақтап қой! Қалған сомманы 72 сағат ішінде төлесең, мына БОНУСТАРҒА ие боласың:\\n\\n✅ Shonbay Online университетінің құны 2 млн теңге тұратын 43 онлайн курсына 1 жылдық доступ аласың\\n\\n✅ Shonbay Business School-дың 70% грантына еш іріктеусіз ие боласың\\n\\n✅ Ал, ең бастысы, ГАРАНТИЯ бар. 3 айлық оқудан кейін проектің болмаса, біз саған оқу ақысын 100% қайтарып береміз\\n\\nРовно 3 секундтан кейін 15 VIP пакетке орын ашам. Үлгерсең, үлгердің, үлгермесең, қалдың! Сондықтан, тезірек мына сілтеме бойынша өт👇\\n\\nhttps://u.to/_lhoGg?utm_source=wh&utm_medium=tens&utm_campaign=application\"\r\n}}".format(chatIdsYesterday[sendMessageIndex])

    sendMessageIndex = 0

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatIdsYesterday[sendMessageIndex])

    print(sendMessageIndex)

    print("I'm working at sendToOldMessageAt2122")

def createGroupSecond():
    global countCharNumber
    createGruopSecond(countCharNumber)

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

# FirstGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# SecondGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# ThirdGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# FoursGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# FivesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# SixesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# SevensGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# EighthsGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# NinesGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
# TensGroupCreationDate_time = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"23"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
#
# sched.add_job(createGroupSecond, trigger='date', next_run_time=FirstGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=SecondGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=ThirdGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=FoursGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=FivesGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=SixesGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=SevensGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=EighthsGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=NinesGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=TensGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=ElevensGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=ThirdGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=FourteenthGroupCreationDate_time)
# sched.add_job(createGroupSecond, trigger='date', next_run_time=FifteensGroupCreationDate_time)

JustOnes = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"12"+":"+"53"+":"+"10"), '%Y-%m-%dT%H:%M:%S')

sched.add_job(createGruopSecond, trigger='date', next_run_time=JustOnes)

FirstMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"12"+":"+"53"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
SecondMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"12"+":"+"54"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
ThirdMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"12"+":"+"55"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
FoursMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"12"+":"+"56"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
FivesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"12"+":"+"57"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
SixesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"12"+":"+"58"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
EightsMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"12"+":"+"59"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
SevensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"00"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
NinesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"01"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
TensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"02"+":"+"20"), '%Y-%m-%dT%H:%M:%S')

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

ChangeGroupInviteLinksTime2 = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"03"+":"+"10"), '%Y-%m-%dT%H:%M:%S')

sched.add_job(changeGroupInviteLinks, trigger='date', next_run_time=ChangeGroupInviteLinksTime2)

sFirstMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"03"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
sSecondMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"04"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
sThirdMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"05"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
sFoursMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"06"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
sFivesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"07"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
sSixesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"08"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
sSevensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"09"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
sEightsMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"10"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
sNinesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"11"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
sTensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"12"+":"+"20"), '%Y-%m-%dT%H:%M:%S')

sched.add_job(jobsendMessageAt1910, trigger='date', next_run_time=sFirstMessageTime)
sched.add_job(jobsendMessageAt1911, trigger='date', next_run_time=sSecondMessageTime)
sched.add_job(jobsendMessageAt1912, trigger='date', next_run_time=sThirdMessageTime)
sched.add_job(jobsendMessageAt1913, trigger='date', next_run_time=sFoursMessageTime)
sched.add_job(jobsendMessageAt1914, trigger='date', next_run_time=sFivesMessageTime)
sched.add_job(jobsendMessageAt1915, trigger='date', next_run_time=sSixesMessageTime)
sched.add_job(jobsendMessageAt1916, trigger='date', next_run_time=sSevensMessageTime)
sched.add_job(jobsendMessageAt1917, trigger='date', next_run_time=sEightsMessageTime)
sched.add_job(jobsendMessageAt1918, trigger='date', next_run_time=sNinesMessageTime)
sched.add_job(jobsendMessageAt1919, trigger='date', next_run_time=sTensMessageTime)

tFirstMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"13"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
tSecondMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"14"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
tThirdMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"15"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
tFoursMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"16"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
tFivesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"17"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
tSixesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"18"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
tSevensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"19"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
tEightsMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"20"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
tNinesMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"21"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
tTensMessageTime = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"22"+":"+"20"), '%Y-%m-%dT%H:%M:%S')

sched.add_job(jobsendMessageAt1930, trigger='date', next_run_time=tFirstMessageTime)
sched.add_job(jobsendMessageAt1931, trigger='date', next_run_time=tSecondMessageTime)
sched.add_job(jobsendMessageAt1932, trigger='date', next_run_time=tThirdMessageTime)
sched.add_job(jobsendMessageAt1933, trigger='date', next_run_time=tFoursMessageTime)
sched.add_job(jobsendMessageAt1934, trigger='date', next_run_time=tFivesMessageTime)
sched.add_job(jobsendMessageAt1935, trigger='date', next_run_time=tSixesMessageTime)
sched.add_job(jobsendMessageAt1936, trigger='date', next_run_time=tSevensMessageTime)
sched.add_job(jobsendMessageAt1937, trigger='date', next_run_time=tEightsMessageTime)
sched.add_job(jobsendMessageAt1938, trigger='date', next_run_time=tNinesMessageTime)
sched.add_job(jobsendMessageAt1939, trigger='date', next_run_time=tTensMessageTime)

FirstMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"23"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
SecondMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"24"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
ThirdMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"25"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
FivesMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"26"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
FoursMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"27"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
SixesMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"28"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
SevensMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"29"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
EightsMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"30"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
NinesMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"31"+":"+"20"), '%Y-%m-%dT%H:%M:%S')
TensMessageTimeOld = datetime.datetime.strptime(str(year+"-"+month+"-"+day+"T"+"13"+":"+"32"+":"+"20"), '%Y-%m-%dT%H:%M:%S')

sched.add_job(jobsendToOldMessageAt2113, trigger='date', next_run_time=FirstMessageTimeOld)
sched.add_job(jobsendToOldMessageAt2114, trigger='date', next_run_time=SecondMessageTimeOld)
sched.add_job(jobsendToOldMessageAt2115, trigger='date', next_run_time=ThirdMessageTimeOld)
sched.add_job(jobsendToOldMessageAt2116, trigger='date', next_run_time=FoursMessageTimeOld)
sched.add_job(jobsendToOldMessageAt2117, trigger='date', next_run_time=FivesMessageTimeOld)
sched.add_job(jobsendToOldMessageAt2118, trigger='date', next_run_time=SixesMessageTimeOld)
sched.add_job(jobsendToOldMessageAt2119, trigger='date', next_run_time=SevensMessageTimeOld)
sched.add_job(jobsendToOldMessageAt2120, trigger='date', next_run_time=EightsMessageTimeOld)
sched.add_job(jobsendToOldMessageAt2121, trigger='date', next_run_time=NinesMessageTimeOld)
sched.add_job(jobsendToOldMessageAt2122, trigger='date', next_run_time=TensMessageTimeOld)

@app.route('/')
def index():
    global number
    number += 1
    global chatInviteLinksToday
    global inviteLinksIndex
    print(str(number)+" this is number")
    if number >= 256:
            if inviteLinksIndex == len(chatInviteLinksToday) - 1:
                number = 0
                inviteLinksIndex = inviteLinksIndex
            else:
                number = 0
                inviteLinksIndex += 1
            return redirect(chatInviteLinksToday[inviteLinksIndex])
    else:
        return redirect(chatInviteLinksToday[inviteLinksIndex])

if __name__ == "__main__":
    sched.start()
    # app.run(debug=True, use_reloader=False)
    app.run(host="45.149.128.147",port=80, debug=True, use_reloader=False)
