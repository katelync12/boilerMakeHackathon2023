import re
from typing import List


def clean_unicode_links(content: str) -> str:
    """Returns the string without unicode, and without links """
    # strip unicode
    content = re.sub(pattern=r'[^\x00-\x7F]+',
                           repl='',
                           string=content)
    # remove links
    # regex source https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url
    content = re.sub(pattern=r'(http(s)?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)',
                     repl='',
                     string=content)

    return content


def get_handles(content:str) -> List[str]:
    """Returns a list of handles: ['@x','@ye'] for 'Hello @x Im @ye' """
    return re.findall(pattern=r'@\w+', string=content)
