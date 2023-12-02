import discord
import asyncio
import json
from discord.ext import commands 
from discord.ext.commands import CommandNotFound
from cogs.utils.checks import *


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def help(self, ctx):
      if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Help Page", description=f"```fix\nBot Prefix: s!.```", color=discord.Color.blue())
        embed.add_field(name="Moderation", value=f"`s!help moderation`")
        embed.add_field(name="Warn", value=f"`s!help warn`")
        embed.add_field(name="Other", value=f"`s!help other`")
        embed.set_footer(text="Designed and Develped by Cali Web Design Services")
        await ctx.send(embed=embed)

    @help.command()
    async def moderation(self, ctx):
      embed = discord.Embed(title="Moderation Commands", description=f"`s!kick @person [reason for kicked]` - kick someone\n\n`s!ban @person [reason for banned]` - ban someone\n\n`s!unban name#id` - unban someone\n\n`s!unmute @person` - unmute someone\n\n`s!mute @person [amount d,h,m,s ex: 5s] [reason]` - time mute someone\n\n`s!clear [amount]` - purges messages, default is 20\n\n`s!give @person @role` - give someone a role\n\n`s!remove @person @role` - remove a role from someone\n\n`s!nick @person [nickname]` - Nickname someone\n\n`s!reset_nick @person` - reset the nickname for the user\n\n`s!sendvm [command]` - this will send a verification message with the command of your choice\n\n`s!verify` - this is the stock verification command", color=discord.Color.blue())
      embed.set_footer(text="All commands have a cooldown")
      await ctx.send(embed=embed)

    @help.command()
    async def warn(self, ctx):
      embed = discord.Embed(title="Warn Commands", description=f"`s!warn @person [reason they were warned]` - warn someone\n\n`s!warnings @person` - get the warnings for someone\n\n`s!delwarn @person` - Deletes all warns for the person you mentioned", color=discord.Color.blue())
      embed.set_footer(text="All commands have a cooldown")
      await ctx.send(embed=embed)

    @help.command()
    async def other(self, ctx):
      embed = discord.Embed(title="Member commands", description=f"`s!suggest [message]` - suggest something to the staff of the server\n\n`s!modmail [message]` - contact an Mod/Admin for questions or help\n\n`s!afk [AFK Note]` - sets you as afk", color=discord.Color.blue())
      embed.set_footer(text="All commands have a cooldown")
      await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(help(bot))