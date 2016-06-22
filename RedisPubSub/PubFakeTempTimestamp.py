import redis
import time
import datetime


pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
i=0

#Type of sensors 
sensorList = 'sensor:type'
temperatureSensor = 'temperature'
accelerometerSensor = 'accelerometer'

#Temperature sensors 
temperatureList = 'sensor:'+temperatureSensor
temperatureSerial = 'TEMP0000'

#The sensor
temperatureKey = 'temperature:'+temperatureSerial

#temperatureAlive = temperatureSerial+':alive'
temperatureAlive = temperatureSerial
temperatureInfo = temperatureSerial+':info'

##SET of type of sensors CONNECTED
r.sadd(sensorList, temperatureSensor)

##SET of temperature sensor CONNECTED
#RedisController.py checks if the sensor is working
#If it is not working, 
#LWM2M checks if the sensor exist, and create the instance. 
#If doesn't exist anymore, the instance will be deleted.
r.sadd(temperatureList, temperatureSerial) 


##SET of temperature sensor data
r.sadd(temperatureKey, 'info', 'alive')

##Verify if the sensor is connected
#If no fetch for more than 2 seconds, the sensor is dead.
#Then removed, and another process will delete the sensor from 
#temperatureList set. So, the LWM2M will be updated.
r.set(temperatureAlive, 'yes')
r.expire(temperatureAlive, 5) #If it is not extended, will expire

while 1:
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	temperature = 25.95
	channel = temperatureSerial
	hashKey = temperatureSerial+':'+str(i);
	print hashKey, temperature, st, i
	r.hmset(hashKey, {'value':temperature, 'timestamp':st, 'logCounter': i}) 
	r.publish(channel, {"value":temperature, "timestamp":st, "logCounter": i, "hashKey": hashKey})
	i+=1
	r.expire(temperatureAlive, 3)
	time.sleep(1)  



