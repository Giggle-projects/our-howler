from datetime import datetime

file_path = "member.txt"
date_format = '%Y-%m-%d/%H:%M:%S'
username_index = 1
slack_id_index = 2
score_index = 3
date_index = 4


def get_score():
    scoreboards = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_data = line.split()
            scoreboards.append(line_data[username_index] + " " + line_data[score_index])

    return ', '.join(scoreboards)


def update_score(target_username):
    now = datetime.now()

    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(lines)

    for i, line in enumerate(lines):
        db_id, username, slack_id, score, now_time = line.split()
        if username == target_username:
            new_score = str(int(score) + 1)
            lines[i] = f"{db_id} {username} {slack_id} {new_score} {now.strftime(date_format)}\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)
    file.close()

    return new_score


def get_today_do_not_upload_users():
    today_date = str(datetime.now().date())

    not_upload_users = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line_split = line.split()
            user_date_info = line_split[date_index].split('/')[0]

            if today_date != user_date_info:
                user_slack_id = line_split[slack_id_index]
                not_upload_users.append(user_slack_id)

    return not_upload_users
