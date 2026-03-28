#!/usr/bin/env bash
# Builds API reference pages via MkDocs Material + mkdocstrings,
# then merges the output into the main Zensical site directory.
set -euo pipefail

echo "Building API reference with MkDocs Material..."
mkdocs build -f mkdocs-api.yml

# mkdocs-api.yml has site_dir: build/api-reference
# MkDocs outputs the full site structure there, with api-reference/ nav pages
# under build/api-reference/api-reference/. Merge into the main Zensical output.
if [[ -d "build/api-reference" ]]; then
  mkdir -p site/api-reference
  # MkDocs generates pages at the root of its output matching the nav structure.
  # Copy all HTML files from the api-reference subdirectory.
  if [[ -d "build/api-reference/api-reference" ]]; then
    cp -r build/api-reference/api-reference/* site/api-reference/
  else
    # Fallback: copy everything except MkDocs chrome (assets, search, etc.)
    cp -r build/api-reference/*.html site/api-reference/ 2>/dev/null || true
  fi
  echo "API reference merged into site/api-reference/"
else
  echo "WARNING: build/api-reference/ not found — skipping merge"
fi
