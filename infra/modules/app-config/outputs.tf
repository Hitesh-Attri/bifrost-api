output "ssm_prefix" {
  description = "SSM path prefix for all bifrost-api parameters"
  value       = "/nexus/${var.environment}/${var.service}"
}

output "parameter_names" {
  description = "Map of parameter key to full SSM path"
  value       = { for k, v in aws_ssm_parameter.this : k => v.name }
}

output "parameter_arns" {
  description = "Map of parameter key to ARN (for IAM policies)"
  value       = { for k, v in aws_ssm_parameter.this : k => v.arn }
}
