from dataclasses import dataclass, field
from typing import List, Optional, Any


# -------------------------
# Базовые классы
# -------------------------

class Statement:
    """
    Базовый класс для всех операторов сценария.
    """
    pass


@dataclass
class Script:
    """
    Весь сценарий Ren'Py.
    """
    labels: dict[str, "Label"] = field(default_factory=dict)

    def add_label(self, label: "Label"):
        self.labels[label.name] = label


# -------------------------
# Структурные элементы
# -------------------------

@dataclass
class Label(Statement):
    """
    label start:
    """
    name: str
    body: List[Statement] = field(default_factory=list)


@dataclass
class Jump(Statement):
    """
    jump end
    """
    target: str


# -------------------------
# Диалоги и выборы
# -------------------------

@dataclass
class Say(Statement):
    """
    "Hello world"
    """
    text: str
    character: Optional[str] = None


@dataclass
class Menu(Statement):
    """
    menu:
        "Option 1":
            jump a
    """
    options: List["MenuOption"] = field(default_factory=list)


@dataclass
class MenuOption:
    text: str
    body: List[Statement] = field(default_factory=list)


# -------------------------
# Переменные и условия
# -------------------------

@dataclass
class Assignment(Statement):
    """
    $ flag = True
    """
    variable: str
    value: Any


@dataclass
class Condition(Statement):
    """
    if flag:
        jump a
    """
    expression: str
    body: List[Statement] = field(default_factory=list)
    else_body: List[Statement] = field(default_factory=list)
