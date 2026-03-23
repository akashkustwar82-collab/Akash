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

# --- Sabse Simple Login Logic ---
if os.path.exists("appstate.json"):
    with open("appstate.json", "r") as f:
        appstate = json.load(f)
    
    try:
        print("🔄 Logging in with Session Cookies...")
        
        # Method: Khali email/pass ke saath appstate pass karna
        bot = MyBot("", "", session_cookies=appstate)
        
        print("🚀 BOT RUNNING SUCCESSFULLY...")
        bot.listen()
        
    except Exception as e:
        print(f"❌ Login Failed: {e}")
        print("💡 Tip: Agar ye error keyword 'session_cookies' ki hai, toh niche wala try karein.")
        
        # Agar upar wala fail ho (keyword error), toh bina keyword ke pass karein:
        try:
            bot = MyBot("", "", appstate)
            bot.listen()
        except:
            print("Fatal Error: Please check library version or appstate format.")
else:
    print("❌ ERROR: 'appstate.json' nahi mili!")
    
