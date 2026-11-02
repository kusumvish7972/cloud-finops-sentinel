import os
import logging
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FinOpsSentinel")

def scan_and_purge_orphaned_disks(subscription_id: str):
    """Identifies unattached managed disks consuming idle OPEX."""
    credential = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credential, subscription_id)
    
    logger.info("Scanning for unattached disks across subscription %s...", subscription_id)
    orphaned_disks = []
    for disk in compute_client.disks.list():
        if disk.managed_by is None:
            orphaned_disks.append({
                "name": disk.name,
                "size_gb": disk.disk_size_gb,
                "tier": disk.sku.name
            })
            logger.warning("Found unattached disk: %s (%d GB, %s)", disk.name, disk.disk_size_gb, disk.sku.name)
            
    logger.info("Scan complete. Total unattached disks detected: %d", len(orphaned_disks))
    return orphaned_disks

if __name__ == "__main__":
    sub_id = os.getenv("AZURE_SUBSCRIPTION_ID", "00000000-0000-0000-0000-000000000000")
    scan_and_purge_orphaned_disks(sub_id)