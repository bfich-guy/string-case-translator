from Cases.camel_case import camel_to_kebab, camel_to_pascal, camel_to_screaming, camel_to_snake
from Cases.kebab_case import kebab_to_camel, kebab_to_pascal, kebab_to_screaming, kebab_to_snake
from Cases.pascal_case import pascal_to_camel, pascal_to_kebab, pascal_to_screaming, pascal_to_snake
from Cases.screaming_case import screaming_to_camel, screaming_to_kebab, screaming_to_pascal, screaming_to_snake
from Cases.snake_case import snake_to_camel, snake_to_kebab, snake_to_pascal, snake_to_screaming
from typing import Callable

cases_registry: dict[str, Callable] = {

    "camelkebab": camel_to_kebab,
    "camelpascal": camel_to_pascal,
    "camelscreaming": camel_to_screaming,
    "camelsnake": camel_to_snake,

    "kebabcamel": kebab_to_camel,
    "kebabpascal": kebab_to_pascal,
    "kebabscreaming": kebab_to_screaming,
    "kebabsnake": kebab_to_snake,

    "pascalcamel": pascal_to_camel,
    "pascalkebab": pascal_to_kebab,
    "pascalscreaming": pascal_to_screaming,
    "pascalsnake": pascal_to_snake,

    "screamingcamel": screaming_to_camel,
    "screamingkebab": screaming_to_kebab,
    "screamingpascal": screaming_to_pascal,
    "screamingsnake": screaming_to_snake,

    "snakecamel": snake_to_camel,
    "snakekebab": snake_to_kebab,
    "snakepascal": snake_to_pascal,
    "snakescreaming": snake_to_screaming,

}