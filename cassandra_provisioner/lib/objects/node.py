from .base import Topology


class Node(Topology):
    def __init__(self, result):
        super().__init__(result)

    def get_cdcs(self):
        if self.cdcs is None:
            # TODO: link to mapper method to get cdcs
            pass
        return self.cdcs

    def get_cluster(self):
        if self.cluster is None:
            # TODO: link to mapper method to get cluster
            pass
        return self.cluster
