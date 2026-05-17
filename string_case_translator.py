from config import cases_registry
from typing import Callable

def string_case_translator(*, 
                           variable_name: str,
                           current_case: str,
                           wanted_case: str,
                           cases_registry: dict[str, Callable] = cases_registry
                           ) -> str | None:
    
    """
    This funtcion gets variable name, it current case and wanted case (that case you needed) and **returns name of variable in wanted case**. 
    Supported registry are: **camel**, **kebab**, **pascal**, **snake**. 
    If function gets arguments that are not in supported cases, it **returns None**. 
    """
    
    try:
        function_name: str = current_case + "_to_" + wanted_case

        result: str | None = cases_registry[function_name](variable_name=variable_name)
        return result
    except KeyError:
        return None