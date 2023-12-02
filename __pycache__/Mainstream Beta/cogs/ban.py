import discord
import datetime
import mysql.connector
from discord.ext import commands
from cogs.utils.checks import load_env_vars, read_json, write_json
from cogs.events import conn

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        # Check if the user has necessary permissions or roles for banning
        return ctx.author.guild_permissions.ban_members

    @commands.hybrid_command(description="Ban Member", with_app_command=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="None was provided"):
        mycursor = conn.cursor()

        try:
            mycursor.execute(
                "INSERT INTO bans (member_id, guild_id, reason, banned_by, timestamp) VALUES (%s, %s, %s, %s, %s)",
                (member.id, ctx.guild.id, reason, ctx.author.id, datetime.datetime.utcnow())
            )
            conn.commit()

            # Notify about the ban
            embed = discord.Embed(
                title=f"Success!",
                description=f":white_check_mark: | {member.name} was banned for\n\nReason: `{reason}`",
                color=discord.Color.red()
            )
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                title="Banned!",
                description=f"You have been banned from {ctx.guild.name}!!\n\nReason: `{reason}`",
                color=discord.Color.red()
            )
            embed2.timestamp = datetime.datetime.utcnow()
            await member.send(embed=embed2)

            # Ban the member
            await member.ban(reason=reason)

        except mysql.connector.Error as err:
            # Handle the database error
            print(f"Error: {err}")
            await ctx.send("An error occurred while trying to ban the member.")
        finally:
            mycursor.close()
            

async def setup(bot):
  await bot.add_cog(ban(bot))