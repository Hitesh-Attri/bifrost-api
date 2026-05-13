variable "environment" {
  type = string
}

variable "service" {
  type    = string
  default = "bifrost-api"
}

variable "parameters" {
  type = map(object({
    value  = string
    secure = optional(bool, false)
  }))
  description = "Map of parameter name to value. Set secure=true for secrets (stored as SecureString)."
}
