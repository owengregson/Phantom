#Command recognizers should start with @Phantom.command (Phantom will react to your command)
@Phantom.command(name="example") # Name of the command
async def example(ctx): # Define your function
    await ctx.send("Hello world!") # Send a message
