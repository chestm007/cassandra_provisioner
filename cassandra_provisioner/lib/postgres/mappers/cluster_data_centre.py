import uuid
from ...objects.cluster_data_centre import ClusterDataCentre


class ClusterDataCentreMapper(object):
    _create_cdc_statement = '''
    INSERT INTO cp.cluster_data_centres (id, cluster_id, subnet, name)
    VALUES (%(id)s, %(cluster_id)s, %(subnet)s, %(name)s);
    '''
    _select_cdc_statement = '''
    SELECT *
    FROM cp.cluster_data_centres
    WHERE id = %(id)s;
    '''

    def __init__(self, client):
        self.client = client

    def create_cdc(self, *_, cluster_id=None, name=None, subnet=None):
        assert cluster_id is not None
        assert name is not None
        assert subnet is not None
        id = uuid.uuid4()
        self.client.execute(self._create_cdc_statement,
                            {
                                'id': str(id),
                                'cluster_id': cluster_id,
                                'name': name,
                                'subnet': subnet
                            })
        res = self.client.get_one_row(
                  self._select_cdc_statement,
                  {'id': str(id)})
        return ClusterDataCentre(res)
