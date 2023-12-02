import discord
from discord.utils import get
from discord.ext import commands
from afks import afks
from cogs.utils.checks import load_env_vars, read_json
import mariadb
import sys

try:
    conn = mariadb.connect(
        user=load_env_vars.sql_user(),
        password=load_env_vars.sql_password(),
        host=load_env_vars.sql_host(),
        port=load_env_vars.sql_port(),
        database=load_env_vars.sql_database()
    )
    print("DB is now connected")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

class events(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self, ctx: commands.Context = None):
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Channel | s!help"))
    # cur = conn.cursor()
    # cur.execute(f"SELECT id FROM blacklists") # get all blacklisted users from sql, make sure you only get the member id
    # var = cur.fetchall()
    self.bot.blacklists = []#leave this empty
    # for member in var:
    #    self.bot.blacklists.append(member)# this will add the member id to the list above

    print(self.bot.user.name + " is ready.")

  @commands.Cog.listener()
  async def on_message(self, ctx):
    if self.bot.user.mentioned_in(ctx) and len(ctx.content.split(' ')) == 1 and ctx.content[-1] == ">" and ctx.content[0] == '<':
      await ctx.channel.send("My prefix is `s!`\nTry `s!help` for help with commands")

async def setup(bot):
  await bot.add_cog(events(bot))