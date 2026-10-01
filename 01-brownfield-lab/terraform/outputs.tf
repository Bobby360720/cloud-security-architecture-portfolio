output "resource_group" { value = azurerm_resource_group.lab.name }
output "vm_private_ip" { value = var.deploy_vm ? azurerm_network_interface.vm[0].private_ip_address : null }
output "vm_public_ip" { value = var.deploy_vm && var.deploy_public_ip ? azurerm_public_ip.vm[0].ip_address : null }
output "function_name" { value = var.deploy_function ? azurerm_linux_function_app.function[0].name : null }
output "storage_name" { value = azurerm_storage_account.lab.name }
output "key_vault_name" { value = azurerm_key_vault.lab.name }
output "workspace_id" { value = var.deploy_monitoring ? azurerm_log_analytics_workspace.lab[0].id : null }
