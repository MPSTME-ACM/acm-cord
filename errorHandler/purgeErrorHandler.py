from discord.ext import commands

async def purge_error_handler(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("🚫 You don't have permission to use this command.", delete_after = 5)
        await ctx.message.delete()
    elif isinstance(error, commands.BadArgument):
        await ctx.send("⚠️ Please provide a valid number.")
    else:
        raise error