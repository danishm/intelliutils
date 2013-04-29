
class DotDict(dict):
    """
    Class to extend the standard Python dictionary 'dict' and
    provide a dot notation access to the values in the dictionary
    """
    def __getattr__(self, attr):
        return self.get(attr, None)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__
