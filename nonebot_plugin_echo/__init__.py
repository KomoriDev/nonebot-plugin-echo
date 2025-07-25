from nonebot.plugin import PluginMetadata, require

require("nonebot_plugin_orm")
require("nonebot_plugin_alconna")
require("nonebot_plugin_localstore")
from nonebot_plugin_alconna import Command

from . import migrations
from .config import Config
from .version import __version__
from .extension import MessageReceiveExtension

__plugin_meta__ = PluginMetadata(
    name="群聊学习",
    description="学习群友们的发言、复读以及主动发言",
    usage="/echo -h|--help",
    type="application",
    homepage="https://github.com/KomoriDev/nonebot-plugin-echo",
    config=Config,
    supported_adapters=None,
    extra={
        "unique_name": "Echo",
        "orm_version_location": migrations,
        "author": "Komorebi <mute231010@gmail.com>",
        "version": __version__,
    },
)

echo = (
    Command("echo")
    .config(hide=True)
    .build(use_cmd_start=True, extensions=[MessageReceiveExtension])
)
