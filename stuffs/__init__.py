from typing import TYPE_CHECKING

from ballsdex.packages.boxes.cog import Boxes

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot


async def setup(bot: "BallsDexBot"):
    await bot.add_cog(Boxes(bot))