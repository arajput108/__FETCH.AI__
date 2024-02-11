# **Printing Agent Name and Address using Context class**
from uagents import Agent, Context

vajra= Agent(name= "vajra", seed= "vajra recovery phrase")

@vajra.on_event("startup")
async def intoduce_agent(ctx: Context):
    ctx.logger.info(f"Hello,I'm agent {ctx.name} and my address is {ctx.address}.")

if __name__=="__main__":
    vajra.run()