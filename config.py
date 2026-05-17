from Cases.camel_case import camel_to_kebab, camel_to_snake, camel_to_pascal
from Cases.kebab_case import kebab_to_camel, kebab_to_pascal, kebab_to_snake
from Cases.pascal_case import pascal_to_camel, pascal_to_kebab, pascal_to_snake
from Cases.snake_case import snake_to_camel, snake_to_kebab, snake_to_pascal
from typing import Callable

cases_registry: dict[str, Callable] = {

    "camel_to_kebab": camel_to_kebab,
    "camel_to_snake": camel_to_snake,
    "camel_to_pascal": camel_to_pascal,
    "kebab_to_camel": kebab_to_camel,
    "kebab_to_pascal": kebab_to_pascal,
    "kebab_to_snake": kebab_to_snake,
    "pascal_to_camel": pascal_to_camel,
    "pascal_to_kebab": pascal_to_kebab,
    "pascal_to_snake": pascal_to_snake,
    "snake_to_camel": snake_to_camel,
    "snake_to_kebab": snake_to_kebab,
    "snake_to_pascal": snake_to_pascal

}