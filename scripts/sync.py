import os

# Hardcoded paths for source and target directories
source = '/home/daniel/Git/daniel-goes-prompting/content'
target = '/home/daniel/Git/prompts-and-outputs/library'

def sync_files(source, target):
    # The rsync command with the --delete option for destructive syncing
    # and --exclude to ignore _index.md files
    os.system(f'rsync -av --delete --exclude "_index.md" {source}/ {target}/')

# Call the function to perform the sync
sync_files(source, target)