import os

import motor.motor_asyncio

MONGO_URL = os.environ["MONGO_URL"]
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client.sixtyfour
collection = database.customers


def customer_helper(customer: dict) -> dict:
    return {
        "id": str(customer["_id"]),
        "record_date": customer.get("record_date", "NAN"),
        "chart_type": customer.get("chart_type", "NAN"),
        "customer_id": customer.get("customer_id", 0),
        "customer_name": customer.get("customer_name", "NAN"),
        "days_overdue": customer.get("days_overdue", 0),
        "amount_outstanding": customer.get("amount_outstanding", 0),
        "recovery": customer.get("recovery", 0),
    }
