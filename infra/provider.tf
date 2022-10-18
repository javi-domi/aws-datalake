provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket = "terraform-state-edc"
    key    = "state/edc/mod1/terraform.tfstate"
    region = "us-east-1"
  }
}