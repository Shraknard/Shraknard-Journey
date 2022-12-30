import discord
import openai
import yaml
from pprint import pprint

# Loads secret.yaml data
with open("secret.yaml", "r") as file:
	config = yaml.safe_load(file)

openai.api_key = config["openaiToken"]
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
	if '!detail ' not in message.content:
		return

	# Define the prompt for the chatbot
	basePrompt = "Imagine a detailed description for " 
	question = basePrompt + message.content.replace('!detail ', '')
	
	# Send the first message so people knows it is processing.
	embed = discord.Embed(title="Generating a Midjourney input", color=0xf5f542)
	embed.add_field(name="Question", value=question, inline=False)
	embed.add_field(name="Generated description", value="Please wait...", inline=False)
	embed.add_field(name="Final Midjourney input", value="Please wait...", inline=False)
	msg = await message.channel.send(embed=embed)

	# Use the ChatGPT API to generate a detailed response
	response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=question,
		max_tokens=1000,
		temperature=0.5,
		top_p=1,
		frequency_penalty=1,
		presence_penalty=2
	)['choices'][0].text
	
	# Send an other message showing update
	embed = discord.Embed(title="Generating a Midjourney input", color=0xf5f542)
	embed.add_field(name="Question", value=question, inline=False)
	embed.add_field(name="Generated description", value=response, inline=False) 
	embed.add_field(name="Final Midjourney input", value="Please wait...", inline=False)
	await msg.edit(embed=embed)

	# Ask ChatGPT to make a lsit of pronouns and adjectives from the description it generated
	condense = '"' + response + " Condense this description to focus on pronouns and adjectives separated by coma" + '"'
	res = openai.Completion.create(
		engine="text-davinci-003",
		prompt=condense,
		max_tokens=500,
		temperature=0.2,
		top_p=1,
		frequency_penalty=1,
		presence_penalty=2,
	)['choices'][0].text
	
	# Update the final string
	final = question.replace(basePrompt, '') + " " + res.replace('\n', '')

	# Send the result to discord
	try:
		embed = discord.Embed(title="Generating a Midjourney input", color=0xf5f542)
		embed.add_field(name="Question", value=question, inline=False)
		embed.add_field(name="Generated description", value=response, inline=False)
		embed.add_field(name="Final Midjourney input", value=final, inline=False)
		await msg.edit(embed=embed)
	except ValueError as e:
		await message.channel.send("Error while generating message")
	return
	
# Run the client (This runs first)
client.run(config['discordToken'])
