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
    """
    
    try:
        function_name: str = current_case + wanted_case

        result: str | None = cases_registry[function_name](variable_name=variable_name)
        return result
    except KeyError:
        return None