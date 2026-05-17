def kebab_to_snake(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in kebab-case and **returns snake_case**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        snake_case_divider: str = "_"
        kebab_case_divider: str = "-"

        result: str = variable_name.replace(kebab_case_divider, snake_case_divider).lower()
        return result
    except TypeError:
        return None
    
def kebab_to_pascal(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in kebab-case and **returns PascalCase**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        kebab_case_divider: str = "-"
        kebab_word_list: list[str] = variable_name.split(kebab_case_divider)
        pascal_word_list: list[str] = []

        for kebab_word in kebab_word_list:
            pascal_word: str = kebab_word.capitalize()
            pascal_word_list.append(pascal_word)

        result: str = "".join(pascal_word_list)
        return result
    except TypeError:
        return None
    
def kebab_to_camel(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in kebab-case and **returns camelCase**. 
    If there is an TypeError or IndexError, function **returns None**. 
    """

    try:
        kebab_case_divider: str = "-"
        kebab_word_list: list[str] = variable_name.split(kebab_case_divider)
        camel_word_list: list[str] = []

        first_word: str = kebab_word_list[0].lower()
        camel_word_list.append(first_word)
        del kebab_word_list[0]

        for kebab_word in kebab_word_list:
            camel_word: str = kebab_word.capitalize()
            camel_word_list.append(camel_word)

        result: str = "".join(camel_word_list)
        return result
    except (TypeError, IndexError):
        return None
    
