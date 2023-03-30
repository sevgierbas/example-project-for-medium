import uvicorn
from fastapi import FastAPI, Depends
from Controller.GetProductInfo import get_product_information
from Models.Request.RequestModel import *

app = FastAPI()

@app.get("/ExampleMethodForMedium")
def getProducts(p: GetProducts = Depends()):
    id, name, description = get_product_information(p.quantity, p.taxes, p.categories_type)
    return {"id": id, "name": name, "description": description}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
