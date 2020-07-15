from dataclasses import dataclass
from typing import List, Optional

from xml_dataclasses import xml_dataclass, rename, XmlDataclass


@xml_dataclass
@dataclass
class Time(XmlDataclass):
    __ns__ = None
    real_time: str = rename(name="RealTime")


@xml_dataclass
@dataclass
class Segment(XmlDataclass):
    __ns__ = None
    name: str = rename(name="Name")
    icon: str = rename(name="Icon")
    segment_history: List[Time] = rename(name="segment_history")


@xml_dataclass
@dataclass
class Run(XmlDataclass):
    __ns__ = None
    game_icon: str = rename(name="GameIcon")
    game_name: str = rename(name="GameName")
    category_name: str = rename(name="CategoryName")
    offset: str = rename(name="Offset")
    attempt_count: str = rename(name="AttemptCount")
    segments: List[Segment] = rename(name="Segments")