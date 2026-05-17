def camel_to_snake(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in camelCase and **returns snake_case**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        
        snake_case_divider: str = "_"
        snake_word_list: list[str] = []

        for character in variable_name:
            character_is_in_upper_register: bool = character.isupper()
            lowered_character: str = character.lower()

            if character_is_in_upper_register:
                snake_word_list.append(snake_case_divider)
                snake_word_list.append(lowered_character)

            else:
                snake_word_list.append(lowered_character)

        result: str = "".join(snake_word_list)
        return result
        
    except TypeError:
        return None
    
def camel_to_pascal(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in camelCase and **returns PascalCase**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        pascal_word_list: list[str] = list(variable_name)
        first_letter: str = pascal_word_list[0].upper()
        pascal_word_list[0] = first_letter

        result: str = "".join(pascal_word_list)
        return result
    except TypeError:
        return None
    
def camel_to_kebab(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in camelCase and **returns kebab-case**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        kebab_case_divider: str = "-"
        kebab_word_list: list[str] = []

        for index, character in enumerate(variable_name):
            character_is_in_upper_register: bool = character.isupper()
            lowered_character: str = character.lower()

            if character_is_in_upper_register:
                index_is_greater_then_zero: bool = index > 0

                if index_is_greater_then_zero:
                    kebab_word_list.append(kebab_case_divider)
                    kebab_word_list.append(lowered_character)
                else:
                    kebab_word_list.append(lowered_character)

            else:
                kebab_word_list.append(lowered_character)

        result: str = "".join(kebab_word_list)
        return result
    except TypeError:
        return None