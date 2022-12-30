# Shraknard Journey

<img src="https://github.com/Shraknard/Shraknard-Journey/blob/main/example.png" alt="example" width="400"/>

## Description

This bot purpose is to generate detailed text to input in [Midjourney](https://www.midjourney.com/).  
It uses [ChatGPT](https://chat.openai.com/chat) to generate detailed descriptions that are then condensed in a text containing mostly pronouns and adjective separated by comas. 

## usage

Once installed, you can use it by typing the command `!detail` followed by anything you want.  

**You send**:  
`!detail an alien`  

**Bot response**:  
`an alien Tall, slender, two arms, four fingers, sharp claws, long tail, scaly green skin, large antennae, yellow slits eyes, small fangs.`

## Install & run

**To use the bot, you'll have to host it yourself.**

**TLDR** : Create a bot in your discord profile, then copy this repo, edit the `secret.yaml` with your info then start the bot using `python ShraknardJourney.py`

### **1) Start a ubuntu VM or server (AWS, GCP, ... or directly on your machine)**

The bot is made to be used in a linux server but as it is written in Python, you are able to use it on other OS.  
If so, **install_ubuntu.sh** will not work and you'll have to adapt by yourself.  
I recommand to install it on a server rather than on tour personnal machine so it can be active 24/7.  
You can set a little server, no need for 18 core with 42GB RAM.  

Here are some usefull guides for creating linux server :  
[Creating a virtual machine in GCP](https://cloud.google.com/compute/docs/quickstart-linux)  
[Creating a server on AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)  

### **2) Create a discord bot**  

[You can follow this tutorial to create and add a bot to your Discord Server](https://discordpy.readthedocs.io/en/stable/discord.html)  
You also need to give it some autorisation to get the members names and IDs.  
Go to https://discord.com/developers/applications/ -> Select your bot -> got to the "**Bot**" page -> Enable **Presence Intent** and **Server Members Intent**.  
The bot only need permission to "send message" and "read history".  

### **3) Clone this repository and install dependencies** 

Open a terminal on your linux server and clone the code : `git clone https://github.com/vmercadi/pyaxie-bot`  
Then install the python dependencies : `pip3 install openai discord`

### **4) Edit secret.yaml**

Now you need to edit the `secret.yaml` file with your own [OpenAI API](https://beta.openai.com/account/api-keys) and [Discord bot token](https://discord.com/developers/applications/) (in Oauth2->General).

### **5) Ready to go**

Now everything should be good. You can run the bot using : `python ShraknardJourney.py`



