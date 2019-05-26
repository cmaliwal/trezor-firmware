# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .NEMMosaicDefinition import NEMMosaicDefinition


class NEMMosaicCreation(p.MessageType):

    def __init__(
        self,
        definition: NEMMosaicDefinition = None,
        sink: str = None,
        fee: int = None,
    ) -> None:
        self.definition = definition
        self.sink = sink
        self.fee = fee

    @classmethod
    def get_fields(cls):
        return {
            1: ('definition', NEMMosaicDefinition, 0),
            2: ('sink', p.UnicodeType, 0),
            3: ('fee', p.UVarintType, 0),
        }