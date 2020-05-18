import discord
import urbandict as ud
from discord.ext import commands

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='urban',
        description='Search from urbandictionary!',
        aliases=['def', 'ud'],
        usage='<text>'
    )
    async def urban_command(self, ctx, *, word):
        embed= discord.Embed(title = word, description='Heres what I could find' , color =0xf5f5dc)
        definition = ud.define(word)
        dict = definition[0]
        embed.add_field(name='Definition', value = dict[def])
        embed.add_field(name='Example', value = dict[example])
        embed.add_field(name='Category', value= dict[category])
        await ctx.send(embed=embed)

        return

def setup(bot):
    bot.add_cog(Utility(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
