from discord.ext import commands

async def verbose_error_handler(ctx, error):
    """
    Handles errors for the verbose command.
    """
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❗ Please provide a message to send.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("❗ An error occurred while trying to send the message.")
    else:
        await ctx.send(f"❗ An unexpected error occurred: {error}")
    
    # Log the error for debugging purposes
    print(f"Error in verbose command: {error}")