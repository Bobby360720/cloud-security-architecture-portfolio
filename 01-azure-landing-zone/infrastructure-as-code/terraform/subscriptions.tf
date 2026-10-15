# -----------------------------------------------------------------------------
# Phase 1 Subscription Placement
# -----------------------------------------------------------------------------
#
# Physical subscriptions used by the representative AFG lab are associated
# with their approved target management-group boundaries.
#
# Existing brownfield subscriptions are placed according to their validated
# use case, lifecycle, and transition requirements.
#
# Additional enterprise subscriptions remain modeled and are documented
# separately unless physically instantiated in the lab.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Core Platform Subscription Placement
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Sandbox Subscription Placement
# -----------------------------------------------------------------------------

resource "azurerm_management_group_subscription_association" "sandbox" {
  management_group_id = azurerm_management_group.sandbox.id
  subscription_id     = var.sandbox_subscription_id
}

resource "azurerm_management_group_subscription_association" "brownfield_sandbox" {
  management_group_id = azurerm_management_group.sandbox.id
  subscription_id     = var.brownfield_sandbox_subscription_id
}

# -----------------------------------------------------------------------------
# Brownfield / Transitional Subscription Placement
# -----------------------------------------------------------------------------

resource "azurerm_management_group_subscription_association" "brownfield_connectivity" {
  management_group_id = azurerm_management_group.legacy.id
  subscription_id     = var.brownfield_connectivity_subscription_id
}

resource "azurerm_management_group_subscription_association" "legacy_identity" {
  management_group_id = azurerm_management_group.decommissioned.id
  subscription_id     = var.legacy_identity_subscription_id
}

resource "azurerm_management_group_subscription_association" "legacy_security" {
  management_group_id = azurerm_management_group.decommissioned.id
  subscription_id     = var.legacy_security_subscription_id
}

resource "azurerm_management_group_subscription_association" "web_apps" {
  management_group_id = azurerm_management_group.online.id
  subscription_id     = var.web_apps_subscription_id
}