import os
import json
import sys
from fbchat import Client
from fbchat.models import *

# --- CONFIGURATION ---
# Render ke Environment Variables se values lega
GROUP_ID = os.environ.get("GROUP_ID")
LOCKED_NAME = os.environ.get("1729820384667780", "Bot Secured Group")
LOCKED_NICKNAME = os.environ.get("LOCKED_शिवराज मौलाना ओर अंशु मीठा की अप्पी का आशिक ध्रुव बदमाश", "Verified User")

class GroupLockBot(Client):
    def onThreadNameChange(self, author_id, new_name, thread_id, thread_type, **kwargs):
        # Agar koi naam badle aur wo bot khud na ho
        if thread_id == GROUP_ID and author_id != self.uid:
            if new_name != LOCKED_NAME:
                print(f"⚠️ Name change detected by {author_id}. Reverting...")
                self.changeThreadName(LOCKED_NAME, thread_id=GROUP_ID, thread_type=ThreadType.GROUP)

    def onNicknameChange(self, author_id, changed_for, new_nickname, thread_id, thread_type, **kwargs):
        # Agar koi nickname badle aur wo bot na ho
        if thread_id == GROUP_ID and author_id != self.uid:
            if new_nickname != LOCKED_NICKNAME:
                print(f"⚠️ Nickname change detected for {changed_for}. Reverting...")
                self.changeNickname(LOCKED_NICKNAME, changed_for, thread_id=GROUP_ID, thread_type=ThreadType.GROUP)

# --- BOT INITIALIZATION ---

appstate_raw = os.environ.get("APPSTATE")

if not appstate_raw:
    print("❌ ERROR: APPSTATE variable missing in Render settings!")
    sys.exit(1)

if not GROUP_ID:
    print("❌ ERROR: GROUP_ID variable missing in Render settings!")
    sys.exit(1)

try:
    # JSON string ko dictionary mein convert karna
    session_cookies = json.loads(appstate_raw)
    
    # Login process (Bina password ke)
    # Note: Kuch forks mein dummy strings "" zaruri hoti hain
    bot = GroupLockBot("dummy@email.com", "dummy_password", session_cookies=session_cookies)
    
    print("✅ Login Successful! Bot is now watching the group.")
    
    # Start listening for changes
    bot.listen()

except Exception as e:
    print(f"❌ Login Failed or Session Expired: {e}")
    print("Tip: Check if your AppState JSON is valid and not expired.")
          
