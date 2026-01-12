# Auto GitHub Committer

An automated GitHub commit system that updates a file and commits changes on a schedule using GitHub Actions (free for public repositories).

## How It Works

This repository uses GitHub Actions to automatically:
1. Update `last-update.txt` with the current timestamp
2. Commit the changes
3. Push to the repository

The workflow runs every 6 hours (at 00:00, 06:00, 12:00, and 18:00 UTC).

## Setup

1. **Push this repository to GitHub** (must be a GitHub repository for Actions to work)
2. **Enable GitHub Actions** in your repository settings (Settings → Actions → General)
3. The workflow will run automatically on the schedule

## Manual Trigger

You can manually trigger the workflow:
- Go to the "Actions" tab in your GitHub repository
- Select "Auto Commit" workflow
- Click "Run workflow"

## Configuration

### Change the Schedule

Edit `.github/workflows/auto-commit.yml` and modify the cron expression:

```yaml
schedule:
  - cron: '0 */6 * * *'  # Change this to your desired schedule
```

Cron syntax: `minute hour day-of-month month day-of-week`

Examples:
- `0 */6 * * *` - Every 6 hours
- `0 0 * * *` - Daily at midnight UTC
- `0 */3 * * *` - Every 3 hours
- `0 9,17 * * *` - At 9 AM and 5 PM UTC daily

### Change the Target File

Edit `scripts/auto-commit.py` and modify the `TARGET_FILE` variable:

```python
TARGET_FILE = "last-update.txt"  # Change to your desired file
```

### Customize Commit Messages

Edit `scripts/auto-commit.py` and modify the `COMMIT_MESSAGE_PREFIX` variable:

```python
COMMIT_MESSAGE_PREFIX = "chore: auto-update"
```

### Customize File Update Logic

Edit the `update_file()` function in `scripts/auto-commit.py` to change what gets written to the file. Currently it writes a timestamp, but you could:
- Write an incrementing counter
- Write random data
- Update multiple files
- Any other logic you need

## Requirements

- Python 3.x (provided by GitHub Actions)
- Git (provided by GitHub Actions)
- GitHub repository (public or private with Actions enabled)

## Free Tier Limits

- **Public repositories**: Unlimited GitHub Actions minutes
- **Private repositories**: 2,000 minutes/month free

## License

Free to use and modify as needed.
