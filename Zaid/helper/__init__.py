import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Zaid"])

async def join(client):
    try:
        await client.join_chat("II_PROFESSOR_READY_4_FUCKING_Il")
    except BaseException:
        pass
