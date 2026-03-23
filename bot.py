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

# --- Login Logic Fix ---
if os.path.exists("appstate.json"):
    with open("appstate.json", "r") as f:
        appstate = json.load(f)
    
    # FIX: Yahan 'session_cookies=' likhne ki zaroorat nahi hai
    # Sirf appstate ko pass karein ya Client.from_session use karein
    try:
        # Kuch versions mein ye kaam karta hai:
        bot = MyBot(session_cookies=appstate) 
    except TypeError:
        # Agar upar wala fail ho, toh ye naya tareeka hai:
        bot = MyBot("", "", session_cookies=appstate)
    
    # Agar phir bhi error de, toh niche wala line use karein:
    # bot = MyBot.from_session(appstate)

    print("🚀 BOT START HO RAHA HAI...")
    bot.listen()
else:
    print("❌ ERROR: appstate.json file nahi mili!")
    
