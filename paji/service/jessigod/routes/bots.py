import json
from typing import Optional

import fastapi
import linebot
import linebot.models
from fastapi import Header, Request
from starlette.background import BackgroundTasks

from paji.service.jessigod import core
from paji.service.jessigod.dependencies import get_jessigod_config

router = fastapi.APIRouter()


@router.post('/api/jessigod/bots/line-webhook')
async def create_propagation_task(
        request: Request,
        background_tasks: BackgroundTasks,
        x_line_signature: Optional[str] = Header(None),
        jessigod_config=fastapi.Depends(get_jessigod_config),
):
    body = await request.body()

    parser = linebot.WebhookParser(jessigod_config.bots.line_bot.channel_secret)
    events = parser.parse(body.decode(), x_line_signature)
    if events:
        background_tasks.add_task(core.handle_line_events, events)

    return 'ok'


@router.post('/api/jessigod/bots/telegram-webhook/{token}')
async def create_propagation_task(
        token: str,
        request: Request,
        background_tasks: BackgroundTasks,
        jessigod_config=fastapi.Depends(get_jessigod_config),
):
    if jessigod_config.bots.telegram_bot.token != token:
        return 'not ok'

    body = await request.body()
    background_tasks.add_task(core.handle_telegram_update, json.loads(body))

    return 'ok'
