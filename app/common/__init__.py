from enum import Enum

from app.common.databases import db, Base


class StringEnum(str, Enum):
    """Enum where members are also (and must be) strings"""

    @classmethod
    def values(cls):
        return tuple(item.value for item in list(cls))
