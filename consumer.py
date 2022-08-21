import boto3
import json
from datetime import datetime
import time
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--stream', required=True, type=str)
    parser.add_argument('--region', required=True, type=str)
    args = parser.parse_args()

    my_stream_name = args.stream


    kinesis_client = boto3.client('kinesis', region_name=args.region)

    response = kinesis_client.describe_stream(StreamName=my_stream_name)

    my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

    # TRIM_HORIZON means start consumer from earliest record
    shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                        ShardId=my_shard_id,
                                                        ShardIteratorType='TRIM_HORIZON')

    my_shard_iterator = shard_iterator['ShardIterator']

    record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator)


    while 'NextShardIterator' in record_response:
        record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'])

        for i in record_response['Records']:
            print(i)

        print("-----")
        # time.sleep(15)