def screaming_to_camel(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in SCREAMING_CASE and **returns camelCase**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        
        screaming_case_divider: str = "_"
        screaming_word_list: list[str] = variable_name.split(screaming_case_divider)
        camel_word_list: list[str] = []

        first_word: str = screaming_word_list[0].lower()
        camel_word_list.append(first_word)
        del screaming_word_list[0]
        

        for screaming_word in screaming_word_list:
            camel_word: str = screaming_word.capitalize()
            camel_word_list.append(camel_word)

        result: str = "".join(camel_word_list)
        return result
    except TypeError:
        return None
    
def screaming_to_kebab(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in SCREAMING_CASE and **returns kebab-case**. 
    If there is an TypeError, function **returns None**. 
    """

    try:     
        screaming_case_divider: str = "_"
        kebab_case_divider: str = "-"
        screaming_word_list: list[str] = variable_name.split(screaming_case_divider)
        kebab_word_list: list[str] = []

        for screaming_word in screaming_word_list:
            kebab_word: str = screaming_word.lower()
            kebab_word_list.append(kebab_word)

        result: str = kebab_case_divider.join(kebab_word_list)
        return result
    except TypeError:
        return None
    
def screaming_to_pascal(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in SCREAMING_CASE and **returns PascalCase**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        screaming_case_divider: str = "_"
        screaming_word_list: list[str] = variable_name.split(screaming_case_divider)
        pascal_word_list: list[str] = []

        for screaming_word in screaming_word_list:
            pascal_word: str = screaming_word.capitalize()
            pascal_word_list.append(pascal_word)

        result: str = "".join(pascal_word_list)
        return result
    except TypeError:
        return None
    
def screaming_to_snake(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in SCREAMING_CASE and **returns snake_case**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        screaming_case_divider: str = "_"
        screaming_word_list: list[str] = variable_name.split(screaming_case_divider)
        snake_word_list: list[str] = []

        for screaming_word in screaming_word_list:
            snake_word: str = screaming_word.lower()
            snake_word_list.append(snake_word)

        result: str = screaming_case_divider.join(snake_word_list)
        return result
    except TypeError:
        return None