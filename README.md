#Python scripts

##RedisPubSub 
Using redis
Two scripts: 
	PubTemperature.py - publishes a message with fake temperature and timestamp in one channel.
	SubTemperature.py - subscribes the channel and receive the message

##TemperatureSensorDS18B20
Two scripts:
	Temperature.py - fetches value from the sensor
	RedisTemperatureTimestamp.py - fetches values from the sensor and store on redis.
	
