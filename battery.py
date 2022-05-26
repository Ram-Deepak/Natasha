import psutil
import datetime
from psutil._common import BatteryTime
import voice_assistant as va

'''if __name__ == '__main__':
    battery_data = psutil.sensors_battery()

    print('Battery power left: {}%'.format(battery_data.percent))

    if battery_data.power_plugged:
        print('Power is connected')
    else:
        print('Power is not connected')
        print('Time left on battery: {}'.format(datetime.timedelta(seconds=battery_data.secsleft)))'''


class Power:

    def __init__(self):
        battery_data = psutil.sensors_battery()

        print('Battery power left: {}%'.format(battery_data.percent))
        va.reply('Battery power left: {}%'.format(battery_data.percent))

        if battery_data.power_plugged:
            print('Power is connected')
            va.reply('Power is connected')
        else:
            print('Power is not connected')
            va.reply('Power is not connected')
            timeleft = str(datetime.timedelta(seconds=battery_data.secsleft)).split(':')
            '''print('Time left on battery: {}'.format(datetime.timedelta(seconds=battery_data.secsleft)))
            va.reply('Time left on battery: {}'.format(datetime.timedelta(seconds=battery_data.secsleft)))'''
            print('Time left on battery: '+str(timeleft[0])+':'+str(timeleft[1])+':'+str(timeleft[2]))
            va.reply('Time left on battery: '+str(timeleft[0])+' hours '+str(timeleft[1])+' minutes '+str(timeleft[2])+' seconds')