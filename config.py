from dataclasses import dataclass
from typing import Set

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(frozen=True)
class Config:
    message: str
    debug: bool
    servers: Set[str]