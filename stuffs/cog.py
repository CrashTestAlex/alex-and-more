import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta
import random
import ballsdex
from ballsdex.core.utils.transformers import (
    BallTransform,
    SpecialTransform,
)
from ballsdex.core.models import (
    Ball,
    BallInstance,
    BlacklistedGuild,
    BlacklistedID,
    GuildConfig,
    Player,
    Trade,
    TradeObject,
    Special
)
from ballsdex.settings import settings
from ballsdex.packages.countryballs.countryball import CountryBall
import ballsdex.packages.config.components as Components
from typing import TYPE_CHECKING, cast

# Credits
# -------
# - crashtestalex
# - hippopotis
# - dot_zz

last_small_times = {}
last_big_times = {}
last_mega_times = {}
last_boost_claim_times = {}

# Down here is where you can alter the cooldowns for each of the commands.
#  I havent been able to make it so when the bot goes down, the commands
# reset, but it'll happen soon, I bet your bottom dollar it'll happen soon!

SMALL_COOLDOWN = timedelta(hours=2)
BIG_COOLDOWN = timedelta(hours=6)
MEGA_COOLDOWN = timedelta(days=1)
BOOST_COOLDOWN_DURATION = timedelta(hours=1, minutes=15)

class Boxes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# WAIT!!! BEFORE YOU UNCOMMENT THE SPECIALS!
# If you DO want the boxes to give you special cards, uncomment each
# & add their respectful ID from the admin panel in the () next to the "int".
# If you DON'T however, delete each of them, and go to the embed areas of EACH OF THE
# EMBED MESSAGES AND DELETE EVERYTHING THAT SAYS "``📦{instanceX.special}``" so that 
# you dont waste more time getting any errors in your terminal.

    async def small_box_rewards(self, interaction: discord.Interaction, box_type: str):
        
        UserID = str(interaction.user.id)
        username = str(interaction.user.name)
        player, created = await Player.get_or_create(discord_id=UserID)
        cob1 = await CountryBall.get_random()
        cob2 = await CountryBall.get_random()
        cob3 = await CountryBall.get_random()
        box_type = "small"

        instance1 = await BallInstance.create(
                ball=cob1.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int("ID GOES HERE")) 
            )
        instance2 = await BallInstance.create(
                ball=cob2.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance3 = await BallInstance.create(
                ball=cob3.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )

        emoji1 = self.bot.get_emoji(instance1.countryball.emoji_id)
        emoji2 = self.bot.get_emoji(instance2.countryball.emoji_id)
        emoji3 = self.bot.get_emoji(instance3.countryball.emoji_id)

        embed = discord.Embed(title=f"*{username}'s* **Small Box**!", description=f"Small Boxes give 3 {settings.plural_collectible_name}, as seen below!", color=discord.Colour.blue())
        embed.add_field(name=f"x1 {emoji1} {cob1.name}", value=f"``💖{instance1.attack_bonus}`` ``⚔️{instance1.health_bonus}`` ``📦{instance1.special}``") # Don't forget!!!
        embed.add_field(name=f"x1 {emoji2} {cob2.name}", value=f"``💖{instance2.attack_bonus}`` ``⚔️{instance2.health_bonus}`` ``📦{instance2.special}``")
        embed.add_field(name=f"x1 {emoji3} {cob3.name}", value=f"``💖{instance3.attack_bonus}`` ``⚔️{instance3.health_bonus}`` ``📦{instance3.special}``")
        embed.set_thumbnail(url="") # Optional 
        embed.set_footer(text="Open your next small box in 2 hours from this message.")

        await interaction.response.send_message(
            embed=embed,
            ephemeral=False
        )

    async def big_box_rewards(self, interaction: discord.Interaction, box_type: str):
        
        UserID = str(interaction.user.id)
        username = str(interaction.user.name)
        player, created = await Player.get_or_create(discord_id=UserID)
        cob1 = await CountryBall.get_random()
        cob2 = await CountryBall.get_random()
        cob3 = await CountryBall.get_random()
        cob4 = await CountryBall.get_random()
        cob5 = await CountryBall.get_random()
        box_type = "big"

        instance1 = await BallInstance.create(
                ball=cob1.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance2 = await BallInstance.create(
                ball=cob2.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance3 = await BallInstance.create(
                ball=cob3.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance4 = await BallInstance.create(
                ball=cob4.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance5 = await BallInstance.create(
                ball=cob5.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )

        emoji1 = self.bot.get_emoji(instance1.countryball.emoji_id)
        emoji2 = self.bot.get_emoji(instance2.countryball.emoji_id)
        emoji3 = self.bot.get_emoji(instance3.countryball.emoji_id)
        emoji4 = self.bot.get_emoji(instance4.countryball.emoji_id)
        emoji5 = self.bot.get_emoji(instance5.countryball.emoji_id)

        embed = discord.Embed(title=f"*{username}'s* **Big Box**!" , description=f"Big Boxes give 5 {settings.plural_collectible_name}, as seen below!", color=discord.Colour.purple())
        embed.add_field(name=f"x1 {emoji1} {cob1.name}", value=f"``💖{instance1.attack_bonus}`` ``⚔️{instance1.health_bonus}`` ``📦{instance1.special}``")
        embed.add_field(name=f"x1 {emoji2} {cob2.name}", value=f"``💖{instance2.attack_bonus}`` ``⚔️{instance2.health_bonus}`` ``📦{instance2.special}``")
        embed.add_field(name=f"x1 {emoji3} {cob3.name}", value=f"``💖{instance3.attack_bonus}`` ``⚔️{instance3.health_bonus}`` ``📦{instance3.special}``")
        embed.add_field(name=f"x1 {emoji4} {cob4.name}", value=f"``💖{instance4.attack_bonus}`` ``⚔️{instance4.health_bonus}`` ``📦{instance4.special}``")
        embed.add_field(name=f"x1 {emoji5} {cob5.name}", value=f"``💖{instance5.attack_bonus}`` ``⚔️{instance5.health_bonus}`` ``📦{instance5.special}``")
        embed.set_thumbnail(url="") # Optional
        embed.set_footer(text="Open your next big box in 6 hours from this message.")

        await interaction.response.send_message(
            embed=embed,
            ephemeral=False
        )

    async def mega_box_rewards(self, interaction: discord.Interaction, box_type: str):
        
        UserID = str(interaction.user.id)
        username = str(interaction.user.name)
        player, created = await Player.get_or_create(discord_id=UserID)
        cob1 = await CountryBall.get_random()
        cob2 = await CountryBall.get_random()
        cob3 = await CountryBall.get_random()
        cob4 = await CountryBall.get_random()
        cob5 = await CountryBall.get_random()
        cob6 = await CountryBall.get_random()
        cob7 = await CountryBall.get_random()
        cob8 = await CountryBall.get_random()
        cob9 = await CountryBall.get_random()
        cob10 = await CountryBall.get_random()
        box_type = "mega"

        instance1 = await BallInstance.create(
                ball=cob1.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int(Add the ID in HERE!!))
            )
        instance2 = await BallInstance.create(
                ball=cob2.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int(Same here...))
            )
        instance3 = await BallInstance.create(
                ball=cob3.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int(And here...))
            )
        instance4 = await BallInstance.create(
                ball=cob4.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int(Ok u get it))
            )
        instance5 = await BallInstance.create(
                ball=cob5.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance6 = await BallInstance.create(
                ball=cob6.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance7 = await BallInstance.create(
                ball=cob7.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance8 = await BallInstance.create(
                ball=cob8.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance9 = await BallInstance.create(
                ball=cob9.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        instance10 = await BallInstance.create(
                ball=cob10.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
#                special= await Special.get(pk=int())
            )
        
        emoji1 = self.bot.get_emoji(instance1.countryball.emoji_id)
        emoji2 = self.bot.get_emoji(instance2.countryball.emoji_id)
        emoji3 = self.bot.get_emoji(instance3.countryball.emoji_id)
        emoji4 = self.bot.get_emoji(instance4.countryball.emoji_id)
        emoji5 = self.bot.get_emoji(instance5.countryball.emoji_id)
        emoji6 = self.bot.get_emoji(instance6.countryball.emoji_id)
        emoji7 = self.bot.get_emoji(instance7.countryball.emoji_id)
        emoji8 = self.bot.get_emoji(instance8.countryball.emoji_id)
        emoji9 = self.bot.get_emoji(instance9.countryball.emoji_id)
        emoji10 = self.bot.get_emoji(instance10.countryball.emoji_id)

        embed = discord.Embed(title=f"*{username}'s* **Mega Box**!", description=f"Mega Boxes give 10 whopping {settings.plural_collectible_name}!!", color=discord.Colour.gold())
        embed.add_field(name=f"x1 {emoji1} {cob1.name}", value=f"``💖{instance1.attack_bonus}`` ``⚔️{instance1.health_bonus}`` ``📦{instance1.special}``")
        embed.add_field(name=f"x1 {emoji2} {cob2.name}", value=f"``💖{instance2.attack_bonus}`` ``⚔️{instance2.health_bonus}`` ``📦{instance2.special}``")
        embed.add_field(name=f"x1 {emoji3} {cob3.name}", value=f"``💖{instance3.attack_bonus}`` ``⚔️{instance3.health_bonus}`` ``📦{instance3.special}``")
        embed.add_field(name=f"x1 {emoji4} {cob4.name}", value=f"``💖{instance4.attack_bonus}`` ``⚔️{instance4.health_bonus}`` ``📦{instance4.special}``")
        embed.add_field(name=f"x1 {emoji5} {cob5.name}", value=f"``💖{instance5.attack_bonus}`` ``⚔️{instance5.health_bonus}`` ``📦{instance5.special}``")
        embed.add_field(name=f"x1 {emoji6} {cob6.name}", value=f"``💖{instance6.attack_bonus}`` ``⚔️{instance6.health_bonus}`` ``📦{instance6.special}``")
        embed.add_field(name=f"x1 {emoji7} {cob7.name}", value=f"``💖{instance7.attack_bonus}`` ``⚔️{instance7.health_bonus}`` ``📦{instance7.special}``")
        embed.add_field(name=f"x1 {emoji8} {cob8.name}", value=f"``💖{instance8.attack_bonus}`` ``⚔️{instance8.health_bonus}`` ``📦{instance8.special}``")
        embed.add_field(name=f"x1 {emoji9} {cob9.name}", value=f"``💖{instance9.attack_bonus}`` ``⚔️{instance9.health_bonus}`` ``📦{instance9.special}``")
        embed.add_field(name=f"x1 {emoji10} {cob10.name}", value=f"``💖{instance10.attack_bonus}`` ``⚔️{instance10.health_bonus}`` ``📦{instance10.special}``")
        embed.set_thumbnail(url="") # Optional 
        embed.set_footer(text="Open your next mega box in 1 day from this message.")

        await interaction.response.send_message(
            embed=embed,
            ephemeral=False
        )

    @app_commands.command(name="small_box", description="Open a small box!") # Change the command name here.
    async def small_box(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        now = datetime.now()

        if user_id in last_small_times:
            last_small_time = last_small_times[user_id]
            elapsed_time = now - last_small_time

            if elapsed_time < SMALL_COOLDOWN:
                remaining_time = SMALL_COOLDOWN - elapsed_time
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                
                if hours > 0:
                    await interaction.response.send_message(
                        f'You cannot open a small box for {hours} hour{"s" if hours != 1 else ""}, {minutes} minute{"s" if minutes != 1 else ""}, and {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                elif minutes > 0:
                    await interaction.response.send_message(
                        f'You cannot open a small box for {minutes} minute{"s" if minutes != 1 else ""} and {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                else:
                    await interaction.response.send_message(
                        f'You cannot open a small box for {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                return

        last_small_times[user_id] = now

        await self.small_box_rewards(interaction, box_type="small")

    @app_commands.command(name="big_box", description="Open a big box!") # Again, change the command name here.
    async def big_box(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        now = datetime.now()

        if user_id in last_big_times:
            last_big_time = last_big_times[user_id]
            elapsed_time = now - last_big_time

            if elapsed_time < BIG_COOLDOWN:
                remaining_time = BIG_COOLDOWN - elapsed_time
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                
                if hours > 0:
                    await interaction.response.send_message(
                        f'You cannot open a big box for {hours} hour{"s" if hours != 1 else ""}, {minutes} minute{"s" if minutes != 1 else ""}, and {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                elif minutes > 0:
                    await interaction.response.send_message(
                        f'You cannot open a big box for {minutes} minute{"s" if minutes != 1 else ""} and {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                else:
                    await interaction.response.send_message(
                        f'You cannot open a big box for {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                return

        last_big_times[user_id] = now

        await self.big_box_rewards(interaction, box_type="big")

    @app_commands.command(name="mega_box", description="Open a mega box!") # And again, change the command name here.
    async def mega_box(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        now = datetime.now()

        if user_id in last_mega_times:
            last_mega_time = last_mega_times[user_id]
            elapsed_time = now - last_mega_time

            if elapsed_time < SMALL_COOLDOWN:
                remaining_time = SMALL_COOLDOWN - elapsed_time
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                
                if hours > 0:
                    await interaction.response.send_message(
                        f'You cannot open a mega box for {hours} hour{"s" if hours != 1 else ""}, {minutes} minute{"s" if minutes != 1 else ""}, and {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                elif minutes > 0:
                    await interaction.response.send_message(
                        f'You cannot open a mega box for {minutes} minute{"s" if minutes != 1 else ""} and {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                else:
                    await interaction.response.send_message(
                        f'You cannot open a mega box for {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                return

        last_mega_times[user_id] = now

        await self.mega_box_rewards(interaction, box_type="mega")