from ninja import NinjaAPI
from todo.models import Task
from typing import List
from ninja import Schema
from django.shortcuts import get_object_or_404

api = NinjaAPI()

class TaskSchema(Schema):
    id: int
    title: str
    description: str
    completed: bool

class TaskCreateSchema(Schema):
    title: str
    description: str

@api.get("/tasks", response=List[TaskSchema])
def list_tasks(request):
    tasks = Task.objects.all()
    return tasks

@api.post("/tasks", response=TaskSchema)
def create_task(request, data: TaskCreateSchema):
    task = Task.objects.create(**data.dict())
    return task

@api.put("/tasks/{task_id}", response=TaskSchema)
def update_task(request, task_id: int, data: TaskCreateSchema):
    task = get_object_or_404(Task, id=task_id)
    for attr, value in data.dict().items():
        setattr(task, attr, value)
    task.save()
    return task

@api.delete("/tasks/{task_id}")
def delete_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return {"success": True}
