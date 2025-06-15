from config import Config
import discord
from discord.ext import commands
from discord.guild import Guild
from discord.channel import TextChannel
from discord.invite import Invite

variables = Config()

BOT_TOKEN = variables.BOT_TOKEN
OWNER_ID = variables.OWNER_ID

owner: discord.User = None

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    guild: Guild = await bot.create_guild(name="MUN Society 25-26")
    channel: TextChannel = await guild.fetch_channels()[0]
    invite: Invite = await channel.create_invite()
    print(f"Join and configure this server: {invite.url}")
    global owner
    owner = await bot.fetch_user(OWNER_ID)

@bot.event
async def on_member_join(ctx, member: discord.Member):
    print(f"Member {member.name} has joined the server.")
    guild: Guild = member.guild
    admin_perms = discord.Permissions(administrator=True)
    admin_role = await guild.create_role(name="Owner", permissions=admin_perms, reason="Initial setup")
    if member.id == owner.id:
        await member.add_roles(admin_role, reason="Assigned admin role to the owner.")

bot.run(BOT_TOKEN)