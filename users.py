from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"],  # 여기에 의존성을 추가할 수 있습니다
    responses={
        200: {"msg": "Success to get data"},
        400: {"mas": "404 Not found"},
    },
)


@router.get("/{user_id}")
def get_users(user_id: int):
    return {"data": user_id}
