import ujson as json

class DObjectConvert(object):
    def to_dict(self):
        return self.__dict__

    def to_json(self, filename=None):
        d = self.to_dict()
        if filename:
            json.dump(open(filename, 'w'), d)
        return json.dumps(d)

    @classmethod
    def from_json(cls, filename=None, string=None):
        if filename:
            data = json.load(open(filename))
        elif string:
            data = json.loads(string)
        else:
            raise Exception("No file or string provided")
        return cls(data)


class DObject(DObjectConvert):
    def __init__(self, dictionary={}):
        self.__dict__.update(dictionary)
        for k, v in dictionary.items():
            if isinstance(v, dict):
                self.__dict__[k] = Struct(v)
