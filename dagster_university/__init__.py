# fmt: off
# dagster_university/__init__.py
from dagster import Definitions, load_assets_from_modules
from .resources import database_resource
from .assets import metrics, trips

trip_assets = load_assets_from_modules([trips])
metric_assets = load_assets_from_modules([metrics])

defs = Definitions(
    assets=[*trip_assets, *metric_assets],
    resources={
        "database": database_resource,
    },
)
