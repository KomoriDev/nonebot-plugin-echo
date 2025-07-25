from enum import Enum

from .config import global_config

NICKNAME = list(global_config.nickname)[0]

NO_PERMISSION_WORDS = [f"{NICKNAME}就喜欢说这个，哼！", f"你管得着{NICKNAME}吗！"]
ENABLE_WORDS = [
    f"{NICKNAME}会尝试学你们说怪话！",
    f"好的呢，让{NICKNAME}学学你们的说话方式~",
]
DISABLE_WORDS = [
    f"好好好，{NICKNAME}不学说话就是了！",
    f"果面呐噻，{NICKNAME}以后不学了...",
]
SORRY_WORDS = [
    f"{NICKNAME}知道错了...达咩!",
    f"{NICKNAME}不会再这么说了...",
    f"果面呐噻,{NICKNAME}说错话了...",
]
DOUBT_WORDS = [f"{NICKNAME}有说什么奇怪的话吗？"]
BREAK_REPEAT_WORDS = ["打断复读", "打断！"]
ALL_WORDS = (
    NO_PERMISSION_WORDS
    + SORRY_WORDS
    + DOUBT_WORDS
    + ENABLE_WORDS
    + DISABLE_WORDS
    + BREAK_REPEAT_WORDS
)


class EchoAction(str, Enum):
    learn = "learn"
    """学习群友的发言"""
    ignore = "ignore"
    """不学习群友的发言"""
    repeat = "repeat"
    """复读群友的发言"""
    ban = "ban"
    """屏蔽群友的发言"""
    set_enable = "set_enable"
    """开启学习群友的指令"""
    set_disable = "set_disable"
    """关闭学习群友的指令"""
