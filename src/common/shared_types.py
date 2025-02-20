"""Types shared across the chord generator modules"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, NamedTuple

from src.common.layout import KeyPosition


class OutputFormat(Enum):
    """Supported output formats for chord generation"""

    STANDARD_JSON = auto()


@dataclass
class WordData:
    """Represents preprocessed data for a word"""

    original: str
    lower: str
    length: int
    zipf_weight: float


class ChordData(NamedTuple):
    """Represents preprocessed data for a chord"""

    letters: str
    keys: tuple[KeyPosition, ...]
    length: int


@dataclass
class SetData:
    """Represents preprocessed data for a set of assignments"""

    length: int
    assignments: Dict[WordData, ChordData]


class StandaloneMetricType(Enum):
    """Types of metrics for standalone chord analysis"""

    CHORD_LENGTH = auto()
    HORIZONTAL_PINCH = auto()
    HORIZONTAL_STRETCH = auto()
    VERTICAL_PINCH = auto()
    VERTICAL_STRETCH = auto()
    DIAGONAL_DOWNWARD_PINCH = auto()
    DIAGONAL_DOWNWARD_STRETCH = auto()
    DIAGONAL_UPWARD_PINCH = auto()
    DIAGONAL_UPWARD_STRETCH = auto()
    SAME_FINGER_DOUBLE_ADJACENT = auto()
    SAME_FINGER_DOUBLE_GAP = auto()
    SAME_FINGER_TRIPLE = auto()
    FULL_SCISSOR_DOUBLE = auto()
    FULL_SCISSOR_TRIPLE = auto()
    FULL_SCISSOR_QUADRUPLE = auto()
    FULL_SCISSOR_QUINTUPLE = auto()
    HALF_SCISSOR_DOUBLE = auto()
    HORIZONTAL_STRETCH_DOUBLE = auto()
    PINKY_RING_SCISSOR = auto()
    RING_INDEX_SCISSOR = auto()


class AssignmentMetricType(Enum):
    """Types of metrics for word-chord assignments"""

    FIRST_LETTER_UNMATCHED = auto()
    SECOND_LETTER_UNMATCHED = auto()
    LAST_LETTER_UNMATCHED = auto()
    PHONETIC_DISSIMILARITY = auto()
    EXTRA_LETTER = auto()


class SetMetricType(Enum):
    """Types of metrics for sets of assignments"""

    FINGER_UTILIZATION = auto()
    HAND_UTILIZATION = auto()
    CHORD_PATTERN_CONSISTENCY = auto()


@dataclass
class StandaloneMetrics:
    """Metrics for evaluating individual chords"""

    costs: Dict[StandaloneMetricType, float]


@dataclass
class AssignmentMetrics:
    """Metrics for evaluating word-chord assignments"""

    costs: Dict[AssignmentMetricType, float]
    word_frequency: float  # From Zipf's law


@dataclass
class SetMetrics:
    """Metrics for evaluating sets of assignments"""

    costs: Dict[SetMetricType, float]
