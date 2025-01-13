from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TastRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TastRepository.add_one(task)
    return {'ok': True, "task_id": task_id}


@router.get('')
async def get_task() -> list[STask]:
    tasks = await TastRepository.find_all()
    return tasks