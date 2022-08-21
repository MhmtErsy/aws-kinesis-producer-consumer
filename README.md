# aws-kinesis-producer-consumer

Firstly create a virtual environment using requirements.txt

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python producer.py [stream-name] [region] [frequency]

- stream-name: Kinesis stream name
- region: AWS region
- frequency: Data push frequency in second
