import hashlib
import json

import fastapi

from paji.service.jessiclient import get_redis_client
from paji.service.jessiclient.dependencies import get_jessiclient_config

router = fastapi.APIRouter()


@router.post('/api/jessiclient/sharing/projects', status_code=201)
async def create_sharing_project(request: fastapi.Request,
                                 config=fastapi.Depends(get_jessiclient_config),
                                 redis_client=fastapi.Depends(get_redis_client)):
    request_body = await request.body()

    m = hashlib.md5()
    m.update(request_body)
    project_code = m.hexdigest()

    redis_client.set(f'jessiclient:projects:{project_code}', request_body, config.sharing.project.expired_time)
    return {
        'data': {
            'projectCode': project_code,
        },
    }


@router.get('/api/jessiclient/sharing/projects/{project_code}')
async def get_sharing_project(project_code: str, redis_client=fastapi.Depends(get_redis_client)):
    data = redis_client.get(f'jessiclient:projects:{project_code}')
    if not data:
        raise fastapi.HTTPException(status_code=404, detail='project 不存在')

    project = json.loads(data)
    return {
        'data': project,
    }
