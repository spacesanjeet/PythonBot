import discord
from discord.ext import commands
import requests

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='pokedex',
        description='Get the pokedex!',
        aliases=['pokemon', 'poke'],
        usage='<pokemonName>'
    )
    async def pokedex_command(self, ctx, pokemon):
        try:
            response = requests.get('https://some-random-api.ml/pokedex?pokemon='+ pokemon)
            response.raise_for_status()
            # access JSOn content
            jsonResponse = response.json()
            dict = jsonResponse.get('sprites')
            embed =  discord.Embed(title=f"**{pokemon.capitalize()} [{jsonResponse.get('id')}]**", description=f"{jsonResponse.get('description')}", color=0xf5f5dc)
            embed.set_thumbnail(url=dict.get('normal'))
            embed.add_field(name="Basics", value=f"**Height: ** {jsonResponse.get('height')}\n**Weight: ** {jsonResponse.get('weight')}\n**Base Experience: ** {jsonResponse.get('base_experience')}\n**Type: ** {jsonResponse.get('type')}\n**Abilities: ** {jsonResponse.get('abilities')}", inline=False)
            embed.add_field(name="Family", value=f"**Egg Group: ** {jsonResponse.get('egg_group')}\n**Family: ** {jsonResponse.get('family')}\n**Gender: ** {jsonResponse.get('gender')}\n**Generation: ** {jsonResponse.get('generation')}\n**Species: ** {jsonResponse.get('species')}", inline=False)
            embed.add_field(name="Stats", value=f"{jsonResponse.get('stats')}")
            await ctx.send(embed=embed)
        except Exception as err:
            await ctx.send(err)

def setup(bot):
    bot.add_cog(Utility(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
