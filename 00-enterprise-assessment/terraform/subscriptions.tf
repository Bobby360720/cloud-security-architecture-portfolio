# -----------------------------------------------------------------------------
# Current-State Subscription Placement
# -----------------------------------------------------------------------------
#
# Physical subscriptions used by the architecture lab are associated with
# their corresponding platform management groups.
#
# The broader enterprise architecture contains additional logical
# subscriptions that are documented separately and may not be physically
# instantiated in the lab environment.
# -----------------------------------------------------------------------------

variable "connectivity_subscription_id" {
  description = "Subscription ID for the Connectivity platform subscription."
  type        = string
}

variable "management_subscription_id" {
  description = "Subscription ID for the Management platform subscription."
  type        = string
}

variable "security_subscription_id" {
  description = "Subscription ID for the Security platform subscription."
  type        = string
}

resource "azurerm_management_group_subscription_association" "connectivity" {
  management_group_id = azurerm_management_group.connectivity.id
  subscription_id     = var.connectivity_subscription_id
}

resource "azurerm_management_group_subscription_association" "management" {
  management_group_id = azurerm_management_group.management.id
  subscription_id     = var.management_subscription_id
}

resource "azurerm_management_group_subscription_association" "security" {
  management_group_id = azurerm_management_group.security.id
  subscription_id     = var.security_subscription_id
}