import redis
import time
import datetime

r=redis.StrictRedis(host='localhost', port=6379, db=0)
i=0
while 1:
	tempfile = open("/sys/bus/w1/devices/28-000006afa537/w1_slave")
	thetext = tempfile.read()
	tempfile.close()
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	tempdata = thetext.split("\n")[1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature / 1000
	i+=1
	user = 'temperature:'+str(i)
	print user
	r.hmset(user, {'value':temperature, 'timestamp':st}) 
	print temperature
	print st
	
	time.sleep(1)


