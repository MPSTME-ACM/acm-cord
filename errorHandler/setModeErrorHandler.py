from discord.ext import commands

async def setMode_error_handler(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        pass
    elif isinstance(error, commands.CheckFailure):
        pass
    else:
        raise error