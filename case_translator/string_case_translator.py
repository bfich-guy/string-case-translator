from config import cases_registry
from typing import Callable

def translate_string_case(*,
                          variable_name: str,
                          current_case: str,
                          wanted_case: str,
                          cases_registry: dict[str, Callable] = cases_registry
                          ) -> str | None:
    
    """
    This function gets variable name, its current case and wanted case (the case you need) and **returns name of variable in wanted case**.
    Supported registries are: **camel**, **kebab**, **pascal**, **screaming**, **snake**. 
    If function gets arguments that are not in supported cases, it **returns None**. 

    Usage Example
    -------------

    print(translate_string_case(variable_name="SCREAMING_TO_PASCAL", current_case="screaming", wanted_case="pascal"))
    >>> ScreamingToPascal
    
    print(translate_string_case(variable_name="camelToKebab", current_case="is_is_obviously_camel_dont_you_see", wanted_case="just_read_the_last_word"))
    >>> None

    Features
    --------

    Library string_case_translator uses the WET pattern, so a **single point of failure is impossible**. 
    
    This function uses built-in C-methods in python, so **it works faster** than regular expressions. 

    Unique Selling Proposition (USP)
    ----------------------------

    This function and library propose **high speed, easy usage and localized potential bugs**. 
    """
    
    try:
        function_name: str = current_case + wanted_case

        result: str | None = cases_registry[function_name](variable_name=variable_name)
        return result
    except KeyError:
        return None