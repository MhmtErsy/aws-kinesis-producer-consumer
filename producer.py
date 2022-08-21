import boto3
import json
import argparse
from datetime import datetime
import calendar
import random
import time



DEVICE_TYPES = ['SMART_HOME', 'INDUSTRIAL_SENSOR', 'INDUSTRIAL_ROBOT', 'HEALTHCARE', 'CAR']
DEVICE_STATUS = ['UP', 'DOWN', 'SHOUTDOWN', 'UNHEALTHY', 'UNKNOWN']
PARTITION_KEY = "pk"

def get_kinesis_client(aws_region):
    kinesis_client = boto3.client('kinesis', region_name=aws_region)
    return kinesis_client

def put_to_stream(kinesis_client, stream_name, device_id, status_timestamp, device_type, device_status):
    payload = {
                'deviceID': str(device_id),
                'statusTimestamp': str(status_timestamp),
                'deviceType': device_type,
                'deviceStatus': device_status
              }

    print(payload)

    put_response = kinesis_client.put_record(
                   StreamName=stream_name,
                   Data=json.dumps(payload),
                   PartitionKey=PARTITION_KEY)

    print(put_response)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--stream', required=True, type=str)
    parser.add_argument('--region', required=True, type=str)
    parser.add_argument('--frequency', required=True, type=int)

    args = parser.parse_args()

    while True:
        device_id = random.randint(1, 100000)
        status_timestamp = datetime.now()
        device_type = random.choice(DEVICE_TYPES)
        device_status = random.choices(DEVICE_STATUS, weights=[0.6, 0.1, 0.1, 0.1, 0.1])[0]

        kinesis_client = get_kinesis_client(args.region)
        put_to_stream(kinesis_client, args.stream, device_id, status_timestamp, device_type, device_status)

        # wait for 5 second
        time.sleep(args.frequency)