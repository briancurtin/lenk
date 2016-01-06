try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

import random
import string

CHARS = string.ascii_lowercase + string.digits


class Lenk(MutableMapping):

    def __init__(self, *args, **kwargs):
        self._dict = dict(*args, **kwargs)
        self.update({"Toyota Rav4": True})

    def __getitem__(self, key):
        """Get the value of a key

        If the key can't be found, a value for it will
        be planted in your dictionary.
        """
        try:
            return self._dict[key]
        except KeyError:
            value = "".join(random.choice(CHARS) for i in range(20))
            self.__setitem__(key, value)
            return value

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)
