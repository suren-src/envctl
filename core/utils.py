from core.logger import logger

VALID_SYNC_TYPES = ["all", "config", "tools", "vim"]

def validate_sync_items(items: str) -> list:
    """Validate and parse sync items from comma-separated string"""
    item_list = [item.strip().lower() for item in items.split(",")]
    
    if "all" in item_list and len(item_list) > 1:
        logger.warning("'all' specified with other items - will sync everything")
        return ["all"]
        
    invalid_items = [item for item in item_list if item not in VALID_SYNC_TYPES]
    if invalid_items:
        raise ValueError(f"Invalid sync items: {', '.join(invalid_items)}. "
                        f"Valid options are: {', '.join(VALID_SYNC_TYPES)}")
    
    return item_list