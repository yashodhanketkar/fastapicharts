from fastapi import APIRouter

from ..controller.customer import (get_all_customers, get_filtered_customers,
                                   get_particular_customer)

router = APIRouter()


@router.get("/")
async def get_all_customers_route():
    customers = await get_all_customers()
    if customers:
        return {"result": customers}
    return {"result": "No customers found"}, 404


@router.get("/new_npa_accounts")
async def get_new_npa_customers_route():
    customers = await get_filtered_customers(
        filter="chart_type", value="New NPA Accounts"
    )
    if customers:
        return {"result": customers}
    return {"result": "No customers found"}, 404


@router.get("/npa_accounts_with_recovery")
async def get_npa_accounts_with_recovery_customers():
    customers = await get_filtered_customers(
        filter="chart_type", value="NPA Accounts with recovery"
    )
    if customers:
        return {"result": customers}
    return {"result": "No customers found"}, 404


@router.get("/new_sma_accounts")
async def get_new_sma_customers_route():
    customers = await get_filtered_customers(
        filter="chart_type", value="New SMA Accounts"
    )
    if customers:
        return {"result": customers}
    return {"result": "No customers found"}, 404


@router.get("/{id}")
async def get_particular_customer_route(id: str):
    customer = await get_particular_customer(id)
    if customer:
        return {"result": customer}
    return {"result": "Customer not found"}, 404
