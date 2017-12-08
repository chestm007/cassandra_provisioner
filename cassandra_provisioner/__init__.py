from .lib.postgres.client import PostgresClient


class ProvisioningCentre(object):
    def __init__(self):
        self.config = Config()
    def log(self, msg):
        print(msg)


    def start_services(self):
        postgres_client = PostgresClient(self.config)


if __name__ == '__main__':
    provisioner = ProvisioningCentre()
    provisioner.start_services()
