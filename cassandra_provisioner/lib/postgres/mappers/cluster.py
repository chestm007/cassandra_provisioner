import uuid
from ...objects.cluster import Cluster


class ClusterMapper(object):
    _create_cluster_statement = '''
    INSERT INTO cp.clusters (id, cassandra_version, name, subnet)
    VALUES (%(id)s, %(cassandra_version)s, %(name)s, %(subnet)s);
    '''
    _select_cluster_statement = '''
    SELECT *
    FROM cp.clusters
    WHERE id = %(id)s;
    '''

    def __init__(self, client):
        self.client = client

    def create_cluster(self, *_, cassandra_version=None, name=None, subnet=None):
        assert cassandra_version is not None
        assert name is not None
        assert subnet is not None
        id = uuid.uuid4()
        self.client.execute(self._create_cluster_statement,
                            {
                                'id': str(id),
                                'cassandra_version': cassandra_version,
                                'name': name,
                                'subnet': subnet
                            })
        res = self.client.get_one_row(
                  self._select_cluster_statement,
                  {'id': str(id)})
        return Cluster(res)
