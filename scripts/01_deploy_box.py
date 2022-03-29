from scripts.helpful_scripts import get_account, encode_function_data
from brownie import network, Box, ProxyAdmin, TransparentUpgradeableProxy, Contract


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    box = Box.deploy({"from": account})
    # print(box.reterive())

    proxy_admin = ProxyAdmin.deploy({"from": account})
    #! initializer = box.store, 1
    box_encorded_initializer_function = encode_function_data()

    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encorded_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )
    print(f"Proxy deployed to {proxy}. now you can upgarade to V2.")
    proxy_box = Contract.from_abi("box", proxy.address, Box.abi)
    proxy_box.store(1, {"from": account})
    print(proxy_box.reterive())
