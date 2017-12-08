from .base import Topology


class ClusterDataCentre(Topology):
    def __init__(self, result):
        self.subnet = None
        self.name = None
        super().__init__(result)

    def get_nodes(self):
        if self.nodes is None:
            # TODO: link to mapper method to get nodes
            pass
        return self.nodes

    def get_cluster(self):
        if self.cluster is None:
            # TODO: link to mapper method to get cluster
            pass
        return self.cluster
