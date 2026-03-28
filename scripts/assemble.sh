#!/usr/bin/env bash
# Sparse-clones docs/ and src/ from source repos into the unified docs structure.
# Requires GH_TOKEN env var for private repo access.
set -euo pipefail

REPOS=(
  "TheDataEngineX/DEX:docs/:docs/framework/"
  "TheDataEngineX/dex-studio:docs/:docs/studio/"
  "TheDataEngineX/infradex:docs/:docs/deploy/"
  "TheDataEngineX/DEX:src/:src/"
)

CLONE_DIR="/tmp/docs-assemble-$$"
trap 'rm -rf "$CLONE_DIR"' EXIT

for entry in "${REPOS[@]}"; do
  IFS=: read -r repo src_path dest_path <<< "$entry"
  slug="${repo//\//-}"
  echo "::group::Pulling $repo:$src_path -> $dest_path"

  if [[ -d "$CLONE_DIR/$slug" ]]; then
    # Already cloned this repo — just add sparse path
    cd "$CLONE_DIR/$slug"
    git sparse-checkout add "$src_path"
    cd - > /dev/null
  else
    git clone --depth 1 --filter=blob:none --sparse \
      "https://x-access-token:${GH_TOKEN}@github.com/$repo.git" \
      "$CLONE_DIR/$slug"
    cd "$CLONE_DIR/$slug"
    git sparse-checkout set "$src_path"
    cd - > /dev/null
  fi

  mkdir -p "$dest_path"
  cp -r "$CLONE_DIR/$slug/$src_path"* "$dest_path"
  echo "::endgroup::"
done

echo "Assembly complete."
