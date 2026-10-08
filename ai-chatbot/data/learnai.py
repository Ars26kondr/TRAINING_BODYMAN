import json
from datetime import datetime
from zoneinfo import ZoneInfo

def is_rest_time():
    my_timezone=ZoneInfo('Etc/GMT-10')

    now=datetime.now(my_timezone)
    weekday=now.weekday()
    hour=now.hour

    is_father_work=(0<=weekday<5) and (9<=hour<18)

    return not is_father_work

SYSTEM_PROMPT=("Ты - сервисный консультант маркетплейса Farpost.", "Точно разъясняй регламенты клиентам и вежливо отвечай на их вопросы.")

def save_json(path, data):
    with open(path, "w", encoding="UTF-8")as f:
        for user, bot in data:
            entry={"messages":[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user},
                    {"role": "assistant", "content": bot}
                ]
            }
            f.write(json.dumps(entry,ensure_ascii=False) + "\n")

def txt_json(input_file, output_file):
    with open(input_file, "r", encoding="UTF-8") as f, open(output_file, "w", encoding="UTF-8") as out:
        for linenum, line in enumerate(f,1):
            line=line.strip()
            if not line:
                continue
            parts=line.split("/", 1)
            if len(parts)!=2:
                print("Допущена ошибка в строке номер: ", linenum)
            que=parts[0].strip()
            answ=parts[1].strip()
            entry={"messages":[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": que},
                    {"role": "assistant", "content": answ}
                ]
            }
            jlin=json.dumps(entry, ensure_ascii=False)
            out.write(jlin+"\n")

txt_json("data/que_ans.txt", "data/train.jsonl")