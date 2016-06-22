import redis
import time
import datetime

#Subscribed to the keyevent expired.
#Any sensor will expire, the controller will remove it from the ONLINE list
#So the LWM2M can create and delete the IPSO Object instance

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
i=0

#Type of sensors
sensorList = 'sensor:type'

#Temperature sensors
temperatureList = 'sensor:temperature'

pubsub = r.pubsub()
pubsub.psubscribe('__keyevent@0__:expired')

print 'Sensor List' + str(r.smembers(sensorList))
print 'Temperature sensor List' + str(r.smembers(temperatureList))


while 1:
	message = pubsub.get_message()
	if message != None and message['data'] != 1:
		#because the first message says the number of subscribers
		sensorSerial = message['data']
		print sensorSerial

		if r.scard(temperatureList) == 1:
			r.srem(sensorList, 'temperature')
		r.srem(temperatureList, sensorSerial)
		print 'Sensor List' + str(r.smembers(sensorList))
		print 'Temperature sensor List' + str(r.smembers(temperatureList))
	time.sleep(0.001)


