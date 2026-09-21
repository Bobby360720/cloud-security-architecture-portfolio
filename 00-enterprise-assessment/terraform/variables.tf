variable "management_groups" {
  description = "Current-state enterprise management group hierarchy."

  type = map(object({
    display_name = string
    parent       = optional(string)
  }))

  default = {
    platform = {
      display_name = "Platform"
    }

    connectivity = {
      display_name = "Connectivity"
      parent       = "platform"
    }

    management = {
      display_name = "Management"
      parent       = "platform"
    }

    security = {
      display_name = "Security"
      parent       = "platform"
    }

    landing_zones = {
      display_name = "Landing-Zones"
    }

    production = {
      display_name = "Production"
      parent       = "landing_zones"
    }

    non_production = {
      display_name = "Non-Production"
      parent       = "landing_zones"
    }

    sandbox = {
      display_name = "Sandbox"
      parent       = "landing_zones"
    }

    legacy = {
      display_name = "Legacy"
      parent       = "landing_zones"
    }
  }
}