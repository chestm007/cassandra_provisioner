import uuid
from ...objects.node import Node


class NodeMapper(object):
    _create_node_statement = '''
    INSERT INTO cp.nodes (id, cluster_data_centre_id, rack)
    VALUES (%(id)s, %(cluster_data_centre_id)s, %(rack)s);
    '''
    _select_node_statement = '''
    SELECT *
    FROM cp.nodes
    WHERE id = %(id)s;
    '''

    def __init__(self, client):
        self.client = client

    def create_node(self, *_, cluster_data_centre_id=None, rack=None):
        assert cluster_data_centre_id is not None
        assert rack is not None
        id = uuid.uuid4()
        self.client.execute(self._create_node_statement,
                            {
                                'id': str(id),
                                'cluster_data_centre_id': cluster_data_centre_id,
                                'rack': rack
                            })
        res = self.client.get_one_row(
                  self._select_node_statement,
                  {'id': str(id)})
        return Node(res)
