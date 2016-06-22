import redis
import time
import datetime

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
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
	channel = 'temperatureId'
	hashKey = channel+':'+ts;
	print hashKey
	print temperature
	print st
	print i 
	r.hmset(hashKey, {'value':temperature, 'timestamp':st, 'log_counter': i}) 
	r.publish(channel, {'value':temperature, 'timestamp':st, 'log_counter': i, 'hashKey': hashKey})
	i+=1
	time.sleep(1)


