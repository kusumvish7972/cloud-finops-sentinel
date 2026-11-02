terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.90"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "finops" {
  name     = var.resource_group_name
  location = var.location
  tags     = var.tags
}

module "cost_governance" {
  source              = "./modules/cost_governance"
  resource_group_name = azurerm_resource_group.finops.name
  location            = azurerm_resource_group.finops.location
  monthly_budget      = var.monthly_budget
  alert_emails        = var.alert_emails
  tags                = var.tags
}

module "waste_purger" {
  source              = "./modules/waste_purger"
  resource_group_name = azurerm_resource_group.finops.name
  location            = azurerm_resource_group.finops.location
  tags                = var.tags
}