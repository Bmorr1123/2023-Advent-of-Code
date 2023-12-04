import os

highest_input = 0
highest_day = 0
highest_mission = 0


files = os.listdir()
for file in files:
    if file.endswith("-input.txt"):
        num = int(file[:file.find("-")])
        highest_input = max(highest_input, num)
    if file.endswith("-code.py"):
        period = file.find(".")
        day = int(file[:period])
        mission = int(file[period+1:file.find("-")])

        if day >= highest_day:
            highest_day = day
            highest_mission = 0
            highest_mission = max(highest_mission, mission)

make_code = False
make_day, make_mission = 0, 1

text_content = ""

if highest_day < highest_input:
    file_name = f"{highest_input:02d}.1-code.py"
elif highest_mission == 1:
    file_name = f"{highest_input:02d}.2-code.py"
    with open(f"{highest_input:02d}.1-code.py", "r") as file:
        for line in file.readlines():
            text_content += line
else:
    file_name = f"{highest_day + 1:02d}-input.txt"

print(f"Making {file_name}")
if file_name not in files:
    out_file = open(file_name, "w+")
    if text_content:
        out_file.write(text_content)
    out_file.close()

