provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket = "terraform-state-edc-btc"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}