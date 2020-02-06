from selenium import webdriver

from logins import *
from variable import *

import click
import time as tm


# Main program integrated with Click
@click.command()
@click.argument('site')
@click.option('--custom', '-c', is_flag=True, help="Input any url (without 'http://')")
@click.option('--view', '-v', is_flag=True, help="View Only mode (No Login).")
@click.option('--time', '-t', default='', help="Specify time in seconds.")
def main(custom, view, site, time=''):
    # Core Feature (Login Designation)
    def login(url, userpath, passpath, loginpath, username, password, additional, secs):
        driver = webdriver.Firefox()
        driver.get(url)

        # Finds paths to send credentials
        def credentials():
            driver.find_element_by_xpath(userpath).send_keys(username)
            driver.find_element_by_xpath(passpath).send_keys(password)
            driver.find_element_by_xpath(loginpath).click()

        # Determines what sites need additional step
        if url == mail.url:
            driver.find_element_by_xpath(additional).click()
        credentials()
        # Determines the amount of time to sleep before closing
        if secs:
            tm.sleep(int(secs))
            driver.close()

    # View Only Feature
    # noinspection PyShadowingNames
    def views(site, secs):
        driver = webdriver.Firefox()
        driver.get(eval(site + '.url'))
        if secs:
            tm.sleep(int(secs))
            driver.close()

    # Custom URL feature
    def customs(arg):
        if '.com' not in arg:
            arg = f"{arg}.com"
        driver = webdriver.Firefox()
        driver.get(f"http://{arg}")
        pass

    # Program Start
    if view:
        views(site, time)
    elif custom:
        customs(site)
        return
    else:
        try:
            login(eval(site + '.url'), eval(site + '.userpath'), eval(site + '.passpath'), eval(site + '.loginpath'),
                  eval('usr.' + site), eval('pwd.' + site), eval(site + '.additional'), time)
        except SyntaxError:
            main(site)
        except NameError:
            main(site)
        except AttributeError:
            print("Understood.")

    print(f"\nSuccessfully viewed {eval(site + '.name')} \n")
    if time:
        print(f"\n Closed after {time} seconds.\n")
    # Program End


if __name__ == "__main__":
    main()
