
resource "aws_s3_bucket" "datalake"{
    bucket = "$(var.base_bucket_name)-$(var.ambiente)-$(var.numero_conta)"
    acl = "private"
    description  = "My first bucket s3"

    server_side_encryption_configuration {
        rule {
            apply_server_side_encryption_by_default {
                sse_algorithm     = "AES256"
            }
        }
    }
}

resource "aws_s3_bucket_object" "code_spark"{
    # nome do bucket criado acima
    bucket = aws_s3_bucket.datalake.id
    key = "emr-code/pyspark/job_spark_from_tf.py"
    acl = "private"
    source = "../job_spark.py"
    etag = filemd5("../job_spark.py")
}

provider "aws" {
    region = "$(var.region)"
}