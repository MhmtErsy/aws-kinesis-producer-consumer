# aws-kinesis-producer-consumer

Firstly create a virtual environment using requirements.txt

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python producer.py --stream [stream name] --region [aws region] --frequency [frequency in second] # PRODUCER
5. python consumer.py --stream [stream name] --region [aws region] # CONSUMER
