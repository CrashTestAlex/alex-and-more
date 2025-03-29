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
    balls,
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
# -------

last_small_times = {}
last_big_times = {}
last_mega_times = {}
last_boost_claim_times = {}

# Down here is where you can alter the cooldowns for the command.
#  I havent been able to make it so when the bot goes down, the command
# resets, but it'll happen soon, I bet your bottom dollar it'll happen soon!

SMALL_COOLDOWN = timedelta(hours=12) # Base 12 but could be anything really, its up to YOU!

class Boxes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def small_box_rewards(self, interaction: discord.Interaction, box_type: str):      
        UserID = str(interaction.user.id)
        username = str(interaction.user.name)
        player, created = await Player.get_or_create(discord_id=UserID)
        cob1 = await CountryBall.get_random()
        cob2 = await CountryBall.get_random()
        box_type = "small"

        instance1 = await BallInstance.create(
                ball=cob1.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        instance2 = await BallInstance.create(
                ball=cob2.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )

        emoji1 = self.bot.get_emoji(instance1.countryball.emoji_id)
        emoji2 = self.bot.get_emoji(instance2.countryball.emoji_id)

        embed = discord.Embed(title=f"*{username}'s* **Small Box**!", description=f"Small Boxes give 2 {settings.plural_collectible_name}, as seen below!", color=discord.Colour.blue())
        embed.add_field(name=f"x1 {emoji1} {cob1.name}", value=f"``💖{instance1.attack_bonus}`` ``⚔️{instance1.health_bonus}`` ``📦{instance1.special}``") # Don't forget!!!
        embed.add_field(name=f"x1 {emoji2} {cob2.name}", value=f"``💖{instance2.attack_bonus}`` ``⚔️{instance2.health_bonus}`` ``📦{instance2.special}``")
        embed.set_thumbnail(url="") # Optional 
        embed.set_footer(text="Open your next box in # hours from this message.")

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
        box_type = "big"

        instance1 = await BallInstance.create(
                ball=cob1.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        instance2 = await BallInstance.create(
                ball=cob2.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        instance3 = await BallInstance.create(
                ball=cob3.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        instance4 = await BallInstance.create(
                ball=cob4.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )

        emoji1 = self.bot.get_emoji(instance1.countryball.emoji_id)
        emoji2 = self.bot.get_emoji(instance2.countryball.emoji_id)
        emoji3 = self.bot.get_emoji(instance3.countryball.emoji_id)
        emoji4 = self.bot.get_emoji(instance4.countryball.emoji_id)

        embed = discord.Embed(title=f"*{username}'s* **Big Box**!" , description=f"Big Boxes give 4 {settings.plural_collectible_name}, as seen below!", color=discord.Colour.purple())
        embed.add_field(name=f"x1 {emoji1} {cob1.name}", value=f"``💖{instance1.attack_bonus}`` ``⚔️{instance1.health_bonus}`` ``📦{instance1.special}``")
        embed.add_field(name=f"x1 {emoji2} {cob2.name}", value=f"``💖{instance2.attack_bonus}`` ``⚔️{instance2.health_bonus}`` ``📦{instance2.special}``")
        embed.add_field(name=f"x1 {emoji3} {cob3.name}", value=f"``💖{instance3.attack_bonus}`` ``⚔️{instance3.health_bonus}`` ``📦{instance3.special}``")
        embed.add_field(name=f"x1 {emoji4} {cob4.name}", value=f"``💖{instance4.attack_bonus}`` ``⚔️{instance4.health_bonus}`` ``📦{instance4.special}``")
        embed.set_thumbnail(url="") # Optional
        embed.set_footer(text="Open your next box in # hours from this message.")

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
        box_type = "mega"

        instance1 = await BallInstance.create(
                ball=cob1.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        instance2 = await BallInstance.create(
                ball=cob2.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        instance3 = await BallInstance.create(
                ball=cob3.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        instance4 = await BallInstance.create(
                ball=cob4.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        instance5 = await BallInstance.create(
                ball=cob5.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        instance6 = await BallInstance.create(
                ball=cob6.model,
                player=player,
                attack_bonus=random.randint(-20, 20),
                health_bonus=random.randint(-20, 20),
                special= await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
            )
        
        emoji1 = self.bot.get_emoji(instance1.countryball.emoji_id)
        emoji2 = self.bot.get_emoji(instance2.countryball.emoji_id)
        emoji3 = self.bot.get_emoji(instance3.countryball.emoji_id)
        emoji4 = self.bot.get_emoji(instance4.countryball.emoji_id)
        emoji5 = self.bot.get_emoji(instance5.countryball.emoji_id)
        emoji6 = self.bot.get_emoji(instance6.countryball.emoji_id)

        embed = discord.Embed(title=f"*{username}'s* **Mega Box**!", description=f"Mega Boxes give 10 whopping {settings.plural_collectible_name}!!", color=discord.Colour.gold())
        embed.add_field(name=f"x1 {emoji1} {cob1.name}", value=f"``💖{instance1.attack_bonus}`` ``⚔️{instance1.health_bonus}`` ``📦{instance1.special}``")
        embed.add_field(name=f"x1 {emoji2} {cob2.name}", value=f"``💖{instance2.attack_bonus}`` ``⚔️{instance2.health_bonus}`` ``📦{instance2.special}``")
        embed.add_field(name=f"x1 {emoji3} {cob3.name}", value=f"``💖{instance3.attack_bonus}`` ``⚔️{instance3.health_bonus}`` ``📦{instance3.special}``")
        embed.add_field(name=f"x1 {emoji4} {cob4.name}", value=f"``💖{instance4.attack_bonus}`` ``⚔️{instance4.health_bonus}`` ``📦{instance4.special}``")
        embed.add_field(name=f"x1 {emoji5} {cob5.name}", value=f"``💖{instance5.attack_bonus}`` ``⚔️{instance5.health_bonus}`` ``📦{instance5.special}``")
        embed.add_field(name=f"x1 {emoji6} {cob6.name}", value=f"``💖{instance6.attack_bonus}`` ``⚔️{instance6.health_bonus}`` ``📦{instance6.special}``")
        embed.set_thumbnail(url="") # Optional 
        embed.set_footer(text="Open your next box in # hours from this message.")

        await interaction.response.send_message(
            embed=embed,
            ephemeral=False
        )

    @app_commands.command(name="open_box", description="Open a loot-box!") # Change the command name here.
    async def open_box(self, interaction: discord.Interaction):
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
                        f'You cannot open a box for {hours} hour{"s" if hours != 1 else ""}, {minutes} minute{"s" if minutes != 1 else ""}, and {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                elif minutes > 0:
                    await interaction.response.send_message(
                        f'You cannot open a box for {minutes} minute{"s" if minutes != 1 else ""} and {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                else:
                    await interaction.response.send_message(
                        f'You cannot open a box for {seconds} second{"s" if seconds != 1 else ""}',
                        ephemeral=True
                    )
                return

        last_small_times[user_id] = now

        # Here we use percentage chance to determine what box you get when you use the command, 
        # you can change them by changing the value of the float to any number you'd like.
        # You can even add more limited time boxes by using this feature and make them really 
        # flippin rare! Just not too rare. Yikes.
        box_types = {
            "small": 0.50,
            "big": 0.35,
            "mega": 0.15
        }

        rand_num = random.choices(list(box_types.keys()), weights=box_types.values(), k=1)[0]
            
        if rand_num == "small":
            await self.small_box_rewards(interaction, box_type="small")
        elif rand_num == "big":
            await self.big_box_rewards(interaction, box_type="big")
        elif rand_num == "mega":
            await self.mega_box_rewards(interaction, box_type="mega")
            rand_num = random.choices(list(box_types.keys()), weights=box_types.values(), k=1)[0]


    @app_commands.command(name="box_stats", description="Get cooldowns & stats for your loot-boxes!")
    async def stats(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        now = datetime.now()
        box_special = await Special.get(pk=int("ID GOES HERE")) # REQUIRED!!! PLEASE!!! 
        player = await Player.get(discord_id=interaction.user.id).prefetch_related("balls")
        ball = await BallInstance.filter(player=player).prefetch_related("special", "trade_player")
        box_brawlers = [x for x in ball if x.special == box_special]
        user_obj = interaction.user

        bot_countryballs = {x: y.emoji_id for x, y in balls.items() if y.enabled}
        if user_id in last_small_times:
            last_small_time = last_small_times[user_id]
            elapsed_time = now - last_small_time

            if elapsed_time < SMALL_COOLDOWN:
                remaining_time = SMALL_COOLDOWN - elapsed_time
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)

                if hours > 0:
                    current_small = f"Box Cooldown: **{hours}:{minutes}:{seconds}**"

                elif minutes > 0:
                    current_small = f"Box Cooldown: **00:{minutes}:{seconds}**"

                else:
                    current_small = f"Box Cooldown: **00:00:{seconds}**"
            else:
                current_small = "***You can open your loot-boxes!!!***"

            last_small_times[user_id] = now
        else:
            current_small = "***You can open your loot-boxes!!!***"

        filters = {"player__discord_id": user_obj.id, "ball__enabled": True}
        filters["special"] = box_special
        bot_countryballs = {
            x: y.emoji_id
            for x, y in balls.items()
            if y.enabled and (box_special.end_date is None or y.created_at < box_special.end_date)
        }

        owned_countryballs = set(
            x[0]
            for x in await BallInstance.filter(**filters)
            .distinct()
            .values_list("ball_id")
        )

        total_countryballs = len(bot_countryballs)
        if total_countryballs > 0:
            completion_percentage = f"{round(len(owned_countryballs) / total_countryballs * 100, 1)}%"
        else:
            completion_percentage = "0.0%"

        if missing_countryballs := set(y for x, y in bot_countryballs.items() if x not in owned_countryballs):
            missing_percentage = f"{round(len(missing_countryballs) / total_countryballs * 100, 1)}%"
        else:
            missing_percentage = "0.0%"

        embed = discord.Embed(
            title=f"{interaction.user.display_name}'s Box Stats",
            color=discord.Colour.gold(),
        )

        embed.description = (
            "## ⌛ Cooldown ⌛\n"
            f"{current_small}\n"
            "### All Box Types:\n"
            "Small Boxes (50%)\n"
            "Big Boxes (35%)\n"
            "Mega Boxes (15%)\n"
            "## 📦 Box Stats 📦\n"
            f"**Total Box {settings.collectible_name.title()}s:** {len(box_brawlers):,}\n"
            f"**Discovered Box Brawlers:** {completion_percentage}\n"
            f"**Missing Box Brawlers:** {missing_percentage}\n"
            f"**Open your boxes every day and get lucky to increase these numbers!**"
        )
        embed.set_author(url=user_obj.display_avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=False)