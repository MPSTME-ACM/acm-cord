import re
from db import add_member
from config import get_mode, role, dept
from discord import Invite
from emailUtil import sendMail

async def registerController(bot_channel, invite_channel, deptId: int, email: str, name: str):
    if deptId is None or email is None or name is None:
        await bot_channel.send("Please provide all required parameters: `!register <deptId> <email> <name>`")
        return
    if deptId < 1 or deptId > 9:
        await bot_channel.send("Invalid department ID. Please choose a number between 1 and 9.")
        return
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        await bot_channel.send("Invalid email format. Please provide a valid email address.")
        return
    if not name or len(name) < 2:
        await bot_channel.send("Invalid name. Please provide a name with at least 2 characters.")
        return
    
    mode = get_mode()

    invite_link: Invite = await invite_channel.create_invite(max_uses=2, unique=True, reason=f"Invite {name} with email {email} to department {deptId} as {role[mode]}", max_age=604800)

    add_member(email, name, deptId, mode, invite_link.url)

    await bot_channel.send(f"Registered `{name}` as `{role[mode]}` for `{dept[deptId]}` with email id: `{email}` and the unique link generated for them is: \n`{invite_link.url}`")

    sendMail(name, email, invite_link.url, dept[deptId], role[mode])