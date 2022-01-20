import datetime
from Modules.clear_scr import clr_scr
import __main__


def check_timeout(time):
    time_diff = datetime.datetime.now() - time
    if time_diff.seconds + time_diff.days * 24 * 3600 > 300:
        clr_scr()
        print("\nYou have been logged out due to inactivity")
        __main__.current_user = None
        return False
    return True
