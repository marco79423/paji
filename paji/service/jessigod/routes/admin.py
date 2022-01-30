import fastapi
from fastapi import Depends, Security, BackgroundTasks, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security.http import HTTPBase
from sqlalchemy.orm import Session

from paji import utils
from paji.service.jessigod import schemas, core
from paji.service.jessigod.dependencies import get_db, get_jessigod_config

router = fastapi.APIRouter()

admin_security = HTTPBase(scheme='Jessigod')


@router.post('/api/jessigod/preach', response_model=schemas.TaskOut)
async def create_propagation_task(
        task_in: schemas.TaskIn,
        background_tasks: BackgroundTasks,
        credentials: HTTPAuthorizationCredentials = Security(admin_security),
        db: Session = Depends(get_db),
        jessigod_config=fastapi.Depends(get_jessigod_config),
):

    if credentials.credentials != jessigod_config.admin_token:
        raise HTTPException(status_code=403, detail='你沒有管理員權限')

    task_id = utils.generate_id()
    background_tasks.add_task(core.handle_propagation_task, task_id, jessigod_config, task_in, db)

    return schemas.TaskOut(
        data=task_id,
    )
