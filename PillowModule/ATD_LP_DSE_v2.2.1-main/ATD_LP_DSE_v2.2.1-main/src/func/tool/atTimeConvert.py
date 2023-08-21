import datetime 
from dateutil import tz

class atTime_Convert_Class():

    def to_local(self, time_utc):
        # change utc time to local time
        # time_utc = datetime.datetime(2023, 1, 2, 5, 22, 49, 957783, tzinfo=tz.tzutc())
        # print(time_utc)
        LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
        time_local = (time_utc + datetime.timedelta(hours= int(str(LOCAL_TIMEZONE)))).replace(tzinfo=tz.tzlocal())
        # print(time_local)
        return time_local
    def to_utc(self, time_local):
        # change utc time to local time
        # time_local = datetime.datetime(2023, 1, 2, 5, 22, 49, 957783, tzinfo=tz.tzlocal())
        # print(time_utc)
        LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
        time_utc = (time_local - datetime.timedelta(hours= int(str(LOCAL_TIMEZONE)))).replace(tzinfo=tz.tzutc())
        # print(time_local)
        return time_utc

atTimeConvert = atTime_Convert_Class()

if __name__ == "__main__":
    time = datetime.datetime(2023, 1, 2, 5, 22, 49, 957783, tzinfo=tz.tzutc())
    print("UTC time : " + str(time))
    print("Local time : " + str(atTimeConvert.to_local(time_utc=time)))
    print("Local time : " + str(atTimeConvert.to_utc(time_local=time)))