provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket = "terraform-state-edc-bt"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}