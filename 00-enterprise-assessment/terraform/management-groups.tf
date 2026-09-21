# -----------------------------------------------------------------------------
# Current-State Management Group Hierarchy
# -----------------------------------------------------------------------------
#
# This configuration reproduces the enterprise management group structure
# documented during the current-state assessment.
#
# Phase 0 intentionally models the current state before architectural
# improvements are introduced in later phases.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Platform
# -----------------------------------------------------------------------------

resource "azurerm_management_group" "platform" {
  name         = "platform"
  display_name = "Platform"
}

resource "azurerm_management_group" "connectivity" {
  name                       = "connectivity"
  display_name               = "Connectivity"
  parent_management_group_id = azurerm_management_group.platform.id
}

resource "azurerm_management_group" "management" {
  name                       = "management"
  display_name               = "Management"
  parent_management_group_id = azurerm_management_group.platform.id
}

resource "azurerm_management_group" "security" {
  name                       = "security"
  display_name               = "Security"
  parent_management_group_id = azurerm_management_group.platform.id
}


# -----------------------------------------------------------------------------
# Landing Zones
# -----------------------------------------------------------------------------

resource "azurerm_management_group" "landing_zones" {
  name         = "landing-zones"
  display_name = "Landing-Zones"
}

resource "azurerm_management_group" "production" {
  name                       = "Production"
  display_name               = "Production"
  parent_management_group_id = azurerm_management_group.landing_zones.id
}

resource "azurerm_management_group" "non_production" {
  name                       = "Non-Production"
  display_name               = "Non-Production"
  parent_management_group_id = azurerm_management_group.landing_zones.id
}

resource "azurerm_management_group" "sandbox" {
  name                       = "Sandbox"
  display_name               = "Sandbox"
  parent_management_group_id = azurerm_management_group.landing_zones.id
}

resource "azurerm_management_group" "legacy" {
  name                       = "legacy"
  display_name               = "Legacy"
  parent_management_group_id = azurerm_management_group.landing_zones.id
}