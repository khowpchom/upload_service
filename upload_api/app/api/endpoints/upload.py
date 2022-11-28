import json
import asyncio
from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, File, UploadFile, BackgroundTasks, WebSocket
from core.redis import redis

from services.upload import task_upload


router = APIRouter()

@router.post("/")
async def upload_api(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if file.content_type != "text/csv":
        raise HTTPException(400, detail="Invalid document type")
    
    task_id = uuid4()
    await redis.set(f"upload:{task_id}", 0)
    background_tasks.add_task(task_upload, file, task_id)
    return {
        "task_id": task_id
    }

# @router.get("/status/{task_id}")
# async def status_api(task_id: UUID):
#     percent = await redis.get(f"upload:{task_id}")
#     if percent is None:
#         raise HTTPException(404, detail=f"Not found data of task_id: {task_id}")
    
#     percent = int(percent)
#     response = {
#         "percent": percent
#     }
#     if percent == 100:
#         result = await redis.get(f"result:{task_id}")
#         response["result"] = json.loads(result)
#         pipeline = redis.pipeline()
#         pipeline.delete(f"upload:{task_id}")
#         pipeline.delete(f"result:{task_id}")
#         await pipeline.execute()
#     return response

@router.websocket("/status/{task_id}")
async def status_socket(websocket: WebSocket, task_id: UUID) -> None:
    await websocket.accept()
    while True:
        percent = await redis.get(f"upload:{task_id}")
        if percent is None:
            await websocket.send_text(f"Not found data of task_id: {task_id}")
            await websocket.close()
        
        percent = int(percent)
        response = {
            "percent": percent
        }
        if percent == 100:
            result = await redis.get(f"result:{task_id}")
            response["result"] = json.loads(result)
            pipeline = redis.pipeline()
            pipeline.delete(f"upload:{task_id}")
            pipeline.delete(f"result:{task_id}")
            await pipeline.execute()
            await websocket.send_json(response)
            await websocket.close()
        await websocket.send_json(response)
        await asyncio.sleep(0.5)
