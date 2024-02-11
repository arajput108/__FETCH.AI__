from uagents import Agent, Context
 
vajra = Agent(name="vajra", seed="vajra recovery phrase")
 
@vajra.on_interval(period=2.0)
async def say_alert(ctx: Context):
    ctx.logger.info(f'alert, This is {ctx.name} speaking !!')
 
if __name__ == "__main__":
    vajra.run()
