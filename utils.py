import json
import logging
from datetime import datetime
import os


logger = logging.getLogger(__name__)


def load_products(path="products.json"):

    try:
        with open(path, "r") as file:
            products = json.load(file)

        logger.info("Products loaded successfully")
        return products

    except FileNotFoundError:

        logger.error("products.json file not found")

        return {}


def save_receipt(cart, total_price, final_price):

    os.makedirs("receipts", exist_ok=True)

    filename = f"receipts/receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    receipt_data = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": cart,
        "total_before_discount": total_price,
        "final_price": round(final_price, 2)
    }

    with open(filename, "w") as file:
        json.dump(receipt_data, file, indent=4)

    logger.info("Receipt saved: %s", filename)
