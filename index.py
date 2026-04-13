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

if __name__ == "__main__":
  print(commander_list(cards))
  print(total_manacosts(cards))