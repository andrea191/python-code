import redis
import time
import datetime


pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
#r=redis.StrictRedis(host='localhost', port=6379, db=0)

i=0
p = r.pubsub()

p.subscribe('temperatureserial')

while True:
	message = p.get_message()
	if i==0 and message:
		print message
		i+=1
	elif message:
		print message
		print type(message)
		data = message['data']
		print data
		print type(data)
		value = data[1:3]
		print type(value)
		print value
	time.sleep(0.001)


