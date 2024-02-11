# ** uAgent address **
from uagents import Agent

vajra= Agent(name="vajra", seed="vajra recovery phase")

print("uAgent address: ", vajra.address)


# ** Print Fetch Network Address **
from uagents import Agent

vajra= Agent(name="vajra", seed="vajra recovery phrase")

print("Fetch network address:", vajra.wallet.address())


