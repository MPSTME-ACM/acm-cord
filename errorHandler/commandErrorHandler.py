from discord.ext import commands

async def command_error_handler(ctx, error):
    if isinstance(error, commands.CheckFailure):
        pass
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        raise error