import discord
from discord.ext import commands

from config import BOT_TOKEN, BOT_CHANNEL, INVITE_TO_CHANNEL
from db import init_db

from controllers.memberJoinController import memberJoinController
from errorHandler.registerErrorHandler import register_error_handler
from errorHandler.verboseErrorHandler import verbose_error_handler
from middleware import need_bot_channel

from controllers.tools import purgeController, verboseController
from controllers.setModeController import setModeController
from controllers.registerController import registerController

from errorHandler.purgeErrorHandler import purge_error_handler
from errorHandler.setModeErrorHandler import setMode_error_handler
from errorHandler.commandErrorHandler import command_error_handler

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

init_db()

bot = commands.Bot(command_prefix="!", intents=intents)

bot_channel = None
invite_channel = None

# Start with the bot's presence set to idle
@bot.event
async def on_ready():
    global bot_channel, invite_channel
    bot_channel = await bot.fetch_channel(BOT_CHANNEL)
    invite_channel = await bot.fetch_channel(INVITE_TO_CHANNEL)
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Streaming(name = "MUN Society", url = "https://munsocietympstme.com/")
    )
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

# Webhooks don't trigger commands. 
@bot.event
async def on_message(message):
    if message.channel.id == bot_channel.id and message.webhook_id:
        parts = message.content.strip().split()
        if len(parts) >= 4:
            dept_id = int(parts[1])
            email = parts[2]
            name = " ".join(parts[3:])
            await registerController(bot_channel, invite_channel, dept_id, email, name)
        else:
            await message.channel.send("Invalid format. Usage: `!register <deptId> <email> <name>`")
        return

    await bot.process_commands(message)

# Setup a command error handler
@bot.event
async def on_command_error(ctx, error):
    await command_error_handler(ctx, error)

@bot.event
async def on_member_join(member):
    await memberJoinController(member, bot.user.id)

# !setMode command to set the mode for direct roles
@bot.command()
@need_bot_channel(BOT_CHANNEL)
async def setMode(ctx, new_mode = "0"):
    await setModeController(ctx, new_mode=int(new_mode))

# setMode command error handler
@setMode.error
async def setMode_error(ctx, error):
    await setMode_error_handler(ctx, error)

# !register command to register a new member
@bot.command()
@need_bot_channel(BOT_CHANNEL)
async def register(ctx, deptId: int = None, email: str = None, *, name: str = None):
    await registerController(bot_channel, invite_channel, deptId, email, name)

# register command error handler
@register.error
async def register_error(ctx, error):
    await register_error_handler(ctx, error)

# !purge command to delete messages
@bot.command(aliases=['clear', 'delete'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int=20):
    await purgeController(ctx, amount)

# purge command error handler
@purge.error
async def purge_error(ctx, error):
    await purge_error_handler(ctx, error)

# !verbose command to send a verbose message
@bot.command()
async def verbose(ctx, *, message: str):
    await verboseController(ctx, message)

# verbose command error handler
@verbose.error
async def verbose_error(ctx, error):
    verbose_error_handler(ctx, error)

bot.run(BOT_TOKEN)