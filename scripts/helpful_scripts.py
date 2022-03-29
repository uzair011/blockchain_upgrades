from brownie import network, accounts, config
import eth_utils

LOCAL_BLOCKCHAIN_ENVS = ["development", "ganache-local", "mainnet-fork-dev"]


def get_account(id=None, index=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


# initializer=box.store.... , 1, 2... for args
def encode_function_data(initializer=None, *args):
    if len(args) == 0 or not initializer:
        return eth_utils.to_bytes(hexstr="0x")
    return initializer.encode_input(*args)
    """Encodes the function call so we can work with an initializer.
    Args:
        initializer ([brownie.network.contract.ContractTx], optional):
        The initializer function we want to call. Example: `box.store`.
        Defaults to None.
        args (Any, optional):
        The arguments to pass to the initializer function
    Returns:
        [bytes]: Return the encoded bytes.
    """
