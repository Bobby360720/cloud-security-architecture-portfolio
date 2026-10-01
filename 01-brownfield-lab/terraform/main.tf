resource "random_string" "suffix" {
  length  = 6
  lower   = true
  upper   = false
  numeric = true
  special = false
}

locals {
  suffix = random_string.suffix.result
  tags = merge({
    Environment = "BrownfieldLab"
    Application = "AFG-Representative-Brownfield"
    Owner       = var.owner
    ManagedBy   = "Terraform"
    CostCenter  = "Portfolio"
    Expiry      = "Ephemeral"
  }, var.tags)
}

resource "azurerm_resource_group" "lab" {
  name     = "rg-${var.prefix}-${local.suffix}"
  location = var.location
  tags     = local.tags
}

resource "azurerm_virtual_network" "legacy" {
  name                = "vnet-${var.prefix}-legacy-${local.suffix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.lab.name
  address_space       = ["10.80.0.0/16"]
  tags                = local.tags
}

resource "azurerm_subnet" "vm" {
  name                 = "snet-legacy-vm"
  resource_group_name  = azurerm_resource_group.lab.name
  virtual_network_name = azurerm_virtual_network.legacy.name
  address_prefixes     = ["10.80.1.0/24"]
}

resource "azurerm_subnet" "app" {
  name                 = "snet-app-reserved"
  resource_group_name  = azurerm_resource_group.lab.name
  virtual_network_name = azurerm_virtual_network.legacy.name
  address_prefixes     = ["10.80.2.0/24"]
}

resource "azurerm_network_security_group" "legacy" {
  name                = "nsg-${var.prefix}-legacy-${local.suffix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.lab.name
  tags                = local.tags
}

resource "azurerm_network_security_rule" "ssh" {
  count                       = var.deploy_vm && var.deploy_public_ip ? 1 : 0
  name                        = "AllowSSHFromOperator"
  priority                    = 110
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "22"
  source_address_prefix       = var.allowed_ssh_cidr
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.lab.name
  network_security_group_name = azurerm_network_security_group.legacy.name
}

resource "azurerm_subnet_network_security_group_association" "vm" {
  subnet_id                 = azurerm_subnet.vm.id
  network_security_group_id = azurerm_network_security_group.legacy.id
}

resource "azurerm_route_table" "legacy" {
  name                = "rt-${var.prefix}-legacy-${local.suffix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.lab.name
  tags                = local.tags
}

resource "azurerm_subnet_route_table_association" "vm" {
  subnet_id      = azurerm_subnet.vm.id
  route_table_id = azurerm_route_table.legacy.id
}

resource "azurerm_public_ip" "vm" {
  count               = var.deploy_vm && var.deploy_public_ip ? 1 : 0
  name                = "pip-${var.prefix}-vm-${local.suffix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.lab.name
  allocation_method   = "Static"
  sku                 = "Standard"
  tags                = local.tags
}

resource "azurerm_network_interface" "vm" {
  count               = var.deploy_vm ? 1 : 0
  name                = "nic-${var.prefix}-vm-${local.suffix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.lab.name
  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.vm.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.deploy_public_ip ? azurerm_public_ip.vm[0].id : null
  }
  tags = local.tags
}

resource "azurerm_linux_virtual_machine" "legacy" {
  count                           = var.deploy_vm ? 1 : 0
  name                            = "vm-${var.prefix}-${local.suffix}"
  resource_group_name             = azurerm_resource_group.lab.name
  location                        = var.location
  size                            = var.vm_size
  admin_username                  = "labadmin"
  disable_password_authentication = true
  network_interface_ids           = [azurerm_network_interface.vm[0].id]
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
    disk_size_gb         = 30
  }
  admin_ssh_key {
    username   = "labadmin"
    public_key = var.ssh_public_key
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "ubuntu-24_04-lts"
    sku       = "server"
    version   = "latest"
  }
  tags = local.tags
}

resource "azurerm_storage_account" "lab" {
  name                            = "st${replace(var.prefix, "-", "")}${local.suffix}"
  resource_group_name             = azurerm_resource_group.lab.name
  location                        = var.location
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  min_tls_version                 = "TLS1_2"
  allow_nested_items_to_be_public = false
  tags                            = local.tags
}

resource "azurerm_key_vault" "lab" {
  name                       = "kv-${var.prefix}-${local.suffix}"
  location                   = var.location
  resource_group_name        = azurerm_resource_group.lab.name
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "standard"
  enable_rbac_authorization  = true
  purge_protection_enabled   = false
  soft_delete_retention_days = 7
  tags                       = local.tags
}

resource "azurerm_service_plan" "function" {
  count               = var.deploy_function ? 1 : 0
  name                = "asp-${var.prefix}-${local.suffix}"
  resource_group_name = azurerm_resource_group.lab.name
  location            = var.location
  os_type             = "Linux"
  sku_name            = "Y1"
  tags                = local.tags
}

resource "azurerm_linux_function_app" "function" {
  count                      = var.deploy_function ? 1 : 0
  name                       = "func-${var.prefix}-${local.suffix}"
  resource_group_name        = azurerm_resource_group.lab.name
  location                   = var.location
  service_plan_id            = azurerm_service_plan.function[0].id
  storage_account_name       = azurerm_storage_account.lab.name
  storage_account_access_key = azurerm_storage_account.lab.primary_access_key
  https_only                 = true
  identity { type = "SystemAssigned" }
  site_config {
    application_stack { python_version = "3.11" }
  }
  tags = local.tags
}

resource "azurerm_log_analytics_workspace" "lab" {
  count               = var.deploy_monitoring ? 1 : 0
  name                = "law-${var.prefix}-${local.suffix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.lab.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
  daily_quota_gb      = 0.1
  tags                = local.tags
}

resource "azurerm_resource_group_policy_assignment" "owner_audit" {
  count                = var.deploy_policy ? 1 : 0
  name                 = "audit-owner-tag"
  resource_group_id    = azurerm_resource_group.lab.id
  policy_definition_id = azurerm_policy_definition.owner_audit[0].id
  display_name         = "AFG lab: audit missing Owner tag"
  description          = "Representative governance gap; audit only."
}

resource "azurerm_policy_definition" "owner_audit" {
  count        = var.deploy_policy ? 1 : 0
  name         = "afg-audit-owner-${local.suffix}"
  policy_type  = "Custom"
  mode         = "Indexed"
  display_name = "AFG: audit resources missing Owner tag"
  policy_rule = jsonencode({
    if   = { field = "tags['Owner']", exists = "false" }
    then = { effect = "audit" }
  })
  metadata = jsonencode({ category = "Tags" })
}
