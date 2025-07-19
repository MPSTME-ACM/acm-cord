from discord.ext import commands

def need_bot_channel(allowed_channel_id):
    async def predicate(ctx):
        if ctx.channel.id != allowed_channel_id:
            await ctx.send("This command can't be used in this channel, If you think this is a mistake, please contact Kartik Jain <acm.dc@jkartik.in>.", delete_after = 10)
            await ctx.message.delete()
            return False
        return True
    return commands.check(predicate)