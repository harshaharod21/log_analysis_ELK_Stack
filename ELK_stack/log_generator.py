from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']

def generate_log():
    return {              
        'message': random.choice(log_levels),
       
    }
   

for _ in range(100):  
    log = generate_log()
    print(f'Sending log: {log}')
    producer.send('logs', log)
    time.sleep(1)