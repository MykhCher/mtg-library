from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel
# =====
from index import commander_list, card_color
from cardlist import cards

app = FastAPI()

class Card(BaseModel):
    name: str
    type: str
    manacost: Dict[str, int]
    power: int | None = None
    toughness: int | None = None
    loyalty: int | None = None

@app.get("/commanders")
def commanders():
    return {"commanders": commander_list(cards)}

@app.get("/colors")
def colors():
    return {card.get("name", "Unknown"): card_color(card) for card in cards}

@app.post("/add-card")
def create_card(new_card: Card):
    card_dict = new_card.model_dump()
    cards.append(card_dict)
    return {"message": f"Successfully added {new_card.name}!"}