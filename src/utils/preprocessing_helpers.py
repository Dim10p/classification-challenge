import re
import html
import pandas as pd


def convert_html_to_ascii(text: str) -> str:
    """
    Converts HTML entities to ASCII characters in the input text.

    Args:
        text (str): The text containing HTML entities to be converted.

    Returns:
        str: Modified text with HTML entities replaced by ASCII characters.
    """
    modified_text = html.unescape(text)
    return modified_text


def remove_html_tags(text: str) -> str:
    """
    Removes HTML tags from the input text.

    Args:
        text (str): The text containing HTML tags to be removed.

    Returns:
        str: Text with HTML tags removed or "-" if the text is only HTML tags.
    """
    html_tags_removal = re.compile('<[^><]+>')
    modified_text = re.sub(html_tags_removal, ' ', text)
    modified_text = ' '.join(modified_text.split())
    return modified_text if modified_text else "-"


def split_uppercase_after_lowercase(text: str) -> str:
    """
    Splits uppercase characters that follow lowercase characters in the input text.

    Args:
        text (str): The text to process.

    Returns:
        str: Text with spaces inserted before uppercase characters following lowercase characters.
    """
    if text == "":
        return text
    else:
        modified_text = ""
        for i in range(len(text) - 1):
            if text[i].islower() and text[i + 1].isupper():
                modified_text += text[i] + " "
            else:
                modified_text += text[i]
        modified_text += text[-1]
    return modified_text


def convert_to_lowercase(text: str) -> str:
    """
    Converts all characters in the input text to lowercase.

    Args:
        text (str): The text to convert.

    Returns:
        str: Lowercase version of the input text.
    """
    modified_text = text.lower()
    return modified_text


def remove_whitespaces(text: str) -> str:
    """
    Removes leading and trailing whitespaces from the input text and collapses
    multiple consecutive whitespaces into a single space.

    Args:
        text (str): The text to clean.

    Returns:
        str: Text with leading/trailing whitespaces removed and extra whitespaces collapsed.
    """
    modified_text = text.strip()
    extra_whitespaces_removal = re.compile('\s+')
    modified_text = re.sub(extra_whitespaces_removal, ' ', modified_text)
    return modified_text


def remove_repeated_punctuations(text: str) -> str:
    """
    Removes repeated consecutive punctuations from the input text.

    Args:
        text (str): The text to process.

    Returns:
        str: Text with repeated consecutive punctuations collapsed to a single occurrence.
    """
    modified_text = re.sub(r'([^\w\s])\1+', r'\1', text)
    return modified_text


def contains_only_punctuations_regex(input_string: str) -> bool:
    """
    Checks if the input text consists only of punctuations.

    Args:
        input_string (str): The text to check.

    Returns:
        bool: True if the input text contains only punctuations, False otherwise.
    """
    return bool(re.match(r'^[^\w]+$', input_string))


def extract_included_occupations(included_occupations_string):
    """
    Extracts a list of occupations from the given string.

    The function looks for the text following 'Examples of the occupations classified here:' and extracts
    occupations listed with each occupation prefixed by '- '.

    Args:
        included_occupations_string (str): A string containing occupations with each occupation prefixed by '- '.

    Returns:
        list: A list of occupations without the prefix '- '.
    """
    if not included_occupations_string:
        return []

    pattern = r"Examples of the occupations classified here:\s*\n"
    match = re.search(pattern, included_occupations_string)

    if not match:
        return []

    relevant_text = included_occupations_string[match.end():]

    lines = relevant_text.split('\n')

    occupations = [line.replace('- ', '') for line in lines if line.startswith('- ')]

    return occupations


def extract_excluded_numbers(excluded_occupations_string):
    """
    Extracts a list of dictionaries with occupations and their corresponding numbers from the given string.

    The function looks for the text following 'Some related occupations classified elsewhere:' and extracts
    occupations and numbers listed with each occupation prefixed by '- '.

    Args:
        excluded_occupations_string (str): A string containing occupations and numbers
        with each occupation prefixed by '- '.

    Returns:
        list: A list of dictionaries where keys are occupations and values are their corresponding numbers.
              Returns None if the relevant pattern is not found.
    """
    if not excluded_occupations_string or pd.isna(excluded_occupations_string):
        return None

    pattern_start = r"Some related occupations classified elsewhere:\s*\n"
    match = re.search(pattern_start, excluded_occupations_string)

    if not match:
        return None

    relevant_text = excluded_occupations_string[match.end():]

    pattern = r'-\s+(.+?)\s*-\s*(\d+)'
    matches = re.findall(pattern, relevant_text)

    return [{occupation.strip(): number} for occupation, number in matches]

