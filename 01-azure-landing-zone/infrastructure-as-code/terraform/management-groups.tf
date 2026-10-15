# -----------------------------------------------------------------------------
# AFG Enterprise Root
# -----------------------------------------------------------------------------

resource "azurerm_management_group" "afg" {
  name         = "afg"
  display_name = "AFG"
}

# -----------------------------------------------------------------------------
# Platform
# -----------------------------------------------------------------------------

resource "azurerm_management_group" "platform" {
  name                       = "platform"
  display_name               = "Platform"
  parent_management_group_id = azurerm_management_group.afg.id
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
  name                       = "landing-zones"
  display_name               = "Landing-Zones"
  parent_management_group_id = azurerm_management_group.afg.id
}

resource "azurerm_management_group" "corp" {
  name                       = "corp"
  display_name               = "Corp"
  parent_management_group_id = azurerm_management_group.landing_zones.id
}

resource "azurerm_management_group" "online" {
  name                       = "online"
  display_name               = "Online"
  parent_management_group_id = azurerm_management_group.landing_zones.id
}

resource "azurerm_management_group" "legacy" {
  name                       = "legacy"
  display_name               = "Legacy"
  parent_management_group_id = azurerm_management_group.landing_zones.id
}


# -----------------------------------------------------------------------------
# Lifecycle Boundaries
# -----------------------------------------------------------------------------

resource "azurerm_management_group" "sandbox" {
  name                       = "Sandbox"
  display_name               = "Sandbox"
  parent_management_group_id = azurerm_management_group.afg.id
}

resource "azurerm_management_group" "onboarding" {
  name                       = "onboarding"
  display_name               = "Onboarding"
  parent_management_group_id = azurerm_management_group.afg.id
}

resource "azurerm_management_group" "decommissioned" {
  name                       = "decommissioned"
  display_name               = "Decommissioned"
  parent_management_group_id = azurerm_management_group.afg.id
}