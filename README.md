<div align="center">

# ðŸ’° Cloud FinOps Sentinel
### Event-Driven Cloud Financial Management & Automated Waste Elimination Platform

[![Terraform](https://img.shields.io/badge/Terraform-%3E%3D1.5.0-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)](https://terraform.io)
[![Azure](https://img.shields.io/badge/Azure-FinOps%20Engine-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Infracost](https://img.shields.io/badge/Infracost-Automated%20PR%20Cost%20Guard-00D2FF?style=for-the-badge&logo=curseforge&logoColor=white)](https://infracost.io)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge)](LICENSE)

<br/>

> **Cloud FinOps Sentinel** is an automated, event-driven governance engine engineered to eliminate cloud waste, enforce proactive budget guardrails, rightsize compute workloads, and optimize annual cloud OPEX by up to 35%.

</div>

---

## âš¡ Core FinOps Capabilities
- **Automated Zombie Resource Purging**: Serverless Azure Functions running daily cron jobs detecting orphaned managed disks, unassociated Public IPs, idle Application Gateways, and stale snapshots.
- **Dynamic Rightsizing Engine**: Continuously evaluates Azure Monitor CPU/Memory percentiles (P95 < 20%) and generates non-disruptive VM rightsizing recommendations.
- **Budget Guardrails & Action Groups**: Multi-tier threshold alerting (50%, 80%, 100%, 120%) with automated rate-limiting webhooks.
- **Infracost Shift-Left CI/CD**: Blocks pull requests introducing unanticipated monthly infrastructure spending before deployment.

---

## ðŸ—ï¸ Architecture Flow

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”       â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”       â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Azure Schedule  â”‚ â”€â”€â”€>  â”‚ FinOps Azure Functionâ”‚ â”€â”€â”€>  â”‚ Waste Elimination    â”‚
â”‚ (Daily Cron)    â”‚       â”‚ (Resource Graph API) â”‚       â”‚ Runbooks (Purge/Off) â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                    â”‚
                                    v
                          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                          â”‚ Slack / Teams SRE    â”‚
                          â”‚ Weekly OPEX Digest   â”‚
                          â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## ðŸš€ Quickstart Deployment

```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform plan
terraform apply
```

<sub>Engineered by **Kusum Vishwakarma** â€¢ Principal Enterprise Cloud Architect</sub>