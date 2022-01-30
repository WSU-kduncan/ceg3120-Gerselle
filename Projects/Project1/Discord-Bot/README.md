# Project 1 Answers
## Setup

- How to get an API token?
	- First if you don't have discord account, [make one](https://discord.com/register).
	- Then log into the [Discord developer panel](https://discordapp.com/developers/applications).
	- In the Applications tab, press on "New Application" on the top right and create one .
	- Then select your new application, and press on the "Bot" tab, then press "Add Bot".
	- After creating your new bot, click on the "Copy" button right next to the bot's icon.

- Where to place token?
	- Prepare your pre-made token or a new one from following the steps above.
	- In the same folder for your bot's code, create an ".env" file.
	- In this new file, enter `DISCORD_TOKEN=[Token]` , where [Token] is  replaced completely by your token.

- Required Dependencies 
	- Python 3
	- Discord 

## Usage

- Current version of the bot can respond to the following phrases:
	- "towel!"
	- "Hello!", "Hi!", or "Hey!"
	- "What do you have?"

- The bot will give the following responses
	- Hitchhicker's Guide to the Galaxy quotes.
		- There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.
		- It is a mistake to think you can solve any major problems just with potatoes.
		- In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.
		- A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.
	- Random greetings in 9 different languages.
		
		| Language | Phrase      	|
		|----------|-------------	|
		| Spanish  | ¡Hola!      	|
		| French   | Bonjour!		|
		| Japanese | こんにちは!	 |
		| Korean   | 여보세요!		 |
		| Russian  | Привет!		|
		| Chinese  | 你好!			|
		| Tagalog  | Kamusta!    	|
		| Arabic   | مرحبا!      	|
		| German   | Grüß Gott!  	|
	- Random images to answer "What do you have?".
		|  			|   		|   		|
		|---		|---		|---		|
		|![](1.jpg)	|![](2.jpg)	|![](3.jpg)	|
		|![](6.jpg)	|![](5.jpg)	|![](4.jpg)	|
		|![](7.jpg)	|![](8.jpg)	|![](9.jpg)	|

## Research

	Essentially, to ensure the bot is "always on" as much as possible, you need to have it running on a dedicated machine that will run 24/7. Potential options include, but are not limited to:
	
	- Personal computers
		- Raspberry Pi's or similar devices with low power consumption would be perfect since this discord bot doesn't need that much processing power to begin with.
	- Cloud servers (AWS, Azure, Google)
		- Again, since this bot doesn't need crazy high specs, consider using the cheapest option available.
	- Virtual Machines
		- If you have a home server, you could setup a simple VM with the sole task of running the bot, that way, any potential exploitations or security risks of the bot can be contained easily and would not be able harm the rest of the machine.