from dataclasses import dataclass, field
from typing import List, Optional, Any, Tuple


# -------------------------
# Базовые классы
# -------------------------

class Statement:
    line: Optional[int] = None
    column: Optional[int] = None


@dataclass
class Script:
    labels: dict[str, "Label"] = field(default_factory=dict)

    def add_label(self, label: "Label"):
        self.labels[label.name] = label


# -------------------------
# Структура
# -------------------------

@dataclass
class Label(Statement):
    name: str
    body: List[Statement] = field(default_factory=list)
    line: Optional[int] = None
    column: Optional[int] = None


@dataclass
class Jump(Statement):
    target: str
    line: Optional[int] = None
    column: Optional[int] = None


# -------------------------
# Диалоги
# -------------------------

@dataclass
class Say(Statement):
    text: str
    character: Optional[str] = None
    line: Optional[int] = None
    column: Optional[int] = None


@dataclass
class Menu(Statement):
    options: List["MenuOption"] = field(default_factory=list)
    line: Optional[int] = None
    column: Optional[int] = None


@dataclass
class MenuOption:
    text: str
    body: List[Statement] = field(default_factory=list)
    line: Optional[int] = None
    column: Optional[int] = None


# -------------------------
# СОСТОЯНИЯ
# -------------------------

@dataclass
class Assignment(Statement):
    var: str
    op: str
    value: int
    line: Optional[int] = None
    column: Optional[int] = None


@dataclass
class Condition(Statement):
    var: str
    op: str
    value: int
    body: List[Statement] = field(default_factory=list)
    line: Optional[int] = None
    column: Optional[int] = None


@dataclass
class UnknownStatement(Statement):
    source: str
    line: Optional[int] = None
    column: Optional[int] = None
    error_message: str = ""