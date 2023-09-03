from bson import ObjectId

from ..database import collection, customer_helper


async def get_all_customers():
    customers = []
    async for customer in collection.find():
        customers.append(customer_helper(customer))
    return customers


async def get_particular_customer(id: str):
    customer = await collection.find_one({"_id": ObjectId(id)})
    if customer:
        return customer_helper(customer)


async def get_filtered_customers(filter: str, value: str):
    customers = await get_all_customers()
    filtered_customers = [
        customer for customer in customers if customer[filter] == value
    ]
    return filtered_customers
