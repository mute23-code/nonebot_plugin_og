from typing import Union
from nonebot import on_message
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot_plugin_guild_patch import Bot, GuildMessageEvent
from .utils import get_og_info

__plugin_meta__ = PluginMetadata(
    name="og",
    description="检测链接并发送网站简介及预览图",
    usage="无",
    extra={
        "Author": "mute. <mute231010@gmail.com>",
        "version": "v0.1.0"
    },
)


get_og = on_message(priority=99)

@get_og.handle()
async def get_og(bot: Bot, event: Union[MessageEvent, GuildMessageEvent]):
    og_info = await get_og_info(event.message)
    if og_info:
        title = og_info.get('title', '未知标题')
        desc = og_info.get('description', '未提供描述信息')
        img = og_info.get('image', None)
        if img:
            msg = f'{img}\n{title}\n{desc}'
        else:
            msg = f'{title}\n{desc}'
        await bot.send(event, message=msg)