import uvicorn
from fastapi import FastAPI, Form
from datetime import datetime

from starlette.requests import Request
import slackSender
import scheduler
import member_dao

signature = " 너 도태될꺼야? 공부해 이놈아!\n" \
            "*<https://github.com/Giggle-projects/our-howler|Github - our howler>*"

channel_name = "howler-alert"
token = "xoxb-2476610625797-6307304308496-zxqnhlXdCLF90D9PwOUR3chk"

app = FastAPI()


@app.post("/")
async def say_anything(
        request: Request
):
    form = await request.form()

    # These are from slack slash command request
    # This request contains a data payload describing the source command and who invoked it.

    token = form["token"]
    team_id = form["team_id"]
    team_domain = form["team_domain"]
    channel_id = form["channel_id"]
    channel_name = form["channel_name"]
    user_id = form["user_id"]
    user_name = form["user_name"]
    command = form["command"]
    text = form["text"]
    response_url = form["response_url"]
    trigger_id = form["trigger_id"]
    api_app_id = form["api_app_id"]
    return "<@{}>".format(user_id) + signature


@app.post("/hey")
def health():
    return "hi"


@app.get("/score")
def get_score():
    members_score = member_dao.get_score()
    return {members_score}


@app.post("/update/{target_username}")
def update_score(target_username):
    new_score = member_dao.update_score(target_username)
    return {new_score}


@app.get("/test")
def get_do_not_upload_users():
    today_date = datetime.now().date()
    users = member_dao.get_member_slack_ids_by_not_exists_update_date(today_date)
    test = ', '.join(users)
    return {test}


def howl():
    today_date = datetime.now().date()
    users = member_dao.get_member_slack_ids_by_not_exists_update_date(today_date)

    for user in users:
        howl_message = "<@{}>".format(user) + signature
        slackSender.send(channel_name, token, howl_message)


if __name__ == "__main__":
    scheduler.addScheduleEveryday("01:22", howl)
    scheduler.runScheduler(5)
    uvicorn.run(app, host="0.0.0.0", port=7777)
