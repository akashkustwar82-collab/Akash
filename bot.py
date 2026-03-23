import json
import os
from fbchat_muqit import Client, Message

class MyBot(Client):
    def onMessage(self, mid=None, author_id=None, message_object=None,
                  thread_id=None, thread_type=None, **kwargs):

        if author_id != self.uid:
            msg = message_object.text.lower() if message_object.text else ""

            if "hi" in msg:
                self.send(Message(text="Hello 👋"), thread_id=thread_id, thread_type=thread_type)
            elif "help" in msg:
                self.send(Message(text="Type: hi / time / owner"), thread_id=thread_id, thread_type=thread_type)
            elif "owner" in msg:
                self.send(Message(text="Bot Owner 👑"), thread_id=thread_id, thread_type=thread_type)
            else:
                self.send(Message(text="I am active 😍"), thread_id=thread_id, thread_type=thread_type)

# --- Updated Login Logic ---
if os.path.exists("appstate.json"):
    with open("appstate.json", "r") as f:
        appstate = json.load(f)
    
    # Method 1: Kuch versions mein seedha dictionary pass karni hoti hai
    try:
        print("Trying Method 1...")
        bot = MyBot("", "", session_cookies=appstate)
    except TypeError:
        # Method 2: Agar keyword accept nahi kar raha, toh manual set karenge
        print("Method 1 failed, trying Method 2...")
        bot = MyBot("", "")
        bot.set_session(appstate)

    print("🚀 BOT START HO RAHA HAI...")
    bot.listen()
else:
    print("❌ ERROR: 'appstate.json' file nahi mili!")
    
