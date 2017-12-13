from cassandra_provisioner.lib.postgres.client import PostgresClient
from cassandra_provisioner.lib.postgres.mappers.cluster import ClusterMapper
from cassandra_provisioner.lib.postgres.mappers.cluster_data_centre import ClusterDataCentreMapper
from cassandra_provisioner.lib.postgres.mappers.node import NodeMapper


def test_basic_connection():
    class Config(object):
        pass

    class Postgres(object):
        user = 'max'
        password = 'Jzey225pf'
        host = '192.168.1.2'
        database = 'cassandra_provisioner'
    config = Config()
    config.postgres = Postgres()
    client = PostgresClient(config)
    client.connect()

    print('successful connection')
    return client


def test_create_cluster(client):
    mapper = ClusterMapper(client)
    cluster = mapper.create_cluster(cassandra_version='apache_cassandra_3.10.1',
                                    name='test_cluster',
                                    subnet='192.168.1.0/26')
    return cluster


def test_create_cdc(client, cluster):
    mapper = ClusterDataCentreMapper(client)
    cdc = mapper.create_cdc(cluster_id=cluster.id,
                            name='test_cdc',
                            subnet='192.168.1.0/24')
    return cdc


def test_create_node(client, cdc, rack):
    mapper = NodeMapper(client)
    node = mapper.create_node(cluster_data_centre_id=cdc.id, rack=rack)
    return node


def _cleanup():
    client.connection.rollback()
    if cluster is not None:
        client.execute('DELETE FROM cp.clusters WHERE id = %(id)s',
                       {'id': cluster.id})
    if cdc is not None:
        client.execute('DELETE FROM cp.cluster_data_centres WHERE id = %(id)s',
                       {'id': cdc.id})
    if len(nodes) > 0:
        for node in nodes:
            client.execute('DELETE FROM cp.nodes WHERE id = %(id)s',
                           {'id': node.id})


if __name__ == '__main__':
    client = test_basic_connection()
    cluster = None
    cdc = None
    rack_prefix = 'rack-'
    nodes = []
    try:
        cluster = test_create_cluster(client)
        print(cluster.__dict__)
        cdc = test_create_cdc(client, cluster)
        print(cdc.__dict__)
        i = 0
        for i in range(3):
            node = test_create_node(client, cdc, rack_prefix + str(i))
            nodes.append(node)
            print(node.__dict__)
        _cleanup()
    except Exception as e:
        _cleanup()
        raise e