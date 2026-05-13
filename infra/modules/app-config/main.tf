locals {
  prefix = "/nexus/${var.environment}/${var.service}"
}

resource "aws_ssm_parameter" "this" {
  for_each = var.parameters

  name  = "${local.prefix}/${each.key}"
  type  = each.value.secure ? "SecureString" : "String"
  value = each.value.value

  lifecycle {
    ignore_changes = [value]  # prevent Terraform from overwriting manual secret rotations
  }
}
