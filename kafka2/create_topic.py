from confluent_kafka.admin import AdminClient, NewTopic

credentials = {}

with open("kafka1/kraft-client.txt") as file:
    for line in file:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            credentials[key] = value

config = {
    "bootstrap.servers": "kafka.minikube.test:30000",
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "PLAIN",
    "sasl.username": credentials["username"],
    "sasl.password": credentials["password"],
    "ssl.ca.location": "kafka2/certificates/ca.crt",
}

admin = AdminClient(config)

topic = NewTopic("task2-demo", num_partitions=1, replication_factor=1)
futures = admin.create_topics([topic])

for name, future in futures.items():
    try:
        future.result()
        print(f"SUCCESS: Topic '{name}' created!")
    except Exception as error:
        print(f"Topic creation result: {error}")
