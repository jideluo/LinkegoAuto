from bin.getperformance import MonkeyTest,MonkeyMtkLog

sn ="8681-M02-0x729bcc98"
delay = 60*30



mtest=MonkeyTest.MonkeyData(sn)
mlog=MonkeyMtkLog.MonkeyLog(sn,delay)

mtest.start()
mlog.start()
mtest.join()
mlog.join()




