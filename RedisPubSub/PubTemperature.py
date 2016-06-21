import redis
import time
import datetime


pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
#r=redis.StrictRedis(host='localhost', port=6379, db=0)

i=0
while 1:
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	user = 'temperature:'+str(i)
	print user
	r.hmset(user, {'value':'25', 'timestamp':st}) 
	r.publish('temperatureserial', {'value': '25', 'timestamp': st})
	i+=1
	time.sleep(3)


