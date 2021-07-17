from fake_web_events import Simulation
import boto3 
import json

client = boto3.client('firehose', region_name='us-west-2', aws_access_key_id='edson-at-616310343000',aws_secret_access_key='peoeV6yjUTyBCCrdXn7WmX5MiCdJP9csu9XZemSOZaQ')

def put_record(event):
    data = json.dumps(event) + "\n"
    response = client.put_record(
        DeliveryStreamName = 'bootcamp-aula-web-events',
        Record = {"Data": data}
    )
    print(event)
    return response


simulation = Simulation(user_pool_size=100, sessions_per_day=100000)
events = simulation.run(duration_seconds=600)
 
for event in events:
    put_record(event)
    





