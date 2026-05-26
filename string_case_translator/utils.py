def get_string_list_of_delimiter_case(*, 
                                     variable_name: str,
                                     divider: str,
                                     ) -> list[str] | None:
    
    """Returns strings of given string between divider. 

    This function **iterates** by splitted words of variable name and **cleans** them from divider. 
    It **uses built-in C methods** of string **.split(), .strip()** to make code faster and more readable. 

    Args:
        variable_name (str): **The variable name** that should be divided by words between divider. 
        divider (str): **The string** that divides variable name into words. 

    Returns:
        list[str] | None: **A list of words** between divider from variable name or **None** if TypeError or AttributeError occurs. 

    Examples:
        >>> get_string_list_of_delimiter_case(variable_name="-kebab-case-", divider="-")
        ['kebab', 'case']
        >>> get_string_list_of_delimiter_case(variable_name="___very_long__snake_case___", divider="_")
        ['very', 'long', 'snake', 'case']
        >>> get_string_list_of_delimiter_case(variable_name=3.14, divider=1.41)
        None
    """

    try:
        variable_name_string_list: list[str] = variable_name.split(divider)
        result: list[str] = []

        for variable_name_string in variable_name_string_list:
            string_is_empty: bool = variable_name_string == ""

            if string_is_empty:
                continue

            result_string: str = variable_name_string.strip(divider)
            result.append(result_string)
        
        return result
    except (TypeError, AttributeError):
        return None
    
def get_string_list_of_bounding_case(*,
                                      variable_name: str
                                      ) -> list[str] | None:
    
    """Returns strings of given string that divided by upper letters. 

    This function **finds** index of upper letters and **creates** slises of given variable name. 
    It **uses built-in C methods** of string **.isupper(), .append()** to make code faster and more readable.  

    Args:
        variable_name: (str): **The variable name** that should be divided into words that starts with upper letter.  

    Returns:
        list[str] | None: **A list of words** between upper letters or **None** if TypeError or AttributeError occurs. 

    Examples:
        >>> get_string_list_of_bounding_case(variable_name="camelCase")
        ['camel', 'Case']
        >>> get_string_list_of_bounding_case(variable_name="PascalCase")
        ['Pascal', 'Case']
        >>> get_string_list_of_bounding_case(variable_name=3.14)
        None
    """

    if not variable_name:
        return None

    try:
        result: list[str] = []
        upper_characters_index_list: list[int] = [0]
        variable_name_length: int = len(variable_name) 

        for index, character in enumerate(variable_name):
            character_is_upper: bool = character.isupper()

            if character_is_upper:
                upper_characters_index_list.append(index)

        upper_characters_index_list.append(variable_name_length)

        for i in range(len(upper_characters_index_list) - 1):
            start: int = upper_characters_index_list[i]
            end: int = upper_characters_index_list[i + 1]

            variable_name_slice: str = variable_name[start:end]
            result.append(variable_name_slice)

        empty_string_is_in_beginning_of_result: bool = result[0] == ""

        if empty_string_is_in_beginning_of_result:
            del result[0]

        return result
    except (TypeError, AttributeError):
        return None
    
def connect_strings_with_divider(*, 
                                 string_list: list[str], 
                                 divider: str,
                                 ) -> str | None:
    
    """Returns string of connected words by divider. 

    This function **connects** words in string_list by divider between them. 
    It uses **built-in C methods** of string **.join()** to make code faster and more readable.  

    Args:
        string_list (list[str]): **A words list** that should be connected into one string by divider between them. 
        divider (str): **A string** that connects words in string_list. 
    
    Returns:
        str | None: **A string** that created by connecting words in string_list and divider between them or None if TypeError or AttributeError occurs.  

    Examples:
        >>> connect_strings_with_divider(string_list=["snake", "case"], divider="_")
        'snake_case'
        >>> connect_strings_with_divider(string_list=True, divider="what is that?")
        None
        >>> connect_strings_with_divider(string_list=["i", "remember", "number", "pi"], divider=3.14)
        None
    """
    
    try:
        result: str = divider.join(string_list)
        return result
    except (TypeError, AttributeError):
        return None
    
def change_divider_in_string(*, 
                             variable_name: str,
                             old_divider: str,
                             new_divider: str,
                             ) -> str | None:
    
    """Returns strings of given string that divided by upper letters. 

    This function **replaces** old divider to new divider in string. 
    It uses **built-in C methods** of string **.replace()** to make code faster and more readable.  

    Args:
        variable_name: (str): **The variable name** that should be divided into words that starts with upper letter.  

    Returns:
        list[str] | None: **A list of words** between upper letters or **None** if TypeError or AttributeError occurs. 

    Examples:
        >>> change_divider_in_string(variable_name="dot.to.kebab", old_divider=".", new_divider="-")
        'dot-to-kebab'
        >>> change_divider_in_string(variable_name="dot.to.kebab", old_divider=True, new_divider="do not divide my variable!")
        None
        >>> change_divider_in_string(variable_name="dot.to.kebab", old_divider="i remember number pi", new_divider=3.141592565358979)
        None
    """

    try:
        result: str = variable_name.replace(old_divider, new_divider)
        return result
    except (TypeError, AttributeError):
        return None

