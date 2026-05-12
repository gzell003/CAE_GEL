from pathlib import Path

APP_TITLE = "Modo Plan SD"

BASE_TMP_PATH = Path("/tmp")
DATABASE_NAME = "modo_plan_sd.db"
DATABASE_PATH = BASE_TMP_PATH / DATABASE_NAME

MAX_RESULTS = 3

MOOD_OPTIONS = [
    "Relajada",
    "Social",
    "Creativa",
    "Curiosa",
    "Energética",
    "Aventurera",
]

BUDGET_OPTIONS = {
    "RD$500": 500,
    "RD$1,000": 1000,
    "RD$1,500": 1500,
    "Sin límite": 999999,
}

EMPTY_RESULTS_MESSAGE = (
    "No encontramos planes que encajen con tu mood y presupuesto hoy."
)

SUCCESS_SAVE_MESSAGE = (
    "Tu plan quedó guardado para revisarlo después."
)

SEARCHING_MESSAGE = (
    "Buscando planes que valgan la salida esta noche..."
)

EVENT_TAG_PRIORITY = {
    "nuevo": 3,
    "popular": 2,
    "oculto": 1,
}
