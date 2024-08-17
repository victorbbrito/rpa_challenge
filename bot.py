from botcity.web import WebBot, Browser, By

from botcity.maestro import *

from webdriver_manager.chrome import ChromeDriverManager

from pathlib import Path

from utils import fill_out_form, collect_data , check_download

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()

    bot.browse("https://www.rpachallenge.com/")

    # Download file, to extract data
    if check_download() :
        bot.navigate_to("https://www.rpachallenge.com/assets/downloadFiles/challenge.xlsx")

    start_button = bot.find_element('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button', By.XPATH)

    start_button.click()

    list_persons = collect_data("challenge.xlsx")

    fill_out_form(bot,list_persons)

    mesage = bot.find_element("/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]", By.XPATH)
    print(mesage.get_attribute("innerHTML"))

    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
