import re

from google.auth.transport.requests import Request
from google.cloud import container_v1
from google.oauth2 import service_account
from kubernetes import client as kubernetes_client
from kubernetes.stream import stream
from paji_sdk.base.exceptions import NotFoundError


class GKECluster:
    def __init__(self, project_id, zone, cluster_id, service_account_file):
        credentials = service_account.Credentials.from_service_account_file(service_account_file)
        cluster_manager_client = container_v1.ClusterManagerClient(credentials=credentials)
        cluster = cluster_manager_client.get_cluster(
            name=f'projects/{project_id}/locations/{zone}/clusters/{cluster_id}'
        )

        kubeconfig_creds = credentials.with_scopes([
            'https://www.googleapis.com/auth/cloud-platform'
        ])
        kubeconfig_creds.refresh(Request())

        configuration = kubernetes_client.Configuration()
        configuration.host = f"https://{cluster.endpoint}:443"
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": "Bearer " + kubeconfig_creds.token}
        kubernetes_client.Configuration.set_default(configuration)

        self.kube_api = kubernetes_client.CoreV1Api()

    def query_pod_info(self, pod_name_pattern, namespace):
        pods = self.kube_api.list_namespaced_pod(namespace=namespace)

        target_pod = None
        for item in pods.items:
            if re.match(pod_name_pattern, item.metadata.name):
                target_pod = item

        if not target_pod:
            raise NotFoundError('找不到對應的 Pod')

        return {
            'name': target_pod.metadata.name,
        }

    def exec_pod(self, namespace, name, command):
        resp = stream(
            self.kube_api.connect_post_namespaced_pod_exec,
            name=name,
            namespace=namespace,
            command=command,
            stderr=False, stdin=False,
            stdout=True, tty=False
        )
        return resp
