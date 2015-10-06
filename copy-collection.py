from mongo import *

readdb = connectToMongo("iwtestb01", "Pass*w0rd!", "test", "test")
writedb = connectToMongo("iwusgtestb01", "ZmVhM2UyOT", "usgtest", "usgtest")

writeCollectionToDb(readdb, writedb, "usgtest", "system_setting", "system_setting")