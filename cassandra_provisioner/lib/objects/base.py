class BaseObject(object):
    def __init__(self, result):
        """
        :param result: postgres dict result
        """
        self.__dict__.update(result)


class Topology(BaseObject):
    def __init__(self, result):
        super().__init__(result)
        self.cluster = None  # should always be a cluster object
        self.cdcs = None  # should always be a tuple of cdc objects
        self.nodes = None  # should always be a tuple of node objects

