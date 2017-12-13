import pyyaml
import os


class Config(object):
    _config_file_name = 'config.yaml'
    _config_dir = '/etc/cassandra_provisioner'
    _config_full_file_name = _config_dir + '/' + _config_file_name

    def __init__(self):
        self._check_config_file_exists()
        with open(self._config_full_file_name, 'r') as f:
            pyyaml.load

    def _check_config_file_exists(self):
        if not os.path.exists('/etc/cassandra_provisioner'):
            self._create_config_dir()
        if not os.path.exists('/etc/cassandra_provisioner/config.yaml', 'w+'):
            self._create_config_file()
        if not os.path.isfile(self._config_full_file_name):
            self._delete_config_file()
            self._create_config_file()

    def _create_config_dir(self):
        os.mkdir(self._config_dir)

    def _create_config_file(self):
        with open(self._config_full_file_name) as f:
            f.write('')

    def _delete_config_file(self):
        os.rmdir(self._config_full_file_name)
