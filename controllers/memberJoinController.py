import discord
from config import Level, RoleId, roleEmoji, dept
from db import get_member_by_invite

async def memberJoinController(member: discord.Member, bot_id: int):
    invites = await member.guild.invites()
    used_invite: discord.Invite | None = None

    for invite in invites:
        if invite.inviter.id == bot_id and invite.uses == 1:
            used_invite = invite
            break
    
    await used_invite.delete(reason=f"Used by {member.name} to join the server.")

    dbMember = get_member_by_invite(used_invite.url)

    await assignDefaultRole(member, dbMember.role)

    if dbMember:
        await member.edit(nick=f"[{roleEmoji[dbMember.role]} {dept[dbMember.department_id]}] {dbMember.name}")
        role_id = RoleId[dbMember.department_id]
        roleObj = discord.utils.get(member.guild.roles, id=role_id)
        if not roleObj:
            raise LookupError(f"The role for department {dept[dbMember.department_id]} was not found.")
        await member.add_roles(roleObj)

async def assignDefaultRole(member: discord.Member, mode: int = 0):
    if mode == 2:
        role = discord.utils.get(member.guild.roles, id=Level.LT.value)
        if not role:
            raise LookupError("The LT role was not found.")
        await member.add_roles(role)
    
    elif mode == 1:
        role = discord.utils.get(member.guild.roles, id=Level.CORE.value)
        if not role:
            raise LookupError("The Core role was not found.")
        await member.add_roles(role)

    else:
        role = discord.utils.get(member.guild.roles, id=Level.EXEC.value)
        if not role:
            raise LookupError("The Exec role was not found.")
        await member.add_roles(role)
