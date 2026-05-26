from enum import Enum

class CaseDividersNames(Enum):
    CAMEL = "CAMEL"
    DOT = "DOT"
    KEBAB = "KEBAB"
    PASCAL = "PASCAL"
    PATH = "PATH"
    SCREAMING = "SCREAMING"
    SNAKE = "SNAKE"
    TRAIN = "TRAIN"

case_dividers_dict: dict[str, str] = {
    CaseDividersNames.CAMEL.value: "",
    CaseDividersNames.DOT.value: ".",
    CaseDividersNames.KEBAB.value: "-",
    CaseDividersNames.PASCAL.value: "",
    CaseDividersNames.PATH.value: "/",
    CaseDividersNames.SCREAMING.value: "_",
    CaseDividersNames.SNAKE.value: "_",
    CaseDividersNames.TRAIN.value: "-",
}