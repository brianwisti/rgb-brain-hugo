---
created: 2024-03-08 20:43:33-08:00
title: Apache Airflow
updated: 2024-05-07 15:16:49-07:00
---

## Apache Airflow

Platform to author, schedule and monitor workflows in [Python](Python.md)

## Jots

Interacts with all components (RDBMS, Spark, Hadoop, etc.) using *operators* and *connections*

## Terms

DAG (workflow)
: sequence of *Tasks* to process a set of data

Task
: created by instantiating and configuring an *Operator* class

Task Instance
: created by executing a *Task* in the context of a particular *DAG Run*

### Related

* [Apache Airflow](https://airflow.apache.org)
* [What is Airflow — Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
* [1. What is Apache Airflow Airflow Beginners Tutorial - YouTube](https://www.youtube.com/watch?v=4aB1NE6qQzs)