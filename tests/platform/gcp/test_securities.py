from typing import Any

import msgspec
import pytest
import respx

from lueur.platform.gcp.securities import explore_securities


@respx.mock
@pytest.mark.asyncio
async def test_explore_global_securities(
    gcp_project: str,
    gcp_global_securities: list[dict[str, Any]]
) -> None:
    respx.post(
        "https://oauth2.googleapis.com/token",
    ).respond(
        content=msgspec.json.encode({
            "access_token": "xyz"
        })
    )
    
    respx.get(
        f"https://compute.googleapis.com/compute/v1/projects/{gcp_project}/global/securityPolicies",
    ).respond(
        content=msgspec.json.encode({
            "items": gcp_global_securities
        })
    )
    
    resources = await explore_securities(gcp_project)
    assert len(resources) == 1


@respx.mock
@pytest.mark.asyncio
async def test_explore_regional_securities(
    gcp_project: str,
    gcp_region: str,
) -> None:
    respx.post(
        "https://oauth2.googleapis.com/token",
    ).respond(
        content=msgspec.json.encode({
            "access_token": "xyz"
        })
    )
    
    respx.get(
        f"https://compute.googleapis.com/compute/v1/projects/{gcp_project}/regions/{gcp_region}/securityPolicies",
    ).respond(
        content=msgspec.json.encode({
            "items": []
        })
    )
    
    resources = await explore_securities(gcp_project, gcp_region)
    assert len(resources) == 0
