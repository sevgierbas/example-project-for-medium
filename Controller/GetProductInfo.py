from fastapi import requests

from Data.UrlData import FAKE_API_URL
import requests


def get_product_information(quantity, taxes, categories_type):
    get_response = requests.get(FAKE_API_URL + '/products?_quantity={_quantity}&_taxes={_taxes}&_categories_type={_categories_type}'.format(
                                            _quantity=quantity,
                                            _taxes=taxes,
                                            _categories_type=categories_type))
    response = get_response.json()
    id = response["data"][0]["id"]
    name = response["data"][0]["name"]
    description = response["data"][0]["description"]

    return id, name, description
