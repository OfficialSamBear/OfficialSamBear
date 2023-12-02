import discord
import aiofiles
import os
import sys
import json
from discord.ext import commands
from cogs.utils.checks import load_env_vars, read_json, write_json
import asyncio

class admincmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.X_train = None

    @commands.command()
    @commands.is_owner()
    async def blacklist(ctx, member: discord.Member):
        data = read_json("blacklisted")
        bot.blacklisted_users = data["blacklistedUsers"]
        if member.id in bot.blacklisted_users:
            await ctx.send(f"{member.name} is already blacklisted")
        else:
            data["blacklistedUsers"].append(member.id)
            write_json(data, "blacklisted")
            await ctx.send(f"I have blacklisted {member.name}")


    @commands.command()
    @commands.is_owner()
    async def unblacklist(ctx, member: discord.Member):
        data = read_json("blacklisted")
        bot.blacklisted_users = data["blacklistedUsers"]
        if member.id in bot.blacklisted_users:
            data["blacklistedUsers"].remove(member.id)
            write_json(data, "blacklisted")
            await ctx.send(f"I have unblacklisted {member.name}")
        else:
            await ctx.send(f"{member.name} is not blacklisted")

async def setup(bot):
    await bot.add_cog(admincmd(bot))
