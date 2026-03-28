class GetConfig():

    def __init__(self) -> None:
        try:
            with open("config.txt", "r") as f:
                self.get_config_info = f.read()
        except FileNotFoundError as e:
            print("ERROR:", e)

    def get_data_config(self) -> dict[str, str]:
        dict_config_info: dict[str, str] = {}
        info_list = self.get_config_info.split("\n")
        for x in info_list:
            key = x.split("=")[0]
            value = x.split("=")[1]
            dict_config_info[key] = value
        return (dict_config_info)
