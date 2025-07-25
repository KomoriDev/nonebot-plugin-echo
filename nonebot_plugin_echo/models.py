from datetime import datetime

from nonebot_plugin_orm import Model
from sqlalchemy import JSON, Text, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column


class ChatContext(Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    keywords: Mapped[str] = mapped_column(Text)
    time: Mapped[int] = mapped_column(
        BigInteger, default=lambda: int(datetime.now().timestamp())
    )
    count: Mapped[int] = mapped_column(default=1)
    answers: Mapped[list["ChatAnswer"]] = relationship(
        "ChatAnswer", back_populates="context", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<ChatContext(id={self.id}, keywords='{self.keywords}', time={self.time}, count={self.count})>"  # noqa: E501


class ChatAnswer(Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    keywords: Mapped[str] = mapped_column(Text)
    scene_id: Mapped[int] = mapped_column()
    count: Mapped[int] = mapped_column(default=1)
    time: Mapped[int] = mapped_column(
        BigInteger, default=lambda: int(datetime.now().timestamp())
    )
    messages: Mapped[list[str]] = mapped_column(JSON, default=[])

    context_id: Mapped[int] = mapped_column(
        ForeignKey("nonebot_plugin_echo_chatcontext.id"), nullable=True
    )
    context: Mapped["ChatContext"] = relationship(
        "ChatContext", back_populates="answers"
    )

    def __repr__(self):
        return f"<ChatAnswer(id={self.id}, keywords='{self.keywords}', scene_id={self.scene_id}, count={self.count}, time={self.time})>"  # noqa: E501


class ChatBlackList(Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    keywords: Mapped[str] = mapped_column(Text)
    is_global: Mapped[bool] = mapped_column(default=False)
    ban_scene_id: Mapped[list[str]] = mapped_column(JSON, default=[])

    def __repr__(self):
        return f"<ChatBlackList(id={self.id}, keywords='{self.keywords}', is_global={self.is_global}, ban_scene_id={self.ban_scene_id})>"  # noqa: E501
