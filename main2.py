from flask import Flask, redirect

app = Flask(__name__)

number = 0

chatInviteLinkIndex = 0

chatInviteLinks = ["https://yandex.kz/", "https://www.google.com/"]

@app.route('/')
def index():
    global number
    number +=1
    global chatInviteLinkIndex
    if number >= 256:
        if chatInviteLinkIndex == len(chatInviteLinks)-1:
            chatInviteLinkIndex = chatInviteLinkIndex
        else:
            chatInviteLinkIndex += 1
        return redirect(chatInviteLinks[chatInviteLinkIndex])
    else:
        return redirect(chatInviteLinks[chatInviteLinkIndex])

if __name__ == "__main__":
    app.run(host="45.149.128.147",port=80)