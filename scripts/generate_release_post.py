#!/usr/bin/env python3
"""Generate a blog post from a GitHub release.

Usage:
    python scripts/generate_release_post.py --repo TheDataEngineX/DEX --tag v1.0.0
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

REPO_DISPLAY_NAMES: dict[str, str] = {
    "TheDataEngineX/DEX": "DataEngineX",
    "TheDataEngineX/dex-studio": "DEX Studio",
    "TheDataEngineX/infradex": "Infradex",
}

TEMPLATE_DIR = Path(__file__).parent.parent / "templates"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "blog" / "posts" / "releases"


def repo_display_name(repo: str) -> str:
    """Map GitHub repo to human-readable display name."""
    return REPO_DISPLAY_NAMES.get(repo, repo.split("/")[-1])


def output_filename(repo: str, tag: str) -> str:
    """Generate the output filename for a release post."""
    slug = repo.split("/")[-1].lower()
    return f"{slug}-{tag}.md"


def fetch_release_notes(repo: str, tag: str) -> str:
    """Fetch release notes from GitHub using the gh CLI."""
    result = subprocess.run(
        ["gh", "release", "view", tag, "--repo", repo, "--json", "body", "-q", ".body"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def render_post(
    repo: str,
    tag: str,
    changelog_body: str,
    release_date: str | None = None,
) -> str:
    """Render a release blog post from the Jinja template."""
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)), autoescape=False)
    template = env.get_template("release-post.md.j2")

    if release_date is None:
        release_date = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

    release_url = f"https://github.com/{repo}/releases/tag/{tag}"
    version = tag.lstrip("v").lstrip("dataenginex-v")

    return template.render(
        release_date=release_date,
        repo_display_name=repo_display_name(repo),
        version=version,
        changelog_body=changelog_body,
        release_url=release_url,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate release blog post")
    parser.add_argument("--repo", required=True, help="GitHub repo (org/name)")
    parser.add_argument("--tag", required=True, help="Release tag")
    args = parser.parse_args()

    changelog_body = fetch_release_notes(args.repo, args.tag)
    post_content = render_post(args.repo, args.tag, changelog_body)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / output_filename(args.repo, args.tag)
    output_path.write_text(post_content)
    print(f"Generated: {output_path}")


if __name__ == "__main__":
    main()
