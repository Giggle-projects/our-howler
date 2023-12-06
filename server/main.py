from datetime import datetime
from fastapi import FastAPI
from starlette.requests import Request

import uvicorn
import member_dao
import env_dao
import scheduler
import slack_sender

signature = " 너 도태될꺼야? 공부해 이놈아!\n" \
            "*<https://github.com/Giggle-projects/our-howler|Github - our howler>*"

commit_signature = " 님이 커밋하셨습니다."

envs = env_dao.init()
channel_name = envs["fastapi.channel_name"]
token =  envs["fastapi.slack.token"]

app = FastAPI()


@app.post("/")
async def say_anything(
        request: Request
):
    form = await request.form()
    user_id = form["user_id"]
    return "<@{}>".format(user_id) + signature + str(datetime.now())


@app.post("/score")
def get_score():
    members_score = member_dao.get_score()
    response = ', '.join(members_score)
    return {response}


@app.post("/update/{target_username}")
def update_score(target_username):
    slack_id, score = member_dao.update_score(target_username)

    howl_message = "<@{}>".format(slack_id) + commit_signature
    slack_sender.send(channel_name, token, howl_message)
    return [slack_id, score]


def howl():
    today_date = datetime.now().date()
    users = member_dao.get_member_slack_ids_by_not_exists_update_date(today_date)

    for user in users:
        howl_message = "<@{}>".format(user) + signature
        slack_sender.send(channel_name, token, howl_message)


if __name__ == "__main__":
    scheduler.add_schedule_everyday("23:59", howl)
    scheduler.run_scheduler(5)
    uvicorn.run(app, host="0.0.0.0", port=7777)
