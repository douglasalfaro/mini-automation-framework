from maf.core.config import CFG
from maf.api.client import ApiClient

def test_health_ok():
    client = ApiClient(CFG.api_base)
    assert client.health() == 200
