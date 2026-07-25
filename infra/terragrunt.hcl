# Root Terragrunt config for bifrost-api project-level infra.
# Reuses nexus-infra's shared S3 state bucket and DynamoDB lock table.
# State keys are namespaced under bifrost-api/ to avoid collisions.

locals {
  path_parts = split("/", path_relative_to_include())
  env        = local.path_parts[0]

  part1      = try(local.path_parts[1], "")
  aws_region = length(regexall("^[a-z]+-[a-z]+-[0-9]+$", local.part1)) > 0 ? local.part1 : "ap-south-1"

  # Path to the nexus-infra repo.
  # CI sets NEXUS_INFRA_PATH to the checkout location.
  # Locally falls back to the sibling-directory convention (../nexus-infra).
  nexus_infra_path = get_env("NEXUS_INFRA_PATH", "${get_repo_root()}/../nexus-infra")
}

remote_state {
  backend = "s3"
  config = {
    bucket         = "nexus-tofu-state-${local.env}"
    key            = "bifrost-api/${path_relative_to_include()}/tofu.tfstate"
    region         = "ap-south-1"
    encrypt        = true
    dynamodb_table = "nexus-tofu-locks"
  }
  generate = {
    path      = "backend.tf"
    if_exists = "overwrite_terragrunt"
  }
}

generate "provider" {
  path      = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents  = <<-EOT
    terraform {
      required_version = ">= 1.6.0"
      required_providers {
        aws = {
          source  = "hashicorp/aws"
          version = "~> 5.0"
        }
      }
    }

    provider "aws" {
      region = "${local.aws_region}"

      default_tags {
        tags = {
          ManagedBy  = "opentofu"
          Env        = "${local.env}"
          Project    = "nexus"
          Service    = "bifrost-api"
          Repository = "bifrost-api"
        }
      }
    }
  EOT
}
