import boto3
import json
from datetime import datetime
import calendar
import random
import time

my_stream_name = 'my-awesome-stream'
kinesis_client = boto3.client('kinesis', region_name='eu-central-1')

DEVICE_TYPES = ['SMART_HOME', 'INDUSTRIAL_SENSOR', 'INDUSTRIAL_ROBOT', 'HEALTHCARE', 'CAR']
DEVICE_STATUS = ['UP', 'DOWN', 'SHOUTDOWN', 'UNHEALTHY', 'UNKNOWN']
PARTITION_KEY = "pk"

def put_to_stream(device_id, status_timestamp, device_type, device_status):
    payload = {
                'deviceID': str(device_id),
                'statusTimestamp': str(status_timestamp),
                'deviceType': device_type,
                'deviceStatus': device_status
              }

    print(payload)

    put_response = kinesis_client.put_record(
                   StreamName=my_stream_name,
                   Data=json.dumps(payload),
                   PartitionKey=PARTITION_KEY)

    print(put_response)

while True:
    device_id = random.randint(1, 10000)
    status_timestamp = datetime.now()
    device_type = random.choice(DEVICE_TYPES)
    device_status = random.choices(DEVICE_STATUS, weights=[0.6, 0.1, 0.1, 0.1, 0.1])[0]


    put_to_stream(device_id, status_timestamp, device_type, device_status)

    # wait for 5 second
    time.sleep(15)