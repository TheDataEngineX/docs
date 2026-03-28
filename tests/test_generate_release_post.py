"""Tests for generate_release_post.py."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))


def test_repo_display_name() -> None:
    from generate_release_post import repo_display_name

    assert repo_display_name("TheDataEngineX/DEX") == "DataEngineX"
    assert repo_display_name("TheDataEngineX/dex-studio") == "DEX Studio"
    assert repo_display_name("TheDataEngineX/infradex") == "Infradex"


def test_render_post() -> None:
    from generate_release_post import render_post

    result = render_post(
        repo="TheDataEngineX/DEX",
        tag="v1.0.0",
        changelog_body="### Features\n- Added new feature",
        release_date="2026-03-28",
    )
    assert "DataEngineX 1.0.0 Released" in result
    assert "### Features" in result
    assert "2026-03-28" in result
    assert "Release" in result


def test_output_filename() -> None:
    from generate_release_post import output_filename

    assert output_filename("TheDataEngineX/DEX", "v1.0.0") == "dex-v1.0.0.md"
    assert (
        output_filename("TheDataEngineX/dex-studio", "v0.2.0")
        == "dex-studio-v0.2.0.md"
    )
