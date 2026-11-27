from confluent_kafka import Consumer

credentials = {}

with open("kafka1/kraft-client.txt") as file:
    for line in file:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            credentials[key] = value

config = {
    "bootstrap.servers": "kafka.minikube.test:19092",
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "PLAIN",
    "sasl.username": credentials["username"],
    "sasl.password": credentials["password"],
    "ssl.ca.location": "kafka2/certificates/ca.crt",
    "group.id": "task2-demo-consumer",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": False,
}

consumer = Consumer(config)
consumer.subscribe(["task2-demo"])

try:
    message = consumer.poll(20)

    if message is None:
        print("No message received within 20 seconds.")
    elif message.error():
        print("Consumer error:", message.error())
    else:
        print("SUCCESS: Message consumed!")
        print("Topic:", message.topic())
        print("Key:", message.key().decode() if message.key() else None)
        print("Value:", message.value().decode())
finally:
    consumer.close()