from fbchat import Client
import json

# 🔧 Load config
with open("config.json") as f:
    config = json.load(f)

PREFIX = config["prefix"]
ADMINS = config["admins"]
GROUP_NAME = config["group_name"]
LOCK_NAME = config["lock_name"]
LOCK_NICK = config["lock_nick"]
AUTO_REPLY = config["auto_reply"]

class MyBot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        global GROUP_NAME, LOCK_NAME, LOCK_NICK

        if author_id == self.uid:
            return

        if message_object.text:
            msg = message_object.text.lower()

            # 🔹 AUTO REPLY
            if AUTO_REPLY and "hello" in msg:
                self.sendMessage("Hi 👋 I am bot", thread_id=thread_id, thread_type=thread_type)

            # ❌ Only admins
            if author_id not in ADMINS:
                return

            # PREFIX check
            if not any(msg.startswith(p) for p in PREFIX):
                return

            cmd = msg[1:]

            # 🔥 HELP
            if cmd == "help":
                self.sendMessage(
                    "🔥 COMMANDS 🔥\n"
                    "!setname NAME\n"
                    "!lockname / unlockname\n"
                    "!setnick NAME\n"
                    "!locknick / unlocknick\n"
                    "!addadmin UID\n"
                    "!help",
                    thread_id=thread_id,
                    thread_type=thread_type
                )

            # 🔹 SET NAME
            elif cmd.startswith("setname"):
                name = message_object.text.split(" ",1)[1]
                GROUP_NAME = name
                self.changeThreadTitle(name, thread_id=thread_id, thread_type=thread_type)

            # 🔒 LOCK NAME
            elif cmd == "lockname":
                LOCK_NAME = True

            elif cmd == "unlockname":
                LOCK_NAME = False

            # 🔹 SET NICK
            elif cmd.startswith("setnick"):
                nick = message_object.text.split(" ",1)[1]
                self.changeNickname(nick, user_id=author_id, thread_id=thread_id, thread_type=thread_type)

            # 🔒 LOCK NICK
            elif cmd == "locknick":
                LOCK_NICK = True

            elif cmd == "unlocknick":
                LOCK_NICK = False

            # ➕ ADD ADMIN
            elif cmd.startswith("addadmin"):
                new_admin = message_object.text.split(" ",1)[1]
                ADMINS.append(new_admin)
                self.sendMessage("✅ Admin Added", thread_id=thread_id, thread_type=thread_type)

    # 🔒 AUTO NAME LOCK
    def onTitleChange(self, author_id, new_title, thread_id, thread_type, **kwargs):
        if LOCK_NAME and new_title != GROUP_NAME:
            self.changeThreadTitle(GROUP_NAME, thread_id=thread_id, thread_type=thread_type)

    # 🔒 AUTO NICK LOCK
    def onNicknameChange(self, author_id, changed_for, new_nickname, thread_id, thread_type, **kwargs):
        if LOCK_NICK:
            self.changeNickname("LOCKED 😎", user_id=changed_for, thread_id=thread_id, thread_type=thread_type)

    # 🚨 Anti-kick alert
    def onPersonRemoved(self, mid, removed_id, author_id, thread_id, thread_type, **kwargs):
        self.sendMessage("⚠️ Someone removed!", thread_id=thread_id, thread_type=thread_type)


# 🔑 LOGIN
with open("appstate.json") as f:
    appstate = json.load(f)

bot = MyBot(None, None)
bot.setSession(appstate)

print("🚀 ULTIMATE BOT RUNNING...")
bot.listen()
