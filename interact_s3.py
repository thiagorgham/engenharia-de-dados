import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.download_file("datalake-enem2020",
                        "data/enem2020.csv",
                        "data/enem2020.csv")

df = pd.read_csv("data/enem2020.csv", sep=";")
print(df)

s3_client.upload_file("data/enem2020_upload.csv",
                    "datalake-enem2020",
                    "data/enem2020_upload.csv")