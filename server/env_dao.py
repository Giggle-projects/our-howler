file_path = "secret-env.txt"


def init():
    env_map = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_data = line.split("=")
            env_map[line_data[0]] = line_data[1]
    return env_map


