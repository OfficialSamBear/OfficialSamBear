import discord
import os
import random
import json
from dotenv import load_dotenv
from discord.ext import commands


def read_json(filename):
  with open(f"cogs/data/{filename}.json", "r") as f:
    data = json.load(f)
  return data

def write_json(data, filename):
  with open(f"cogs/data/{filename}.json", "w") as f:
    json.dump(data, f, indent=4)

class load_env_vars():
    load_dotenv()
    def token():
      TOKEN = os.getenv('TOKEN')
      token = str(TOKEN)
      return token
    def prefix():
      PREFIX = os.getenv('PREFIX')
      prefix = str(PREFIX)
      return prefix
    def sql_user():
      sql_user = os.getenv('MYSQL_USER')
      sql_user = str(sql_user)
      return sql_user
    def sql_password():
      sql_password = os.getenv('MYSQL_PASSWORD')
      sql_password = str(sql_password)
      return sql_password
    def sql_host():
      sql_host = os.getenv('MYSQL_HOST')
      sql_host = str(sql_host)
      return sql_host
    def sql_port():
      sql_port = os.getenv('MYSQL_PORT')
      sql_port = int(sql_port)
      return sql_port
    def sql_database():
      sql_database = os.getenv('MYSQL_DATABASE')
      sql_database = str(sql_database)
      return sql_database
    
def is_staff():
  def predicate(ctx):
    return True
  return commands.check(predicate)