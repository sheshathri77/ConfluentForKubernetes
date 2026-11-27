# Confluent Platform (CFK) and Apache Flink Integration

## 1. Project Overview

This project focuses on deploying Confluent Platform using Confluent for Kubernetes (CFK), configuring external Kafka connectivity, enabling TLS and Role-Based Access Control (RBAC) using Metadata Service (MDS), and integrating Apache Flink for real-time stream processing.

The implementation and testing have primarily been performed in a local Kubernetes environment using Minikube. OpenShift/ROSA-specific validation remains pending.

## 2. Project Objectives

The project consists of four major deliverables:

1. Deploy Confluent Platform on OpenShift using CFK, including Kafka brokers, Schema Registry, Kafka Connect and Control Center.
2. Expose Kafka outside the cluster using external listeners and connect external clients.
3. Enable TLS and RBAC with Metadata Service (MDS).
4. Deploy Apache Flink alongside CFK and execute a streaming job that reads from and writes to Kafka topics.

## 3. Technology Stack

| Technology | Version / Configuration |
|---|---|
| Kubernetes | Minikube |
| Confluent for Kubernetes | 3.4.0 |
| Confluent Server | 8.3.0 |
| Apache Flink | 2.3.0 |
| Kafka SQL Connector | 5.1.0 |
| Python Kafka Client | confluent-kafka |
| Authentication | SASL/PLAIN |
| Encryption | TLS |
| Namespace | confluent |

## 4. Architecture Overview

The architecture consists of a Confluent Kafka cluster managed by CFK, with Kafka brokers and a KRaft controller.

External Python producer and consumer applications connect to Kafka through external listeners using SASL/PLAIN authentication over TLS.

MDS provides authentication and RBAC capabilities.

Apache Flink is deployed alongside Kafka using a JobManager and TaskManager. A Flink SQL streaming job consumes messages from the `flink-input` topic and writes processed messages to the `flink-output` topic.

## 5. Deliverable Progress

### Deliverable 1: Deploy Confluent Platform Using CFK

**Status: Partially Completed**

- Deployed Kafka brokers and KRaft controller using CFK 3.4.0.
- Configured the Kafka cluster in the `confluent` namespace.
- Verified that Kafka and KRaft pods are running.
- Schema Registry, Kafka Connect and Control Center deployment status requires further verification.

### Deliverable 2: External Kafka Connectivity

**Status: Core Connectivity Tested**

- Configured external Kafka listeners using NodePort services.
- Configured bootstrap NodePort `30000` and broker NodePort `30001`.
- Configured external hostname `kafka.minikube.test`.
- Connected external Python producer and consumer applications.
- Successfully tested Kafka connectivity using SASL/PLAIN authentication over TLS.
- OpenShift Route-based exposure remains pending.

### Deliverable 3: TLS and RBAC With MDS

**Status: Local Security Validation Completed**

- Enabled TLS encryption for Kafka listeners.
- Configured SASL/PLAIN authentication.
- Configured Metadata Service (MDS) and Role-Based Access Control (RBAC).
- Validated administrator authentication.
- Validated reader authentication and authorized topic access.
- Tested unauthorized write operations and confirmed access rejection (HTTP 40301).
- Stored functional testing evidence in the `deliverable3-evidence/` directory.

### Deliverable 4: Apache Flink Integration

**Status: Streaming Job Submitted; End-to-End Validation Pending**

- Deployed Flink JobManager and TaskManager in the `confluent` namespace.
- Configured Flink REST API and dashboard access.
- Integrated the Kafka SQL connector.
- Configured authenticated Kafka connectivity using TLS and SASL/PLAIN.
- Created Kafka topics `flink-input` and `flink-output`.
- Created Flink SQL source and sink table definitions.
- Successfully submitted a streaming job named `cfk-flink-kafka-demo`.
- Latest observed job state was `RUNNING`.

The remaining task is to verify successful task execution and confirm actual message delivery from `flink-input` to `flink-output`.

## 6. Important Configuration and Commands

### Check Kubernetes Resources

```bash
kubectl get pods -n confluent
kubectl get services -n confluent
kubectl get kafka -n confluent

##New branch