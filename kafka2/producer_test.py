from confluent_kafka import Producer

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
}

producer = Producer(config)

producer.produce(
    "task2-demo",
    key="test-key",
    value="Hello from external Kafka producer!"
)

producer.flush()
print("SUCCESS: Message produced!")