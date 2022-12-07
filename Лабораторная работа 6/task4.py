import json
INPUT_FILE = "new_input.csv"

def csv_to_list_dict(file, delimiter=',', new_line='\n') -> list[dict]:
    with open(INPUT_FILE, 'rt') as f:
        keys = f.read().strip().split(new_line)
        result = dict()
        json_list = list()
        for num, val in enumerate(keys):
            if num == 0: heades = val.split(delimiter)
            else: rows = val.split(delimiter)
            if num > 0:
                for num_2, val_2 in enumerate(heades):
                    result[val_2] = rows[num_2]
                result_2 = result.copy()
                json_list.append(result_2)
        return json_list

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
