#!/usr/bin/env python
import time
import datetime
import os

CONFIG = {
    'TIME_DB_FILE': '/etc/chronia.time',  # file where chronia keeps last time
    'TIME_SYNC_INTERVAL': 60,  # seconds between time syncs
    'STARTUP': 15,  # if you can't get time from net in that time, get it from time
}

_BASE_TS = 1440937010  # time less than that is considered unsynced

if __name__ == '__main__':
    # phase 1 - trail time
    for i in xrange(0, CONFIG['STARTUP']):
        if time.time() > _BASE_TS:
            break  # time is synced
        time.sleep(1)
    else:  # time failed to be synced in STARTUP seconds
        try:
            with open(CONFIG['TIME_DB_FILE'], 'rb') as f:
                timestamp = float(f.read())

            # we have time, adjust for uptime
            with open('/proc/uptime', 'r') as f:
                timestamp += int(f.read().split(' ')[0])

            os.system('date -s %s' % (datetime.datetime.fromtimestamp(timestamp).isoformat(),))
        except IOError:
            pass  # I surrender. Wait for NTP sync to resume.

    # phase 2 - wait for NTP sync (will immediately succeed if synced)
    while True:
        time.sleep(10)
        if time.time() > _BASE_TS:
            break

    # time synced. Sync time each X seconds.
    while True:
        time.sleep(CONFIG['TIME_SYNC_INTERVAL'])
        with open(CONFIG['TIME_DB_FILE'], 'wb') as f:
            f.write(str(time.time()))
