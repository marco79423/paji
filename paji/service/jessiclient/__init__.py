from paji.service.base import ServiceBase
from paji.service.jessiclient.dependencies import get_redis_client
from paji.service.jessiclient.routes import sharing_project


class JessiclientService(ServiceBase):

    def setup(self):
        self.app.include_router(sharing_project.router)
        self.logger.info('啟動 Jessiclient 成功')
