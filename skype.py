from skpy import Skype, SkypeEventLoop, SkypeNewMessageEvent, SkypeAuthException

class SkypePing(SkypeEventLoop):
    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent) \
          and not event.msg.userId == self.userId \
          and "ping" in event.msg.content:
            event.msg.chat.sendMsg("Pong!")

sk = Skype(connect=False)
sk.conn.setTokenFile(".tokens-app")
try:
    print("Token ready!")
    sk.conn.readToken()
except SkypeAuthException:
    username = input("Username: ")
    password = input("Password: ")
    sk.conn.setUserPwd(username, password)
    sk.conn.getSkypeToken()


ping = SkypePing(tokenFile=".tokens-app", autoAck=True)
ping.loop()


