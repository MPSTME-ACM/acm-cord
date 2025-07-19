from config import set_mode

async def setModeController(ctx, new_mode: int):
    """Set mode to give direct roles to what level, defaults to Executive."""
    if new_mode not in [0, 1, 2]:
        await ctx.send("⚠️ Please provide a valid number. \n 💙 `0` for Executive,\n 💠 `1` for Core, \n 👑 `2` for SC.")
        return
    set_mode(new_mode)
    await ctx.send(f"Mode set to {new_mode} ({'Executive' if new_mode == 0 else 'Core' if new_mode == 1 else 'SC'})")