from configreader import Configuration


def main():

    #   Single config file load
    singleConfig = Configuration(r".\test data\config.ini")
    print()

    #   Multiple config file load
    # multiConfig = Configuration(r"test data")
    # for keys in multiConfig.multiContent:
    #     print(multiConfig.multiContent[keys].values())


if __name__ == "__main__":
    main()
