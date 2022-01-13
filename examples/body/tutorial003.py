from typing import Optional

import citus

app = citus.App()


class Item(citus.Base):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None



@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
