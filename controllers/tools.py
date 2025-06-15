from config import Level

async def purgeController(ctx, amount: int = 20):
    if amount < 1 or amount > 250:
        await ctx.send("❗ Please specify a number between 1 and 250.")
        return
    
    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"✅ Deleted {len(deleted) - 1} message(s).", delete_after=5)

async def verboseController(ctx, message: str):
    has_role = any(role.id == Level.LT.value for role in ctx.author.roles)
    is_admin = ctx.author.guild_permissions.administrator

    if not (has_role or is_admin):
        await ctx.send("🚫 You don't have permission to use this command.", delete_after=5)
        return

    await ctx.message.delete()
    await ctx.send(f"{message}") # \n\n_This message was verbose'd by {ctx.author.mention}._")