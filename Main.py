'''
       ______      ___    _       __     __       ____            _           
      / ____/___ _/ (_)  | |     / /__  / /_     / __ \___  _____(_)___ _______ 
     / /   / __ `/ / /   | | /| / / _ \/ __ \   / / / / _ \/ ___/ / __ `/ __  /
    / /___/ /_/ / / /    | |/ |/ /  __/ /_/ /  / /_/ /  __(__  ) / /_/ / / / /
    \____/\__,_/_/_/     |__/|__/\___/_.___/  /_____/\___/____/_/\__, /_/ /_/ 
                                                                /____/       

    This program was created by Cali Web Design Corporation. http://www.caliwebdesignservices.com
    
    Copyright Statement: Do not copy this website, if the code is found to be duplicated, reproduced,
    or copied we will fine you a minimum of $250,000 and criminal charges may be pressed.
    
    Creator/Developer: Cali Web Design Development Team, Michael Brinkley, Nick Derry.
    
    Inital Development: 11/28/2023
    Last Edited: 11/28/2023
     Contact Information:
        Phone: +1-877-597-7325
        Email: support@caliwebdesignservices.com
        
    CopyOurCodeWeWillSendYouToJesus(C)2023ThisIsOurHardWork.
        
    Dear rule breakers, questioners, straight-A students who skipped class: We want you.
    https://caliwebdesignservices.com/careers.
    
    NOTICE TO ALL DEVELOPERS, DO NOT MISUSE COPY OR EDIT THE MYSQL INFORMATION FOR THE BOT AS ITS
    A SHARED DATABASE FOR OUR WEB HOSTING AND WEB DESIGN SERVICES.
    
'''


import discord
import aiofiles
import os
import sys
import json
from discord.ext import commands
from cogs.utils.checks import load_env_vars, read_json, write_json
import asyncio

class Bot(commands.AutoShardedBot):
    async def is_owner(self, user: discord.User):
        bypassed_users = [1117952814044434442, 1063643318757634168]
        if user.id in bypassed_users:
            return True
        else:
            return False

    async def setup_hook(self) -> None:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
        await bot.load_extension("cogs.utils.hot_reload")
        print("All cogs loaded successfully!")

intent = discord.Intents.default()
intent.message_content = True
intent.members = True
bot = Bot(
    command_prefix=load_env_vars.prefix(),
    intents=intent,
    help_command=None,
    allowed_mentions=discord.AllowedMentions(
        replied_user=True, everyone=True, roles=True
    ),
)

bot.blacklisted_users = []

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f"channels | m.help"))
    data = read_json("blacklisted")
    bot.blacklisted_users = data["blacklistedUsers"]
    print(bot.user.name + " is ready.")

@bot.before_invoke
async def before_invoke(ctx):
    if ctx.channel.type == discord.ChannelType.private:
        raise commands.NoPrivateMessage(
            "This command cannot be used in private messages."
        )

    elif ctx.author.id in bot.blacklisted_users:
        if ctx.invoked_with != "unblacklist":
            raise commands.CommandInvokeError("You are blacklisted.")

bot.run(load_env_vars.token())
