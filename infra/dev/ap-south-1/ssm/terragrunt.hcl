locals {
  env_vars = read_terragrunt_config(find_in_parent_folders("env.hcl"))
  env      = local.env_vars.locals.environment
}

include "root" {
  path = find_in_parent_folders()
}

include "envcommon" {
  path = "${get_repo_root()}/infra/_envcommon/app-config.hcl"
}

inputs = {
  environment = local.env
  service     = "bifrost-api"

  # Non-sensitive env vars → stored as String
  # Sensitive values      → stored as SecureString (set secure = true)
  #
  # All params land at: /nexus/{env}/bifrost-api/{KEY}
  # The ECS task role in nexus-infra has read access to /nexus/{env}/bifrost-api/*
  parameters = {
    APP_ENV   = { value = local.env }
    LOG_LEVEL = { value = "info" }
    DEBUG     = { value = "false" }

    # Example secret (add real value manually in AWS console or via CLI after apply):
    # DATABASE_URL = { value = "placeholder", secure = true }
  }
}
