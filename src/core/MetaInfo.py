from dataclasses import dataclass


@dataclass
class MetaInfo:
    line: int
    column: int

    @classmethod
    def from_lark(cls, meta):
        return MetaInfo(meta.line, meta.column)
