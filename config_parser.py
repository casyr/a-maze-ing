class GetConfig():

    def __init__(self) -> None:
        try:
            with open("config.txt", "r") as f:
                self.get_config_info = f.read()
        except FileNotFoundError as e:
            print("ERROR:", e)
        self.dict_config_info: dict[str, str] = {}
        self.info_list = self.get_config_info.split("\n")

    def get_data_config(self) -> dict[str, str]:
        for x in self.info_list:
            key = x.split("=")[0]
            value = x.split("=")[1]
            self.dict_config_info[key] = value
        return (self.dict_config_info)


def main() -> None:
    get_config = GetConfig()
    print(get_config.get_data_config())


if __name__ == "__main__":
    main()
