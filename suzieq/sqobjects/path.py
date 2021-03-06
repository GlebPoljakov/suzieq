from suzieq.sqobjects.basicobj import SqObject


class PathObj(SqObject):
    def __init__(self, **kwargs):
        super().__init__(table='path', **kwargs)

    def get(self, **kwargs):

        return self.engine_obj.get(**kwargs)

    def summarize(self, **kwargs):
        """Summarize topology info for one or more namespaces"""

        return self.engine_obj.summarize(**kwargs)
