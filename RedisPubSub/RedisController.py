import redis
import time
import datetime


pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
i=0

#Type of sensors
sensorList = 'sensor:type'
'''
temperatureSensor = 'temperature'
accelerometerSensor = 'accelerometer'

#Temperature sensors '''
temperatureList = 'sensor:temperature'

'''
#The sensor
temperatureKey = 'temperature:TEMP0000'

#LWM2M checks if the sensor exist, and create the instance. 
#If doesn't exist anymore, the instance will be deleted.
r.sadd(temperatureList, temperatureSerial) 

#If no fetch for more than 2 seconds, the sensor is dead.
#Then removed, and another process will delete the sensor from 
#temperatureList set. So, the LWM2M will be updated.
r.setex(temperatureSerialIdKey, )
'''
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


