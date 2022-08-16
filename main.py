import time
from datetime import datetime
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def site_block():
    # Time at which blocking starts
    start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9)
    # Time at which blocking stops
    finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 10)

    print(start_time)
    print(finish_time)

    hosts = r'C:\Windows\System32\drivers\etc\hosts'
    # hosts = '/etc/hosts'
    redirect_url = '127.0.0.1'

    blocked_sites = ['www.youtube.com', 'youtube.com', 'www.vk.com', 'vk.com']

    while True:
        if start_time < datetime.now() < finish_time:
            print('Доступ ограничен!')

            with open(hosts, 'r+') as file:
                src = file.read()

                for site in blocked_sites:
                    if site in src:
                        pass
                    else:
                        file.write(f'{redirect_url} {site}\n')
        else:
            with open(hosts, 'r+') as file:
                src = file.readlines()
                file.seek(0)

                for line in src:
                    if not any(site in line for site in blocked_sites):
                        file.write(line)
                file.truncate()
            print('Доступ открыт!')

        time.sleep(5)


if __name__ == '__main__':
    if is_admin():
        site_block()

    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
