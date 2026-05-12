#!/bin/bash
# git bisect run script: find the commit that introduced the ruby boxing SIGSEGV.
#
# Prerequisites:
#   1. crash_ruby.epub must be present at:
#      test/fixtures/vertical_text/crash_ruby.epub
#      (EPUB with <ruby>石<rt>いし</rt></ruby>, no "ruby { display: inline }" CSS)
#
# Usage (from crengine submodule root):
#   git bisect start
#   git bisect bad HEAD                 # current: crashes
#   git bisect good eabbbe2f            # last upstream commit: no crash
#   git bisect run \
#       base/tests/fixtures/vertical_text/bisect-ruby-crash.sh
#   git bisect reset
#
# Returns: 0 = good (no crash), 1 = bad (crash), 125 = skip (build fail).

set -e
KOREADER_ROOT="$(cd "$(dirname "$0")/../../../../.." && pwd)"
EPUB="$KOREADER_ROOT/test/fixtures/vertical_text/crash_ruby.epub"

if [ ! -f "$EPUB" ]; then
    echo "ERROR: $EPUB not found." >&2
    echo "Create it with: create-epub.py --no-workaround crash_ruby.epub" >&2
    exit 125
fi

# Rebuild koreader-cre for the current crengine commit.
echo "==> Building..."
if ! (cd "$KOREADER_ROOT" && nix develop --command ./kodev build -d emulator 2>&1 | tail -3); then
    echo "Build failed — skipping (exit 125)"
    exit 125
fi

# Run the bisect spec: passes if no crash, SIGSEGV kills process → exit 139.
echo "==> Testing..."
(cd "$KOREADER_ROOT" && \
 nix develop --command ./kodev test front -f "Ruby boxing bisect") 2>&1 | tail -3
STATUS=$?

if [ "$STATUS" -eq 0 ]; then
    echo "==> GOOD: ruby EPUB opened without crashing at $(git rev-parse --short HEAD)"
    exit 0
else
    echo "==> BAD: crashed (exit $STATUS) at $(git rev-parse --short HEAD)"
    exit 1
fi
