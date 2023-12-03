from datetime import datetime

file_path = "member.txt"
date_format = '%Y/%m/%d/%H:%M:%S'
username_index = 1
score_index = 3


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
