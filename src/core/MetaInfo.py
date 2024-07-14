from dataclasses import dataclass

from lark.tree import Meta

@dataclass(kw_only=True)
class MetaInfo:

    meta:Meta

    @classmethod
    def from_lark(cls, meta):
        return MetaInfo(meta=meta)
    
    @property
    def line(self):
        return self.meta.line

    @property
    def column(self):
        return self.meta.column