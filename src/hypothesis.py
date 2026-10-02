from dataclasses import dataclass, field
from typing import List


@dataclass
class Hypothesis:
    id: str
    cause: str
    assumptions: List[str] = field(default_factory=list)
    predicted_effects: List[str] = field(default_factory=list)
    required_evidence: List[str] = field(default_factory=list)