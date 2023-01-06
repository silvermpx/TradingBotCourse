import requests


def get_contracts_bitmex():

    response_object = requests.get("https://testnet.bitmex.com/api/v1/instrument/active")
    print(response_object.status_code)
    contracts = []

    for contract in response_object.json():
        contracts.append(contract['symbol'])
    return contracts

print(get_contracts_bitmex())