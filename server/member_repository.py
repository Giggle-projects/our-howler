from datetime import datetime

file_path = "member.txt"
date_format = '%Y/%m/%d/%H:%M:%S'


def insert_user(target_username):
    now = datetime.now()

    with open(file_path, 'a+') as file:
        file.write(f"\n{target_username} 0 {now.strftime(date_format)}")

        file.seek(0)
        lines = file.readlines()
        return len(lines)


def update_score(target_username):
    now = datetime.now()

    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(lines)

    for i, line in enumerate(lines):
        username, score, now_time = line.split()
        if username == target_username:
            new_score = str(int(score) + 1)
            lines[i] = f"{username} {new_score} {now.strftime(date_format)}\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)
    file.close()

    return new_score
