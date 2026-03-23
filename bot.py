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

# --- Updated Login Logic (Method 3) ---
if os.path.exists("appstate.json"):
    with open("appstate.json", "r") as f:
        appstate = json.load(f)
    
    try:
        print("🚀 Login attempt using from_session...")
        # Naye versions mein ye sabse best tarika hai
        bot = MyBot.from_session(appstate)
        
        print("✅ BOT START HO GAYA HAI!")
        bot.listen()
        
    except Exception as e:
        print(f"❌ Login Error: {e}")
        print("Try updating your appstate.json with fresh cookies.")
else:
    print("❌ ERROR: 'appstate.json' file nahi mili!")
    
