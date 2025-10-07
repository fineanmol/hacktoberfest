import os
import subprocess
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple
import git
from git import Repo, GitCommandError

class GitManager:
    """Handles all Git operations for the backup tool"""

    def __init__(self, folder_path: str, remote_url: str, logger: logging.Logger):
        self.folder_path = Path(folder_path).resolve()
        self.remote_url = remote_url
        self.logger = logger
        self.repo: Optional[Repo] = None

    def initialize_repository(self) -> Tuple[bool, str]:
        """Initialize or connect to existing Git repository"""
        try:
            if (self.folder_path / '.git').exists():
                # Repository already exists
                self.repo = Repo(self.folder_path)
                self.logger.info(f"Connected to existing repository at {self.folder_path}")
            else:
                # Initialize new repository
                self.repo = Repo.init(self.folder_path)
                self.logger.info(f"Initialized new repository at {self.folder_path}")

            # Configure remote
            self._setup_remote()

            return True, "Repository initialized successfully"

        except Exception as e:
            error_msg = f"Failed to initialize repository: {str(e)}"
            self.logger.error(error_msg)
            return False, error_msg

    def _setup_remote(self):
        """Setup or update remote origin"""
        try:
            if 'origin' in [remote.name for remote in self.repo.remotes]:
                origin = self.repo.remotes.origin
                if origin.url != self.remote_url:
                    origin.set_url(self.remote_url)
                    self.logger.info(f"Updated remote URL to {self.remote_url}")
            else:
                self.repo.create_remote('origin', self.remote_url)
                self.logger.info(f"Added remote origin: {self.remote_url}")

        except Exception as e:
            self.logger.warning(f"Remote setup warning: {str(e)}")

    def has_changes(self) -> bool:
        """Check if there are any changes to commit"""
        if not self.repo:
            return False

        try:
            # Check for untracked files
            untracked = self.repo.untracked_files

            # Check for modified files
            modified = [item.a_path for item in self.repo.index.diff(None)]

            # Check for staged changes
            staged = [item.a_path for item in self.repo.index.diff("HEAD")]

            has_changes = len(untracked) > 0 or len(modified) > 0 or len(staged) > 0

            if has_changes:
                self.logger.debug(f"Changes detected - Untracked: {len(untracked)}, "
                                f"Modified: {len(modified)}, Staged: {len(staged)}")

            return has_changes

        except Exception as e:
            self.logger.error(f"Error checking for changes: {str(e)}")
            return False

    def commit_changes(self) -> Tuple[bool, str]:
        """Stage all changes and create a commit"""
        if not self.repo:
            return False, "Repository not initialized"

        try:
            # Stage all changes (including untracked files)
            self.repo.git.add('.')

            # Create commit with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_message = f"Auto Backup: {timestamp}"

            commit = self.repo.index.commit(commit_message)

            self.logger.info(f"Created commit {commit.hexsha[:8]}: {commit_message}")
            return True, f"Commit created: {commit.hexsha[:8]}"

        except Exception as e:
            error_msg = f"Failed to commit changes: {str(e)}"
            self.logger.error(error_msg)
            return False, error_msg

    def push_changes(self) -> Tuple[bool, str]:
        """Push commits to remote repository"""
        if not self.repo:
            return False, "Repository not initialized"

        try:
            origin = self.repo.remotes.origin

            # Try to push
            push_info = origin.push()

            success_count = 0
            for info in push_info:
                if info.flags & info.ERROR:
                    error_msg = f"Push failed: {info.summary}"
                    self.logger.error(error_msg)
                    return False, error_msg
                else:
                    success_count += 1

            if success_count > 0:
                self.logger.info("Successfully pushed to remote repository")
                return True, "Push successful"
            else:
                return False, "No refs were pushed"

        except GitCommandError as e:
            error_msg = f"Git push failed: {str(e)}"
            self.logger.error(error_msg)
            return False, error_msg
        except Exception as e:
            error_msg = f"Push failed with error: {str(e)}"
            self.logger.error(error_msg)
            return False, error_msg

    def get_last_commit_info(self) -> Optional[str]:
        """Get information about the last commit"""
        if not self.repo:
            return None

        try:
            if self.repo.heads:
                last_commit = self.repo.head.commit
                return f"{last_commit.hexsha[:8]} - {last_commit.message.strip()}"
            return None
        except Exception as e:
            self.logger.error(f"Error getting last commit info: {str(e)}")
            return None

    def pull_changes(self) -> Tuple[bool, str]:
        """Pull changes from remote repository"""
        if not self.repo:
            return False, "Repository not initialized"

        try:
            origin = self.repo.remotes.origin
            pull_info = origin.pull()

            self.logger.info("Successfully pulled from remote repository")
            return True, "Pull successful"

        except Exception as e:
            error_msg = f"Pull failed: {str(e)}"
            self.logger.warning(error_msg)  # Warning since it's not always critical
            return False, error_msg
