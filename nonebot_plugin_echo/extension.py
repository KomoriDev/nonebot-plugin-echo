from nonebot import logger
from nonebot.adapters import Bot, Event
from nonebot_plugin_alconna import Alconna, Extension, UniMessage


class MessageReceiveExtension(Extension):
    @property
    def priority(self) -> int:
        return 15

    @property
    def id(self) -> str:
        return "MessageReceiveExtension"

    async def receive_wrapper(
        self, bot: Bot, event: Event, command: Alconna, receive: UniMessage
    ) -> UniMessage:
        logger.trace(f"Bot {bot.adapter.get_name()} {bot.self_id} received msg")

        return receive
