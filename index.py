from cardlist import cards

def commander_list(cardlist: list):
  return [
    card.get("name")
    for card in cardlist
    if "Legendary" in card.get("type", "") and "Creature" in card.get("type", "")
  ]

def total_manacosts(cardlist: list):
  return {
    card.get("name"): sum(
      card.get("manacost", {}).values()
    ) 
    for card in cardlist
  }

def is_permanent(card: dict):
  return "Sorcery" not in card.get("type", "") and "Instant" not in card.get("type", "")

def card_color(card: dict):
  manacost = card.get("manacost", {})
  colors = []
  for mana, amount in manacost.items():
    if amount and mana != "colorless":
      colors.append(mana)
  return colors


if __name__ == "__main__":
  print({card.get("name", ""): card_color(card) for card in cards})