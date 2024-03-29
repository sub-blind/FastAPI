from fastapi import APIRouter
import time

router = APIRouter()


# 동기
@router.get("/slow-sync-ping")
def slow_sync_ping():
    time.sleep(10)

    return {"msg": "pong"}


# 비동기
import asyncio


@router.get("/slow-async-ping")
async def slow_async_ping():
    await asyncio.sleep(10)
    return {"message": "pong"}


def cpu_intensive_task():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    result = fibonacci(35)
    return result


# Worst case
# CPU 부하 -> Event Loop에 부하가 걸림
async def cpu_hard_task():
    result = await cpu_intensive_task()
    return {"msg": result}


# best case
# CPU에 부하가 많이 걸리는 작업은 -> 이벤트 루프에서 분리 후,
# 별도의 프로세스에서 실행하게 만들어준다.
from concurrent.futures import ProcessPoolExecutor


def cpu_bound_task():
    with ProcessPoolExecutor() as executor:
        result = asyncio.get_event_loop().run_in_executor(executor, cpu_intensive_task)
    return {"result": result}
