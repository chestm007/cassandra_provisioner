class Service(object):
    required_attrs = ('name', )

    def sanity_check(self):
        for attr in self.required_attrs:
            if not hasattr(self, attr):
                raise AttributeError('{classname} has no {attr} attribute'.format(
                                     classname=str(self.__class__.__name__),
                                     attr=attr))

