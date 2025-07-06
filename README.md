# Reddit ETL Pipeline with Airflow, Docker & AWS S3

This project demonstrates an end-to-end **ETL pipeline** that extracts trending posts from Reddit, transforms them into a clean tabular format, and uploads them to an AWS S3 bucket — all orchestrated via **Apache Airflow** running in **Docker containers**.

---

## 📌 Project Summary

| Stage         | Tool/Tech Used                                                   | Description                                            |
| ------------- | ---------------------------------------------------------------- | ------------------------------------------------------ |
| Extract       | [PRAW](https://praw.readthedocs.io/) (Python Reddit API Wrapper) | Fetch top posts from the r/india subreddit             |
| Transform     | `pandas`                                                         | Clean, flatten and structure the post data             |
| Load          | `boto3` + `AWS S3`                                               | Upload transformed CSV to S3 with timestamped filename |
| Orchestration | `Apache Airflow` (via Docker)                                    | DAG to schedule and manage the ETL process daily       |

---

## 🛠️ Features

* Daily scheduled ETL using Airflow
* Clean modular code (`extract.py`, `transform.py`, `upload.py`)
* Dockerized setup with `docker-compose`
* Automatic timestamped S3 uploads
* Robust Airflow DAG with retries & logs

---

## 📂 Project Structure

```
reddit-etl/
├── dags/
│   └── airflow_dag.py            # Airflow DAG definition
├── scripts/
│   ├── extract.py                # Reddit API extraction logic
│   ├── transform.py              # Data transformation
│   └── upload.py                 # S3 upload logic
├── data/
│   └── reddit_top_posts.csv      # Output file (locally stored before upload)
├── .env                          # Reddit API and AWS credentials
├── docker-compose.yaml          # Docker orchestration config
├── requirements.txt             # Python dependencies
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aniketryback/reddit-etl.git
cd reddit-etl
```

### 2. Add Environment Variables

Create a `.env` file with the following:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret
REDDIT_USER_AGENT=your_app_name
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

### 3. Build and Launch Airflow with Docker

```bash
docker-compose up --build
```

### 4. Initialize Airflow DB and Create Admin User (one-time)

```bash
docker-compose run airflow-webserver airflow db init
docker-compose run airflow-webserver airflow users create \
  --username admin \
  --password admin \
  --firstname Aniket \
  --lastname Majumder \
  --role Admin \
  --email aniket@example.com
```

### 5. Access Airflow UI

Go to `http://localhost:8080` and activate the `reddit_etl_pipeline` DAG.

---

## 📈 Sample Output

```
reddit_top_posts_2025-07-06_12-15-39.csv (uploaded to S3)
```

| title                  | score | url                                           | created\_utc |
| ---------------------- | ----- | --------------------------------------------- | ------------ |
| "Reddit India post..." | 2310  | [https://reddit.com/](https://reddit.com/)... | 2025-07-06   |

---

## 🧠 Concepts Covered

* Airflow DAG authoring and scheduling
* Docker container orchestration
* Working with Reddit API via PRAW
* Data transformation using pandas
* Uploading to AWS S3 with boto3
* Managing credentials securely via `.env`

---

## ✨ Future Enhancements

* Use AWS Lambda instead of local Docker
* Store metadata in PostgreSQL or Redshift
* Create Looker Studio dashboards from S3
* Integrate with Slack or Email for notifications

---

## 👨‍💻 Author

**Aniket Majumder**

* Aspiring Data Engineer | Cognizant | India
* [LinkedIn](https://www.linkedin.com/in/aniket-majumder/) | [GitHub](https://github.com/aniketryback)

---

## 📄 License

This project is licensed under the MIT License.
