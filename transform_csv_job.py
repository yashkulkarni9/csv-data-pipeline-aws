import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_data = glueContext.create_dynamic_frame.from_catalog(
    database="DB_NAME",
    table_name="ACUAL_TABLE_NAME"
)

glueContext.write_dynamic_frame.from_options(
    frame=input_data,
    connection_type="s3",
    connection_options={"path": "S3_OUTPUT_BUCKET_PATH"},
    format="csv"
)

job.commit()
