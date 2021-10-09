import json

from pydantic import BaseModel


class Base(BaseModel):
    """
    This is Base, here am i
    """

    @classmethod
    def load(cls, data):
        """
        loads
        """
        if type(data) is dict:
            return cls(**data)
        loaded = json.loads(data.decode())
        return cls(**loaded)

    def dump(self):
        return self.json().encode()
