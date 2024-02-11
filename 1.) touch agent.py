from uagents import Agent, Context
 
vajra = Agent(name="vajra", seed="vajra recovery phrase")
 
@vajra.on_event("startup")
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.name}')
 
if __name__ == "__main__":
    vajra.run()