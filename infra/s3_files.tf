resource "aws_s3_bucket_object" "spark_job" {
  bucket = aws_s3_bucket.datalake.id
  key    = "emr-code/pyspark/spark_job.py"
  acl    = "private"
  source = "../etl/spark_job.py"
  etag   = filemd5("../etl/spark_job.py")
}