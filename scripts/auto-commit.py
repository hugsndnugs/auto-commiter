#!/usr/bin/env python3
"""
Auto-commit script that updates a file and commits the changes.
"""

import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Configuration
TARGET_FILE = "last-update.txt"
COMMIT_MESSAGE_PREFIX = "chore: auto-update"

def update_file(file_path: Path) -> str:
    """
    Update the target file with current timestamp.
    Returns the content that was written.
    """
    timestamp = datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + " UTC"
    content = f"Last updated: {timestamp}\n"
    
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content)
    
    return content.strip()

def main():
    """Main function to update file and commit changes."""
    repo_root = Path(__file__).parent.parent
    target_file = repo_root / TARGET_FILE
    os.chdir(repo_root)
    
    # Update the file
    content = update_file(target_file)
    print(f"Updated {TARGET_FILE}: {content}")
    
    # Stage the file
    os.system(f'git add {TARGET_FILE}')
    
    # Check if there are changes to commit
    result = os.system('git diff --staged --quiet')
    if result == 0:
        print("No changes to commit.")
        return 0
    
    # Create commit
    commit_message = f"{COMMIT_MESSAGE_PREFIX} {TARGET_FILE}"
    result = os.system(f'git commit -m "{commit_message}"')
    
    if result != 0:
        print("Error: Failed to create commit.", file=sys.stderr)
        return 1
    
    print(f"Successfully committed: {commit_message}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
