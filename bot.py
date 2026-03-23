import json
from fbchat import Client
from fbchat.models import Message

class MyBot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None,
                  thread_id=None, thread_type=None, **kwargs):

        if author_id != self.uid:
            msg = message_object.text.lower() if message_object.text else ""

            # Simple commands
            if "hi" in msg:
                self.send(Message(text="Hello 👋"), thread_id=thread_id, thread_type=thread_type)

            elif "help" in msg:
                self.send(Message(text="Type: hi / time / owner"), thread_id=thread_id, thread_type=thread_type)

            elif "owner" in msg:
                self.send(Message(text="Bot Owner 👑"), thread_id=thread_id, thread_type=thread_type)

            else:
                self.send(Message(text="I am active 🤖"), thread_id=thread_id, thread_type=thread_type)


# Load appstate
with open("appstate.json", "r") as f:
    appstate = json.load(f)

# Login using session cookies
bot = MyBot(session_cookies=appstate)

print("🚀 BOT RUNNING SUCCESSFULLY...")
bot.listen()
