import re


def _name_matches(pattern, name, full=False):
    if None in [pattern, name]:
        return True

    elif isinstance(pattern, str):

        if (pattern == name) or (not full and name.startswith(pattern)):
            return pattern

    else:
        m = re.fullmatch(pattern, name) if full else re.match(pattern, name)

        if m:
            return m.group()
