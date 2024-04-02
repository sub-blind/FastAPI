users = {1: {"username": "jaeseop"}, 2: {"username": "seopjae"}}


def get_current_username(token: str):
    # 토큰을 유저 ID로 간주
    user_id = int(token)

    user = users.get(user_id)

    return user["username"]
