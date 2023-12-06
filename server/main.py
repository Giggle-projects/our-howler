import uvicorn
from fastapi import FastAPI, Form
from datetime import datetime

from starlette.requests import Request
import slackSender
import scheduler
import member_dao

signature = " 너 도태될꺼야? 공부해 이놈아!\n" \
            "*<https://github.com/Giggle-projects/our-howler|Github - our howler>*"


commit_signature = " 님이 커밋하셨습니다."

channel_name = "howler-alert"
token = "xoxb-2476610625797-6307304308496-zxqnhlXdCLF90D9PwOUR3chk"

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
    slackSender.send(channel_name, token, howl_message)
    return [slack_id, score]


def howl():
    today_date = datetime.now().date()
    users = member_dao.get_member_slack_ids_by_not_exists_update_date(today_date)

    for user in users:
        howl_message = "<@{}>".format(user) + signature
        slackSender.send(channel_name, token, howl_message)


if __name__ == "__main__":
    scheduler.addScheduleEveryday("23:59", howl)
    scheduler.runScheduler(5)
    uvicorn.run(app, host="0.0.0.0", port=7777)
