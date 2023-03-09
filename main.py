def run_the_scraper():
    # some func
    pass


def check_for_start_scraper() -> bool:
    i = 0
    while i < 1:
        input_user_choice = str(input("Should the scrapping be started?: "))
        if input_user_choice.lower() == 'n':
            return False
        elif input_user_choice.lower() == 'y':
            i = 1
            return True
        else:
            print("INPUT_NOT_VALID")


if __name__ == "__main__":
    while True:
        print("MESSAGE_HOW_START_STOP_SCRAPER")
        if not check_for_start_scraper():
            break
        run_the_scraper()
        print("scrapping results")
