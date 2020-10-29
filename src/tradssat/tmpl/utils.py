import re


def _name_matches(pattern, name, full=False):
    """
    
    Parameters
    ----------
    pattern: str | re.Pattern
        The desired name, or a regex.
    name: str
        The name to test.
    full:
        Whether ``pattern`` should match the full name or just the beginning.

    Returns
    -------

    """
    if None in [pattern, name]:
        return True

    elif isinstance(pattern, str):

        if (pattern == name) or (not full and name.startswith(pattern)):
            return pattern

    else:
        m = re.fullmatch(pattern, name) if full else re.match(pattern, name)

        if m:
            return m.group()
