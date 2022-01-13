from typing import Optional

import citus

app = citus.App()


class Item(citus.Base):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items/")
async def create_item(item: Item):
    return item
