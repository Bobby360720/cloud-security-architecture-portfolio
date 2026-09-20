variable "location" {
  description = "Azure region used for Terraform bootstrap resources."
  type        = string
  default     = "centralus"
}

variable "resource_group_name" {
  description = "Resource group containing Terraform state infrastructure."
  type        = string
  default     = "rg-tfstate-01"
}

variable "storage_account_prefix" {
  description = "Prefix used for the Terraform state storage account."
  type        = string
  default     = "sttfstate"
}