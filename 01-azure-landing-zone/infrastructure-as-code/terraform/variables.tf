# -----------------------------------------------------------------------------
# Phase 1 Subscription Variables
# -----------------------------------------------------------------------------
#
# Subscription identifiers are supplied through the local terraform.tfvars
# file, which is excluded from source control.
#
# These variables support both validated platform subscriptions and existing
# brownfield subscriptions being transitioned into the Phase 1 target
# management-group hierarchy.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Core Platform Subscriptions
# -----------------------------------------------------------------------------

variable "connectivity_subscription_id" {
  description = "Subscription ID for the validated Connectivity platform subscription."
  type        = string
}

variable "management_subscription_id" {
  description = "Subscription ID for the validated Management platform subscription."
  type        = string
}

variable "security_subscription_id" {
  description = "Subscription ID for the validated Security platform subscription."
  type        = string
}

# -----------------------------------------------------------------------------
# Sandbox Subscriptions
# -----------------------------------------------------------------------------

variable "sandbox_subscription_id" {
  description = "Subscription ID for the validated Sandbox subscription."
  type        = string
}

variable "brownfield_sandbox_subscription_id" {
  description = "Subscription ID for the representative brownfield lab subscription placed beneath Sandbox."
  type        = string
}

# -----------------------------------------------------------------------------
# Brownfield / Transitional Subscriptions
# -----------------------------------------------------------------------------

variable "brownfield_connectivity_subscription_id" {
  description = "Subscription ID for the brownfield Connectivity subscription transitioning beneath the Legacy management group."
  type        = string
}

variable "legacy_identity_subscription_id" {
  description = "Subscription ID for the empty legacy Identity subscription transitioning beneath Decommissioned."
  type        = string
}

variable "legacy_security_subscription_id" {
  description = "Subscription ID for the empty legacy Security subscription transitioning beneath Decommissioned."
  type        = string
}

variable "web_apps_subscription_id" {
  description = "Subscription ID for the Web Apps subscription transitioning beneath the Online landing zone."
  type        = string
}