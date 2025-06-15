import os
from enum import Enum
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

BOT_CHANNEL = int(os.getenv('BOT_CHANNEL', 0))
BOT_LOG_CHANNEL = int(os.getenv('BOT_LOG_CHANNEL', 0))

INVITE_TO_CHANNEL = int(os.getenv('INVITE_TO_CHANNEL', 0))

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./database.db')

SMTP_SEVER = os.getenv('SMTP_SEVER')
SMTP_SERVER_PORT = os.getenv('SMTP_SERVER_PORT')
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
EMAIL_FROM = os.getenv('EMAIL_FROM')


dept = ["", "BDnM", "CnD", "ED", "HOSP", "IHC", "LOGI", "PR", "RnD", "TECH"]

role = ["Executive", "Core", "LT"]
roleEmoji = ["💙", "💠", "👑"]

RoleId = [
          0, 
          int(os.getenv('BDNM_ROLE_ID', 0)),
          int(os.getenv('CND_ROLE_ID', 0)),
          int(os.getenv('ED_ROLE_ID', 0)),
          int(os.getenv('HOSP_ROLE_ID', 0)),
          int(os.getenv('IHC_ROLE_ID', 0)),
          int(os.getenv('LOGI_ROLE_ID', 0)),
          int(os.getenv('PR_ROLE_ID', 0)),
          int(os.getenv('RND_ROLE_ID', 0)),
          int(os.getenv('TECH_ROLE_ID', 0))
        ]

class Level(Enum):
    LT = int(os.getenv('LT_ROLE_ID', 0))
    CORE = int(os.getenv('CORE_ROLE_ID', 0))
    EXEC = int(os.getenv('EXEC_ROLE_ID', 0))

MODE = 0  # 0 = Executive, 1 = Core, 2 = LT

def get_mode():
    """Get the current mode for direct roles."""
    return MODE

def set_mode(new_mode: int):
    """Set the mode for direct roles."""
    global MODE
    if new_mode in [0, 1, 2]:
        MODE = new_mode
    else:
        raise ValueError("Invalid mode. Must be 0 (Executive), 1 (Core), or 2 (LT).")
    
    print(f"Mode set to {MODE} ({role[MODE]})")