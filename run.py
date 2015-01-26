from mongo import *

db = connectToMongo("iwdevb01", "Pass*w0rd!", "dev")
readCollection(db, "persons")

writeCollection(db, "persons", "/tmp")