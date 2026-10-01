variable "subscription_id" {
  type        = string
  description = "Existing lab subscription; this configuration never creates subscriptions or management groups."
}

variable "location" {
  type    = string
  default = "centralus"
}

variable "prefix" {
  type    = string
  default = "afg-bf"
}

variable "owner" {
  type    = string
  default = "Portfolio"
}

variable "ssh_public_key" {
  type        = string
  description = "Contents of your SSH public key (never a private key)."
  default     = ""
}

variable "deploy_vm" {
  type        = bool
  default     = false
  description = "Cost switch: deploy VM only for active exercises."
}

variable "vm_size" {
  type    = string
  default = "Standard_B1s"
}

variable "deploy_function" {
  type    = bool
  default = true
}

variable "deploy_monitoring" {
  type        = bool
  default     = false
  description = "Cost switch: workspace only; no data ingestion configured."
}

variable "deploy_policy" {
  type        = bool
  default     = false
  description = "Audit missing Owner tag in lab RG; never assigns a tenant-wide policy."
}

variable "deploy_public_ip" {
  type        = bool
  default     = false
  description = "Optional VM public IP; avoid unless essential; restrict SSH source."
}

variable "allowed_ssh_cidr" {
  type        = string
  default     = "127.0.0.1/32"
  description = "Set to your public IP /32 if enabling VM public IP."
}

variable "tags" {
  type    = map(string)
  default = {}
}

