import concurrent.futures
import pandas as pd
import requests
import boto3


def upload_file(row):
    s3 = boto3.client('s3', aws_access_key_id="",
                  aws_secret_access_key="")
    bucket_name = "projeto-puc"
    url = row['url']
    response = requests.get(url)
    filename = row['filename']
    response = s3.put_object(Bucket=bucket_name, Key="raw_db/"+filename, Body=response.content)
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
    s3.close()
    return status

df = pd.read_excel('caminho-dados-historicos.xlsx')
df['status'] = ""

# número máximo de threads para executar as requisições
max_workers = 5

with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    tasks = [executor.submit(upload_file, row) for index, row in df.iterrows()]
    
    for index, task in enumerate(tasks):
        status = task.result()
        df.at[index, 'status'] = status

        filename = df.at[index, 'filename']
        if status == 200:
            print(f"Arquivo {filename} enviado para o S3 com sucesso. Status - {status}")
        else:
            print(f"Não foi possível enviar o arquivo {filename}. Status - {status}")

df.to_excel('caminho-dados-historicos.xlsx', index=False)

