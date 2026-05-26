from string_case_translator.config.case_registry import case_registry

def translate_string_case(*,
                          variable_name: str,
                          current_case: str,
                          target_case: str,
                          ) -> str | None:
    
    """Returns string with changed case

    This function **gets** variable name, target case and wanted case. 
    It **connects** current case and target case into tuple and **uses** the needed function from dictionary. 
    Supported cases: **CAMEL, DOT, KEBAB, PASCAL, PATH, SCREAMING, SNAKE, TRAIN**. 

    Args:
        variable_name (str): **A variable name**. 
        current_case (str): **A case** of variable name. 
        target_case (str): **A case** that is need for variable name. 

    Returns:
        str | None: **Variable name** with changed case or **None** if KeyError occurs. 

    Examples:
        >>> translate_string_case(variable_name='snake_to_pascal', current_case='SNAKE', target_case='PASCAL')
        'FirstTry'

        >>> translate_string_case(variable_name='__IaMdRuNk__', current_case='__uh?', target_case='__just_READ_IT_somehow!!!__')
        None
    """
    
    needed_case: tuple[str, str] = (current_case, target_case)
    
    try:
        result: str | None = case_registry[needed_case](variable_name=variable_name)
        return result
    except KeyError:
        return None
    
