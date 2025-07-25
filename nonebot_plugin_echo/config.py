from pathlib import Path

from ruamel.yaml import YAML
from pydantic import Field, BaseModel
from nonebot import get_driver, get_plugin_config
from pydantic_yaml import to_yaml_file, parse_yaml_file_as
from nonebot_plugin_localstore import get_plugin_config_dir

yaml = YAML(typ="safe")
yaml.default_flow_style = True

config_path = get_plugin_config_dir() / "config.yml"


class EchoConfig(BaseModel):
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.model_fields:
                self.__setattr__(key, value)


class EchoSceneConfig(EchoConfig):
    enable: bool = Field(default=True, alias="群聊学习开关")
    ban_words: list[str] = Field(default_factory=list, alias="屏蔽词")
    ban_users: list[int] = Field(default_factory=list, alias="屏蔽用户")
    reply_threshold: int = Field(default=4, alias="回复阈值")
    reply_threshold_weights: list[int] = Field(
        default=[10, 30, 60], alias="回复阈值权重"
    )
    repeat_threshold: int = Field(default=3, alias="复读阈值")
    break_repeat_probability: float = Field(default=0.25, alias="打断复读概率")
    speak_enable: bool = Field(default=True, alias="主动发言开关")
    speak_threshold: int = Field(default=5, alias="主动发言阈值")
    speak_min_interval: int = Field(default=300, alias="主动发言最小间隔")
    speak_continuously_probability: float = Field(default=0.5, alias="连续主动发言概率")
    speak_continuously_max_len: int = Field(default=3, alias="最大连续主动发言句数")
    speak_poke_probability: float = Field(default=0.5, alias="主动发言附带戳一戳概率")


class EchoGlobalConfig(EchoConfig):
    ban_words: list[str] = Field(default_factory=list, description="全局屏蔽词")
    ban_users: list[int] = Field(default_factory=list, description="全局屏蔽用户")
    sentence_keyword_count: int = Field(
        default=3,
        description="单句句关键词数量",
    )
    cross_scene_reply_threshold: int = Field(
        default=3,
        description="跨场景回复阈值",
    )
    learn_max_count: int = Field(default=6, alias="最高学习次数")
    dictionary: list[str] = Field(default_factory=list, description="自定义词典")
    scene_config: dict[str, EchoSceneConfig] = Field(
        default_factory=dict,
        description="场景配置",
    )


class EchoConfigManager:
    def __init__(self) -> None:
        self._cfg_path = Path(plugin_config.external_config)
        if self._cfg_path.exists():
            self._config = parse_yaml_file_as(EchoGlobalConfig, self._cfg_path)
        else:
            self._config = EchoGlobalConfig()
        self.save()

    def get_scene_config(self, scene_id: str) -> EchoSceneConfig:
        if scene_id not in self._config.scene_config:
            self._config.scene_config[scene_id] = EchoSceneConfig()
            self.save()
        return self._config.scene_config[scene_id]

    def get_global_config(self) -> EchoGlobalConfig:
        return self._config

    def save(self) -> None:
        to_yaml_file(self._cfg_path, self._config, custom_yaml_writer=yaml)


class ScopedConfig(BaseModel):
    enable_webui: bool = Field(default=True)
    external_config: str = Field(default=str(config_path))


class Config(BaseModel):
    echo: ScopedConfig = Field(default_factory=ScopedConfig)
    """Echo Plugin Config"""


global_config = get_driver().config
plugin_config = get_plugin_config(Config).echo

config_manager = EchoConfigManager()
