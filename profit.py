crop_prices = {
    "rice": 20000,
    "maize": 18000,
    "wheat": 22000,
    "cotton": 30000
}

crop_yield = {
    "rice": 2.5,
    "maize": 2.0,
    "wheat": 2.2,
    "cotton": 1.8
}

def calculate_profit(crop):
    return (crop_prices.get(crop,15000) * crop_yield.get(crop,2)) - 15000