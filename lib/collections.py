#!/usr/bin/env python
# To do
# - REST API - schedule collection
#   - Celery backed by Redis
#   - Data persists to Cassandra
# - REST API - get status
# - Command line tool to interact with API
# - Data is picked up from Cassandra and copied into MySQL
# - Data is made searchable via API

# import yaml

#GCP libs
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# class Utils:
#     def __init__(self):
#         self.config_path = "config.yml"
#
#     def config_parse(self):
#         with open(self.config_path, 'r') as ymlfile:
#             cfg = yaml.load(ymlfile)
#
#         return cfg

class Gcp:
    def __init__(self):
        self.credentials = GoogleCredentials.get_application_default()

    def create_service(self, service_name):
        self.service = discovery.build(service_name, 'beta', credentials=self.credentials)

    def collect_instances(self, project, zone):
        result = self.service.instances().list(project=project, zone=zone).execute()
        return result

    def collect_zones(self, service, project):
        result = []

        request = service.zones().list(project=project)

        while request is not None:
            response = request.execute()

            for zone in response['items']:
                result.append(zone["name"])

            request = service.zones().list_next(previous_request=request, previous_response=response)

        return result



# if __name__ == "__main__":
#
#     credentials = GoogleCredentials.get_application_default()
#     service = discovery.build('compute', 'beta', credentials=credentials)
#
#     ## Parse config values ##
#     cfg = config_parse()
#     projects = cfg['collector']['projects']
#     resources = cfg['collector']['resources']
#
#     zones = collect_zones(service, projects[0])
#
#     for project in projects:
#         for zone in zones:
#             instances = collect_instances(service, project, zone)
#             print "%s, %s" % (zone, instances)
#
