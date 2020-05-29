import discord
import pypokedex
from discord.ext import commands

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
        p = pypokedex.get(name=pokemon)
        try:
            pokemonName = p.name
            embed = discord.Embed(title=f"**{pokemonName.capitalize()} [{p.dex}]**", color=0xf5f5dc)
            embed.add_field(name="Basics", value=f"**Height: ** {p.height}\n**Weight: ** {p.weight}\n**Base Experience: ** {p.base_experience}\n**Type: ** {p.types}\n**Abilities: ** {p.abilities}", inline=False)
            embed.add_field(name="Stats and Moves", value=f"**Hp: ** {p.base_stats[0]}\n**Attack: ** {p.base_stats[1]}\n**Defense: ** {p.base_stats[2]}\n**SpecialAtk: ** {p.base_stats[3]}\n**SpecialDef: ** {p.base_stats[4]}\n**Speed: ** {p.base_stats[5]}")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(e)

def setup(bot):
    bot.add_cog(Utility(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
