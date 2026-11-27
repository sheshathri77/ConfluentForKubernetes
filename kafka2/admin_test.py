from confluent_kafka.admin import AdminClient

credentials = {}

with open("kafka1/kraft-client.txt", "r") as file:
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

try:
    metadata = admin.list_topics(timeout=20)
    print("SUCCESS: Authenticated Kafka connection established!")
    print("Cluster ID:", metadata.cluster_id)
    print("Brokers:", list(metadata.brokers.keys()))
except Exception as error:
    print("Kafka connection failed:", error)
