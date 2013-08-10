
class DotDict(dict):
    """
    Class to extend the standard Python dictionary 'dict' and
    provide a dot notation access to the values in the dictionary
    """
    def __getattr__(self, attr):
        return self.get(attr, None)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

def is_none(val):
    """
    Returns true if the value is to be considered as None. The notion
    of None includes empty string or space
    """
    if val in [None, '', ' ']:
        return True
    else:
        return False

def is_not_none(val):
    return not is_none(val)

def drop_nones(vals):
    """
    Remove None or empty strings from a list
    """
    return filter(is_not_none, vals)

def coalesce(*values):
    """
    Return the first non null values from the list of values passed
    to the function.
    """
    for value in values:
        if value is not None:
            return value
    
    return None
    