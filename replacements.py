import tempfile, json

def doPlaceHolders(filename, customerName, hostName):
	fp = tempfile.TemporaryFile()
	inputFile = open(filename, 'r')
    for line in inputFile:
		line = line.replace('#customerName#', customerName)
		line = line.replace('#host#', hostName)
		fp.write(line)

	fp.seek(0)
	try:
	data = json.load(fp)
	return data
	except (TypeError,ValueError), exception:
	logging.error('%s %s',filename, exception)
	return
