from sqlalchemy import select
from database import new_session, TaskORM
from schema import STasAdd, STask

"""await ставим только при запросе к самой БД, а не к внутренней кухне"""

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STasAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush() # уже отрправляем в БД изменения и получаем id у объекта
            await session.commit() # только потом записываем изменения
            return task.id



    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return tasks_schemas

