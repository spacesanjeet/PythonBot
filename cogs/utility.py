import discord
import urbandictionary as ud
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
        for d in definition:
            embed.add_field(name='Definition' , value = d.definition , inline = True)
            embed.add_field(name='Example' , value = d.example, inline = True)
            embed.add_field(name= 'Upvotes 👍' , value = d.upvotes , inline = True)
            embed.add_field(name='Downvotes 👎' , value = d.downvotes , inline = True)
            embed.set_footer(text = 'Requested by {}'.format(ctx.message.author))
            embed.set_thumbnail(url = 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSZp9CZhLovlcsXWhjiIPjTEwWG7HRmCEYT7NmYDXrGdYUOhfRWjHgbdiU9')
            await ctx.send(embed=embed)
            break

        return

def setup(bot):
    bot.add_cog(Utility(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
