# -----------------------------------------------------------------------------
# Management Group Outputs
# -----------------------------------------------------------------------------

output "platform_management_group_id" {
  description = "Resource ID of the Platform management group."
  value       = azurerm_management_group.platform.id
}

output "landing_zones_management_group_id" {
  description = "Resource ID of the Landing-Zones management group."
  value       = azurerm_management_group.landing_zones.id
}

output "management_group_ids" {
  description = "Resource IDs for the current-state management group hierarchy."

  value = {
    platform       = azurerm_management_group.platform.id
    connectivity   = azurerm_management_group.connectivity.id
    management     = azurerm_management_group.management.id
    security       = azurerm_management_group.security.id
    landing_zones  = azurerm_management_group.landing_zones.id
    production     = azurerm_management_group.production.id
    non_production = azurerm_management_group.non_production.id
    sandbox        = azurerm_management_group.sandbox.id
    legacy         = azurerm_management_group.legacy.id
  }
}