from typing import List

from .customer import get_all_customers, get_filtered_customers


def date_range(date, range):
    if range == "monthly":
        date = f"{date}"[0:7]  # gets month and year
    else:
        date = f"{date}"[0:4]  # gets month and year
    return date


async def get_gross_npa():
    total = 0
    customers: List[dict] = await get_filtered_customers(
        filter="chart_type", value="New NPA Accounts"
    ) + await get_filtered_customers(
        filter="chart_type", value="NPA Accounts with recovery"
    )

    for customer in customers:
        total += int(customer.get("amount_outstanding", 0))
    return total


async def get_gross_sma():
    total = 0
    customers: List[dict] = await get_filtered_customers(
        filter="chart_type", value="New SMA Accounts"
    )

    for customer in customers:
        total += int(customer.get("amount_outstanding", 0))
    return total


async def get_gross_recoveries():
    total = 0
    customers: List[dict] = await get_all_customers()

    for customer in customers:
        total += int(customer.get("recovery", 0))
    return total


async def get_ranged_npa(range: str):
    month_record = {}
    customers: List[dict] = await get_filtered_customers(
        filter="chart_type", value="New NPA Accounts"
    ) + await get_filtered_customers(
        filter="chart_type", value="NPA Accounts with recovery"
    )
    for customer in customers:
        date = customer.get("record_date", 0)
        if date == 0:
            continue
        date = date_range(date, range)
        month_record[date] = customer.get("amount_outstanding", 0) + month_record.get(
            date, 0
        )

    return month_record


async def get_ranged_sma(range: str):
    month_record = {}
    customers: List[dict] = await get_filtered_customers(
        filter="chart_type", value="New SMA Accounts"
    )
    for customer in customers:
        date = customer.get("record_date", 0)
        if date == 0:
            continue
        date = date_range(date, range)
        month_record[date] = customer.get("amount_outstanding", 0) + month_record.get(
            date, 0
        )

    return month_record


async def get_ranged_recoveries(range: str):
    month_record = {}
    customers: List[dict] = await get_all_customers()
    for customer in customers:
        date = customer.get("record_date", 0)
        if date == 0:
            continue
        date = date_range(date, range)
        month_record[date] = customer.get("recovery", 0) + month_record.get(date, 0)

    return month_record
