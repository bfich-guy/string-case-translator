def pascal_to_camel(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in PascalCase and **returns camelCase**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        pascal_word_list: list[str] = list(variable_name)
        first_letter: str = pascal_word_list[0].lower()
        pascal_word_list[0] = first_letter

        result: str = "".join(pascal_word_list)
        return result
    except TypeError:
        return None

def pascal_to_kebab(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in PascalCase and **returns kebab-case**. 
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
    
def pascal_to_screaming(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in PascalCase and **returns SCREAMING_CASE**. 
    If there is an TypeError, function **returns None**. 
    """

    screaming_case_divider: str = "_"
    screaming_word_list: list[str] = []

    try:
        for index, character in enumerate(variable_name):
            character_is_in_upper_register: bool = character.isupper()
            upper_character: str = character.upper()

            if character_is_in_upper_register:
                index_is_greater_then_zero: bool = index > 0

                if index_is_greater_then_zero:
                    screaming_word_list.append(screaming_case_divider)
                    screaming_word_list.append(upper_character)

                else:
                    screaming_word_list.append(upper_character)

            else:
                screaming_word_list.append(upper_character)

        result: str = "".join(screaming_word_list)
        return result
    except TypeError:
        return None
    
def pascal_to_snake(*, variable_name: str) -> str | None:

    """
    This function gets variable name writed in PascalCase and **returns snake_case**. 
    If there is an TypeError, function **returns None**. 
    """

    try:
        snake_case_divider: str = "_"
        pascal_word_list: list[str] = []

        for index, character in enumerate(variable_name):
            character_is_in_upper_register: bool = character.isupper()
            lowered_character: str = character.lower()

            if character_is_in_upper_register:
                index_is_greater_then_zero: bool = index > 0

                if index_is_greater_then_zero:
                    pascal_word_list.append(snake_case_divider)
                    pascal_word_list.append(lowered_character)
                else:
                    pascal_word_list.append(lowered_character)

            else:
                pascal_word_list.append(lowered_character)

        result: str = "".join(pascal_word_list)
        return result
    except TypeError:
        return None