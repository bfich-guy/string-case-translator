from typing import Callable

from string_case_translator.config.case_dividers import CaseDividersNames

from string_case_translator.cases.camel import camel_to_dot, camel_to_kebab, camel_to_pascal, camel_to_path, camel_to_screaming, camel_to_snake, camel_to_train
from string_case_translator.cases.dot import dot_to_camel, dot_to_kebab, dot_to_pascal, dot_to_path, dot_to_screaming, dot_to_snake, dot_to_train
from string_case_translator.cases.kebab import kebab_to_camel, kebab_to_dot, kebab_to_screaming, kebab_to_pascal, kebab_to_path, kebab_to_snake, kebab_to_train
from string_case_translator.cases.pascal import pascal_to_camel, pascal_to_dot, pascal_to_kebab, pascal_to_path, pascal_to_screaming, pascal_to_snake, pascal_to_train
from string_case_translator.cases.path import path_to_camel, path_to_dot, path_to_kebab, path_to_pascal, path_to_screaming, path_to_snake, path_to_train
from string_case_translator.cases.screaming import screaming_to_camel, screaming_to_dot, screaming_to_kebab, screaming_to_pascal, screaming_to_path, screaming_to_snake, screaming_to_train
from string_case_translator.cases.snake import snake_to_camel, snake_to_dot, snake_to_kebab, snake_to_pascal, snake_to_path, snake_to_screaming, snake_to_train
from string_case_translator.cases.train import train_to_camel, train_to_dot, train_to_kebab, train_to_pascal, train_to_path, train_to_screaming, train_to_snake


case_registry: dict[tuple, Callable] = {
    
    (CaseDividersNames.CAMEL.value, CaseDividersNames.DOT.value): camel_to_dot,
    (CaseDividersNames.CAMEL.value, CaseDividersNames.KEBAB.value): camel_to_kebab,
    (CaseDividersNames.CAMEL.value, CaseDividersNames.PASCAL.value): camel_to_pascal,
    (CaseDividersNames.CAMEL.value, CaseDividersNames.PATH.value): camel_to_path,
    (CaseDividersNames.CAMEL.value, CaseDividersNames.SCREAMING.value): camel_to_screaming,
    (CaseDividersNames.CAMEL.value, CaseDividersNames.SNAKE.value): camel_to_snake,
    (CaseDividersNames.CAMEL.value, CaseDividersNames.TRAIN.value): camel_to_train,

    (CaseDividersNames.DOT.value, CaseDividersNames.CAMEL.value): dot_to_camel,
    (CaseDividersNames.DOT.value, CaseDividersNames.KEBAB.value): dot_to_kebab,
    (CaseDividersNames.DOT.value, CaseDividersNames.PASCAL.value): dot_to_pascal,
    (CaseDividersNames.DOT.value, CaseDividersNames.PATH.value): dot_to_path,
    (CaseDividersNames.DOT.value, CaseDividersNames.SCREAMING.value): dot_to_screaming,
    (CaseDividersNames.DOT.value, CaseDividersNames.SNAKE.value): dot_to_snake,
    (CaseDividersNames.DOT.value, CaseDividersNames.TRAIN.value): dot_to_train,

    (CaseDividersNames.KEBAB.value, CaseDividersNames.CAMEL.value): kebab_to_camel,
    (CaseDividersNames.KEBAB.value, CaseDividersNames.DOT.value): kebab_to_dot,
    (CaseDividersNames.KEBAB.value, CaseDividersNames.SCREAMING.value): kebab_to_screaming,
    (CaseDividersNames.KEBAB.value, CaseDividersNames.PASCAL.value): kebab_to_pascal,
    (CaseDividersNames.KEBAB.value, CaseDividersNames.PATH.value): kebab_to_path,
    (CaseDividersNames.KEBAB.value, CaseDividersNames.SNAKE.value): kebab_to_snake,
    (CaseDividersNames.KEBAB.value, CaseDividersNames.TRAIN.value): kebab_to_train,

    (CaseDividersNames.PASCAL.value, CaseDividersNames.CAMEL.value): pascal_to_camel,
    (CaseDividersNames.PASCAL.value, CaseDividersNames.DOT.value): pascal_to_dot,
    (CaseDividersNames.PASCAL.value, CaseDividersNames.KEBAB.value): pascal_to_kebab,
    (CaseDividersNames.PASCAL.value, CaseDividersNames.PATH.value): pascal_to_path,
    (CaseDividersNames.PASCAL.value, CaseDividersNames.SCREAMING.value): pascal_to_screaming,
    (CaseDividersNames.PASCAL.value, CaseDividersNames.SNAKE.value): pascal_to_snake,
    (CaseDividersNames.PASCAL.value, CaseDividersNames.TRAIN.value): pascal_to_train,

    (CaseDividersNames.PATH.value, CaseDividersNames.CAMEL.value): path_to_camel,
    (CaseDividersNames.PATH.value, CaseDividersNames.DOT.value): path_to_dot,
    (CaseDividersNames.PATH.value, CaseDividersNames.KEBAB.value): path_to_kebab,
    (CaseDividersNames.PATH.value, CaseDividersNames.PASCAL.value): path_to_pascal,
    (CaseDividersNames.PATH.value, CaseDividersNames.SCREAMING.value): path_to_screaming,
    (CaseDividersNames.PATH.value, CaseDividersNames.SNAKE.value): path_to_snake,
    (CaseDividersNames.PATH.value, CaseDividersNames.TRAIN.value): path_to_train,

    (CaseDividersNames.SCREAMING.value, CaseDividersNames.CAMEL.value): screaming_to_camel,
    (CaseDividersNames.SCREAMING.value, CaseDividersNames.DOT.value): screaming_to_dot,
    (CaseDividersNames.SCREAMING.value, CaseDividersNames.KEBAB.value): screaming_to_kebab,
    (CaseDividersNames.SCREAMING.value, CaseDividersNames.PASCAL.value): screaming_to_pascal,
    (CaseDividersNames.SCREAMING.value, CaseDividersNames.PATH.value): screaming_to_path,
    (CaseDividersNames.SCREAMING.value, CaseDividersNames.SNAKE.value): screaming_to_snake,
    (CaseDividersNames.SCREAMING.value, CaseDividersNames.TRAIN.value): screaming_to_train,

    (CaseDividersNames.SNAKE.value, CaseDividersNames.CAMEL.value): snake_to_camel,
    (CaseDividersNames.SNAKE.value, CaseDividersNames.DOT.value): snake_to_dot,
    (CaseDividersNames.SNAKE.value, CaseDividersNames.KEBAB.value): snake_to_kebab,
    (CaseDividersNames.SNAKE.value, CaseDividersNames.PASCAL.value): snake_to_pascal,
    (CaseDividersNames.SNAKE.value, CaseDividersNames.PATH.value): snake_to_path,
    (CaseDividersNames.SNAKE.value, CaseDividersNames.SCREAMING.value): snake_to_screaming,
    (CaseDividersNames.SNAKE.value, CaseDividersNames.TRAIN.value): snake_to_train,

    (CaseDividersNames.TRAIN.value, CaseDividersNames.CAMEL.value): train_to_camel,
    (CaseDividersNames.TRAIN.value, CaseDividersNames.DOT.value): train_to_dot,
    (CaseDividersNames.TRAIN.value, CaseDividersNames.KEBAB.value): train_to_kebab,
    (CaseDividersNames.TRAIN.value, CaseDividersNames.PASCAL.value): train_to_pascal,
    (CaseDividersNames.TRAIN.value, CaseDividersNames.PATH.value): train_to_path,
    (CaseDividersNames.TRAIN.value, CaseDividersNames.SCREAMING.value): train_to_screaming,
    (CaseDividersNames.TRAIN.value, CaseDividersNames.SNAKE.value): train_to_snake,

}

