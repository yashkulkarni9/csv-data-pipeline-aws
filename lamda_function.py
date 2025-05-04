import boto3
import csv
import os
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    destination_bucket = os.environ['DEST_BUCKET']

    response = s3.get_object(Bucket=source_bucket, Key=object_key)
    content = response['Body'].read().decode('utf-8').splitlines()

    reader = csv.reader(content)
    header = next(reader)
    cleaned_rows = [header]

    for row in reader:
        if all(row): 
            cleaned_rows.append(row)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(cleaned_rows)
    output.seek(0)

    cleaned_key = "processed_" + object_key
    s3.put_object(Bucket=destination_bucket, Key=cleaned_key, Body=output.getvalue())

    return {
        'statusCode': 200,
        'body': f"Processed {object_key} and stored as {cleaned_key}."
    }
