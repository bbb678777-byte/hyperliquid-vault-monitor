# collector/hyperliquid.py
import requests


HYPERLIQUID_API_BASE = "https://api.hyperliquid.xyz"


def fetch_vault_state(vault_address: str) -> dict:
    """
    获取 Vault 当前状态（TVL / equity 等）
    """
    url = f"{HYPERLIQUID_API_BASE}/info"
    payload = {
        "type": "vaultState",
        "vaultAddress": vault_address
    }

    resp = requests.post(url, json=payload, timeout=10)
    resp.raise_for_status()

    return resp.json()