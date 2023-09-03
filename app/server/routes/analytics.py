from fastapi import APIRouter

from ..controller.analytics import (get_gross_npa, get_gross_recoveries,
                                    get_gross_sma, get_ranged_npa,
                                    get_ranged_recoveries, get_ranged_sma)

router = APIRouter()


@router.get("/gross_npa")
async def get_gross_npa_route():
    return {"total": await get_gross_npa()}


@router.get("/gross_sma")
async def get_gross_sma_router():
    return {"total": await get_gross_sma()}


@router.get("/recoveries")
async def get_gross_recoveries_route():
    return {"total": await get_gross_recoveries()}


@router.get("/npa_record")
async def get_per_month_npa_route(range: str = "monthly"):
    if range in ["monthly", "yearly"]:
        return {"total": await get_ranged_npa(range)}
    return {"error": "Incorrect range"}, 400


@router.get("/sma_record")
async def get_per_month_sma_route(range: str = "monthly"):
    if range in ["monthly", "yearly"]:
        return {"total": await get_ranged_sma(range)}


@router.get("/recoveries_record")
async def get_per_month_recoveries_route(range: str = "monthly"):
    if range in ["monthly", "yearly"]:
        return {"total": await get_ranged_recoveries(range)}
