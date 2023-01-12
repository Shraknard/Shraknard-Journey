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
	basePrompt = "Imagine a very detailed visual description for " 
	question = basePrompt + message.content.replace('!detail ', '')
	details = '; rich in terms but condensed to focus on pronouns and adjectives separated by coma. The condensed should be at least 120 characters long.'

	# Send the first message so people knows it is processing.
	embed = discord.Embed(title="Generating a Midjourney input", color=0xf5f542)
	embed.add_field(name="Question", value=question, inline=False)
	embed.add_field(name="Generated output", value="Please wait...", inline=False)
	msg = await message.channel.send(embed=embed)

	# Use the ChatGPT API to generate a detailed response
	response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=question + details,
		max_tokens=900,
		temperature=0.5,
		top_p=1,
		frequency_penalty=1,
		presence_penalty=2
	)['choices'][0].text
	
	# Update the final string
	final = question.replace(basePrompt, '') + " " + response.replace('\n', '')

	# Send the result to discord
	try:
		embed = discord.Embed(title="Generating a Midjourney input", color=0xf5f542)
		embed.add_field(name="Question", value=question, inline=False)
		embed.add_field(name="Generated output", value=final, inline=False)
		await msg.edit(embed=embed)
	except ValueError as e:
		await message.channel.send("Error while generating message")
	return
	
# Run the client (This runs first)
client.run(config['discordToken'])
