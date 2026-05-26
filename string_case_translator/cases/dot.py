from string_case_translator.utils import get_string_list_of_delimiter_case, connect_strings_with_divider
from string_case_translator.config.case_dividers import CaseDividersNames, case_dividers_dict

def dot_to_camel(*, variable_name: str) -> str | None:

    dot_divider: str = case_dividers_dict[CaseDividersNames.DOT.value]
    dot_word_list: list[str] | None = get_string_list_of_delimiter_case(variable_name=variable_name, divider=dot_divider)

    if dot_word_list is None:
        return None
    
    camel_divider: str = case_dividers_dict[CaseDividersNames.CAMEL.value]
    camel_word_list: list[str] = [dot_word.capitalize() if index > 0 else dot_word.lower() for index, dot_word in enumerate(dot_word_list)]

    result: str | None = connect_strings_with_divider(string_list=camel_word_list, divider=camel_divider)
    return result

def dot_to_kebab(*, variable_name: str) -> str | None:

    dot_divider: str = case_dividers_dict[CaseDividersNames.DOT.value]
    dot_word_list: list[str] | None = get_string_list_of_delimiter_case(variable_name=variable_name, divider=dot_divider)

    if dot_word_list is None:
        return None
    
    kebab_divider: str = case_dividers_dict[CaseDividersNames.KEBAB.value]
    kebab_word_list: list[str] = [dot_word.lower() for dot_word in dot_word_list]

    result: str | None = connect_strings_with_divider(string_list=kebab_word_list, divider=kebab_divider)
    return result

def dot_to_pascal(*, variable_name: str) -> str | None:

    dot_divider: str = case_dividers_dict[CaseDividersNames.DOT.value]
    dot_word_list: list[str] | None = get_string_list_of_delimiter_case(variable_name=variable_name, divider=dot_divider)

    if dot_word_list is None:
        return None
    
    pascal_divider: str = case_dividers_dict[CaseDividersNames.PASCAL.value]
    pascal_word_list: list[str] = [dot_word.capitalize() for dot_word in dot_word_list]

    result: str | None = connect_strings_with_divider(string_list=pascal_word_list, divider=pascal_divider)
    return result

def dot_to_path(*, variable_name: str) -> str | None:

    dot_divider: str = case_dividers_dict[CaseDividersNames.DOT.value]
    dot_word_list: list[str] | None = get_string_list_of_delimiter_case(variable_name=variable_name, divider=dot_divider)

    if dot_word_list is None:
        return None
    
    path_divider: str = case_dividers_dict[CaseDividersNames.PATH.value]
    path_word_list: list[str] = [dot_word.lower() for dot_word in dot_word_list]

    result: str | None = connect_strings_with_divider(string_list=path_word_list, divider=path_divider)
    return result

def dot_to_screaming(*, variable_name: str) -> str | None:

    dot_divider: str = case_dividers_dict[CaseDividersNames.DOT.value]
    dot_word_list: list[str] | None = get_string_list_of_delimiter_case(variable_name=variable_name, divider=dot_divider)

    if dot_word_list is None:
        return None
    
    screaming_divider: str = case_dividers_dict[CaseDividersNames.SCREAMING.value]
    screaming_word_list: list[str] = [dot_word.upper() for dot_word in dot_word_list]

    result: str | None = connect_strings_with_divider(string_list=screaming_word_list, divider=screaming_divider)
    return result

def dot_to_snake(*, variable_name: str) -> str | None:

    dot_divider: str = case_dividers_dict[CaseDividersNames.DOT.value]
    dot_word_list: list[str] | None = get_string_list_of_delimiter_case(variable_name=variable_name, divider=dot_divider)

    if dot_word_list is None:
        return None
    
    snake_divider: str = case_dividers_dict[CaseDividersNames.SNAKE.value]
    snake_word_list: list[str] = [dot_word.lower() for dot_word in dot_word_list]

    result: str | None = connect_strings_with_divider(string_list=snake_word_list, divider=snake_divider)
    return result

def dot_to_train(*, variable_name: str) -> str | None:

    dot_divider: str = case_dividers_dict[CaseDividersNames.DOT.value]
    dot_word_list: list[str] | None = get_string_list_of_delimiter_case(variable_name=variable_name, divider=dot_divider)

    if dot_word_list is None:
        return None
    
    train_divider: str = case_dividers_dict[CaseDividersNames.TRAIN.value]
    train_word_list: list[str] = [dot_word.capitalize() for dot_word in dot_word_list]

    result: str | None = connect_strings_with_divider(string_list=train_word_list, divider=train_divider)
    return result

