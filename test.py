file_path = "member.txt"

result = []
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line_split = line.split()
        result.append(line_split[1] + " " + line_split[3])

member_score = ', '.join(result)
print(member_score)

