import json
from fbchat import Client, ThreadType

# CONFIG
THREAD_ID = "1729820384667780"  # Replace with your Group ID
LOCKED_NAME = "शिवराज मौलाना ओर अंशु मीठा की अप्पी का आशिक ध्रुव बदमाश इंटर "
APPSTATE_FILE = "appstate.json"

class GroupLockBot(Client):
    def onTitleChange(self, mid=None, author_id=None, new_title=None, 
                      thread_id=None, thread_type=ThreadType.GROUP, **kwargs):
        
        if thread_id == THREAD_ID and new_title != LOCKED_NAME:
            try:
                self.changeThreadTitle(LOCKED_NAME, thread_id=THREAD_ID, thread_type=ThreadType.GROUP)
            except Exception as e:
                print(f"Error: {e}")

# Load AppState
with open(APPSTATE_FILE, "r") as f:
    appstate = json.load(f)

# Start Bot
bot = GroupLockBot("", "", session_cookies=appstate)
bot.changeThreadTitle(LOCKED_NAME, thread_id=THREAD_ID, thread_type=ThreadType.GROUP)
bot.listen()
