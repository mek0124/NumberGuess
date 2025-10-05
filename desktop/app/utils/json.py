import json
import os


class JsonEngine:
    def __init__(self):
        pass

    def get_file_path(self, file_name: str = "user.json") -> str:
        curr_dir = os.path.abspath(os.path.dirname(__file__))
        one_up = os.path.abspath(os.path.dirname(curr_dir))
        data_dir = os.path.join(one_up, "data")

        if not os.path.isdir(data_dir):
            os.makedirs(data_dir, exist_ok=True)

        user_file = os.path.join(data_dir, "user.json")

        if not os.path.isfile(user_file):
            with open(user_file, 'w+', encoding="utf-8-sig") as f:
                json.dump({"history": []}, f, indent=2)

            return user_file
        
        return user_file

    def write_to_json(self, game_dict: dict) -> None:
        user_json_file = self.get_file_path()

        with open(user_json_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)
            data["history"].append(game_dict)

            with open(user_json_file, 'w+', encoding="utf-8-sig") as new:
                json.dump(data, new, indent=2)

        return

    def get_player_history(self) -> list:
        user_json_file = self.get_file_path()

        with open(user_json_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)
            print(data)

            return data["history"]