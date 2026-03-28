class GetConfig():

    def __init__(self, config_file_name: str) -> None:
        try:
            with open(config_file_name, "r") as f:
                self.get_config_info = f.read()
        except FileNotFoundError as e:
            print("ERROR:", e)

    def get_data_config(self) -> dict[str, str]:
        dict_config_file: dict[str, str] = {}
        list_config_file = self.get_config_info.split("\n")
        for x in list_config_file:
            key = x.split("=")[0]
            value = x.split("=")[1]
            dict_config_file[key] = value
        return (dict_config_file)
