from paji.service.db_backup.gke_mysql_client.gke_cluster import GKECluster


class GKEMysqlClient:

    def __init__(self, connection_info):
        self.connection_info = connection_info

        # 連到指定的 k8s
        self.cluster = GKECluster(
            project_id=self.connection_info.project_id,
            zone=self.connection_info.zone,
            cluster_id=self.connection_info.cluster_id,
            service_account_file=self.connection_info.service_account_file,
        )

        # 找到指定的 mysql pod
        pod_info = self.cluster.query_pod_info(
            namespace=self.connection_info.namespace,
            pod_name_pattern=self.connection_info.pod_name_pattern,
        )

        self.namespace = self.connection_info.namespace
        self.pod_name = pod_info['name']

    def get_database_sql(self, database_name):
        result = self.cluster.exec_pod(
            namespace=self.namespace,
            name=self.pod_name,
            command=[
                'mysqldump',
                '-u' + self.connection_info.account,
                '-p' + self.connection_info.password,
                database_name,
            ],
        )
        return result
