from beacontools import parse_packet
import paho.mqtt.client as mqtt
import json
import mysql.connector
from mysql.connector import MySQLConnection, Error
from mysql.connector import errorcode
from datetime import datetime
import os, time
from pytz import timezone
from python_mysql_dbconfig import read_db_config, read_mqtt_config


fmt = '%Y-%m-%d %H:%M:%S'
# define eastern timezone
eastern = timezone('Asia/Kathmandu')
naive_dt = datetime.now()
logFile = r'errorfile.txt'
with open(logFile, 'w') as f:
    f.write('File created\n')




try:
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    if conn.is_connected():
        print('Connected to MySQL database')

except mysql.connector.Error as error:
    print(error)
    with open(logFile, 'a') as f:
        loc_dt = datetime.now(eastern)
        print("Error = {} \n Time = {} \n".format(error, loc_dt.strftime(fmt)), file = f)
        

    




# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    #Subscribing in on_connect() means that if we lose the connection and
    #reconnect then subscriptions will be renewed.
    #client.subscribe("gwt/ble/office")
    client.subscribe("gwt/ble/#", 2)

def insertChar(mystring, position, chartoinsert ):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring

def print_list(packet):
    #global uid_frame
    uid_frame = parse_packet(packet)
    d = dict();  
    
    try:
        d['Namespace'] = uid_frame.namespac
    except:
        pass
    try:
        d['Instance'] = uid_frame.instance
    except:
        pass
    
    try:
        d['TX Power'] = uid_frame.tx_power
        
    except:
        pass
    try:
        d['TX Power'] = uid_frame.tx_power
    except:
        pass
    try:
        d['URL'] = uid_frame.url
    except:
        pass
    try:
        d['Voltage'] = uid_frame.voltage
    except:
        pass
    try:
        d['Temperature'] = uid_frame.temperature
    except:
        pass
    try:
        d['Temperature (8.8 fixed point)'] = uid_frame.temperature_fixed_point
    except:
        pass
    try:
        d['Advertising count'] = uid_frame.advertising_count
    except:
        pass
    try:
        d['Seconds since boot'] = uid_frame.seconds_since_boot
    except:
        pass
    try:
        d['Data'] = uid_frame.encrypted_data
    except:
        pass
    try:
        d['Salt'] = uid_frame.salt
    except:
        pass
    try:
        d['Mic'] = uid_frame.mic
    except:
        pass
    try:
        d['UUID'] = uid_frame.uuid
    except:
        pass
    try:
        d['Major'] = uid_frame.major
    except:
        pass
    try:
        d['Minor'] = uid_frame.minor
    except:
        pass
    try:
        d['TX Power'] = uid_frame.tx_power
    except:
        pass
    try:
        print("UUID: %s" % uid_frame.uuid)
        #d['Instance'] = uid_frame.instance
    except:
        pass
    try:
        print("Major: %d" % uid_frame.major)
        #d['Instance'] = uid_frame.instance
    except:
        pass
    try:
        d['Temperature cypress'] = uid_frame.cypress_temperature
    except:
        pass
    try:
        d['Humidity cypress'] = uid_frame.cypress_humidity
    except:
        pass
    try:
        d['Identifier'] = uid_frame.identifier
    except:
        pass
    try:
        d['Protocol Version'] = uid_frame.protocol_version
    except:
        pass
    try:
        d['Acceleration (g)'] = uid_frame.acceleration
    except:
        pass
    try:
        d['Is moving'] = uid_frame.is_moving
    except:
        pass
    try:
        print("Identifier: %s" % uid_frame.identifier)
        #d['Instance'] = uid_frame.instance
    except:
        pass
    try:
        d['Protocol Version'] = uid_frame.protocol_version
    except:
        pass
    try:
        d['Magnetic field'] = uid_frame.magnetic_field
    except:
        pass
    return d 


def insert_temphum(temp, hum, gmac, dmac, rssi):
    try:
        mySql_insert_query = """INSERT INTO dataontemp(temp, humidity, deviceId, cDate) 
                               VALUES(%s, %s, %s, %s) """
        recordTuple = (temp, hum, "1", int(time.time()))
        cursor = conn.cursor()
        cursor.execute(mySql_insert_query, recordTuple)
        conn.commit()
        print("Record inserted successfully into table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into table {}".format(error))
        with open(logFile, 'a') as f:
            loc_dt = datetime.now(eastern)
            print("Error = {} \n Time = {} \n".format(error, loc_dt.strftime(fmt)), file = f)

 
# The callback for when a PUBLISH message is received from the server.


def reversestr(s):
    return("".join(map(str.__add__, s[-2::-2] ,s[-1::-2])))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    mqtt_payload = json.loads(msg.payload)
    #print(mqtt_payload['msg'])
    #data = mqtt_payload['obj'][0]['data1']
    data_length = len(mqtt_payload['obj'])
    print(data_length)
    for i in range(0, data_length):
        print("loop {}".format(i+1))
        data = mqtt_payload['obj'][i]['data1']
        print("data = {}".format(data))
        data_in_hex = bytes.fromhex(data)
        d = print_list(data_in_hex)
        try:
            print(d['UUID'])
            print(d['Major'])
            print(d['Minor'])
            # the sensor returns temperature and  humidity data in the minor
            minor = hex(d['Minor']).lstrip("0x")
            print(minor)
            minor = str(minor)
            print(minor)
            print("Data is")
            print(minor[0:2])
            humidity = int((minor[0:2]),16)
            temperature = int((minor[2:4]),16)
            print ("Humidity : {}".format(humidity))
            print ("Temp : {}".format(temperature))
            print(mqtt_payload['gmac'])
            print(mqtt_payload['obj'][i]['dmac'])
            print(mqtt_payload['obj'][i]['rssi'])
            dmac = mqtt_payload['obj'][i]['dmac']
            print(dmac)
            dmac = reversestr(dmac)
            print(dmac)
            insert_temphum(temperature, humidity, mqtt_payload['gmac'], dmac, mqtt_payload['obj'][i]['rssi'] )
        except:
            pass
            
        

mqttconfig = read_mqtt_config()
broker_address = mqttconfig['broker_address']
port = mqttconfig['port']                         #Broker port
user = mqttconfig['user']
password = mqttconfig['password']



client = mqtt.Client()
client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


 
