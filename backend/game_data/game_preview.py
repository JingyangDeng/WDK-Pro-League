from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from .player_snapshot import PlayerSnapshot
from .io import Deserializable


@dataclass
class GamePreview(Deserializable):
    """简略的游戏摘要"""

    players: List[PlayerSnapshot]
    """参与的玩家，按照座位顺序"""

    player_points: List[int]
    """每个玩家获得的点数（当盘游戏的点数，非玩家累计点数）"""

    game_date: Optional[datetime]
    """实际进行游戏的日期"""

    game_id: str
    """Index 所用的唯一 key"""

    pt_delta: List[int]
    """玩家获得的分数"""

    r_delta: List[float]
    """玩家获得的 R 分数"""
