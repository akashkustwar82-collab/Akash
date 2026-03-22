"""
Messenger Group Name Lock Bot (Educational Example)
---------------------------------------------------
This script uses the fbchat library to:
1. Set a specific group name.
2. Monitor the group for name changes.
3. Automatically change it back (lock the name).

Requirements:
pip install fbchat

NOTE:
- Use responsibly and follow Facebook/Messenger platform rules.
- Your account must have permission to change the group name.
"""

from fbchat import Client, ThreadType
from fbchat.models import *
import time

# ==== CONFIG ====
EMAIL = "your_facebook_email"
PASSWORD = "your_facebook_password"
THREAD_ID = "GROUP_THREAD_ID"
LOCKED_NAME = "My Locked Group Name"

CHECK_INTERVAL = 10  # seconds


class GroupLockBot(Client):
    def onMessage(self, mid=None, author_id=None, message_object=None,
                  thread_id=None, thread_type=ThreadType.USER, **kwargs):
        # Ignore bot's own messages
        if author_id == self.uid:
            return

        if thread_id == THREAD_ID:
            try:
                info = self.fetchThreadInfo(thread_id)[thread_id]
                current_name = info.name

                if current_name != LOCKED_NAME:
                    print("Group name changed! Resetting...")
                    self.changeThreadTitle(LOCKED_NAME, thread_id=THREAD_ID, thread_type=ThreadType.GROUP)

            except Exception as e:
                print("Error:", e)


def main():
    print("Starting Messenger Group Lock Bot...")
    bot = GroupLockBot(EMAIL, PASSWORD)

    # Set the name initially
    try:
        bot.changeThreadTitle(LOCKED_NAME, thread_id=THREAD_ID, thread_type=ThreadType.GROUP)
        print("Group name set and locked.")
    except Exception as e:
        print("Failed to set group name:", e)

    while True:
        try:
            bot.listen()
        except Exception as e:
            print("Reconnect error:", e)
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
