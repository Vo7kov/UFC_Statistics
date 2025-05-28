from fastapi import APIRouter, Query
from services.data_loader import load_data
from services.fight_time_distribution import get_fight_time_distribution
from services.confidence_interval import get_confidence_interval
from services.clt_distribution import get_clt_distribution
from fastapi.responses import JSONResponse, StreamingResponse
import io
import matplotlib.pyplot as plt

router = APIRouter()

df = load_data()

@router.get("/distribution/fight-time")
async def distribution_fight_time():
  _, fig = get_fight_time_distribution(df)
  buf = io.BytesIO()
  fig.savefig(buf, format="png")
  buf.seek(0)
  plt.close(fig)
  return StreamingResponse(buf, media_type="image/png")

@router.get("/confidence-interval/fight-time")
async def confidence_interval_fight_time():
  result = get_confidence_interval(df)
  return JSONResponse(content=result)

@router.get("/clt/fight-time")
async def clt_fight_time():
  _, fig = get_clt_distribution(df)
  buf = io.BytesIO()
  fig.savefig(buf, format="png")
  buf.seek(0)
  plt.close(fig)
  return StreamingResponse(buf, media_type="image/png")