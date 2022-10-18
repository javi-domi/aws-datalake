resource "aws_glue_catalog_database" "datalake" {
  name = "datalakedb"
}

resource "aws_glue_crawler" "datalake" {
  name          = "datalake_s3_crawler"
  role          = aws_iam_role.glue_role.arn
  database_name = aws_glue_catalog_database.datalake.name
  schedule      = "cron(0 12 * * ? *)"
  s3_target {
    path = "s3://${aws_s3_bucket.datalake.id}/staging/"
  }

  configuration = <<EOF
{
   "Version": 1.0,
   "Grouping": {
      "TableGroupingPolicy": "CombineCompatibleSchemas" }
}
EOF

  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }
}