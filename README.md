# ELK Stack with Kafka for Log Analysis and Visualization

This project implements a logging and monitoring solution using the **ELK Stack (Elasticsearch, Logstash, Kibana)** integrated with **Apache Kafka** for real-time log data streaming, analysis, and visualization.

## Architecture Overview

- **Kafka**: Acts as a distributed data streaming platform to ingest logs in real time.
- **Logstash**: Configured to pull data from Kafka, process it, and send it to Elasticsearch.
- **Elasticsearch**: Stores and indexes the processed log data, allowing for fast search and retrieval.
- **Kibana**: Visualizes the data stored in Elasticsearch, providing dashboards and analytics.

## Prerequisites

- **Docker & Docker Compose**: Recommended for setting up the stack quickly.
- **Sufficient Memory**: ELK stack requires at least 4GB of RAM to run smoothly.

## Installation Steps

1. **Clone Repository**:
```bash
   git clone <repository-url>
   cd elk-kafka-log-analysis
```
   
2. **Set Up Docker Containers**:
   - Start all services (Elasticsearch, Logstash, Kibana, Kafka, and Zookeeper) with Docker Compose.
```bash
   docker-compose up -d
```
   
3.**Run from terminal**:

```bash
docker-compose up -d
```
- Change the directory to ELK_stack and run:
```bash
docker-compose up -d
```
4. **Run python file**

Run the log generator file:
```bash
python log_generator.py
```
5.**Access Kibana**:

Visit http://localhost:5601 to access Kibana.

## Usage

### Send Logs to Kafka:
- Produce log data into Kafka using log-producing clients or scripts.

### Logstash Processing:
- Logstash pulls data from Kafka, applies transformations, and sends it to Elasticsearch.

### Visualize in Kibana:
- Create index patterns, dashboards, and visualizations in Kibana to monitor and analyze log data in real time.





