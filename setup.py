from pathlib import Path
import subprocess
import platform


class Setup:
    """Class to setup a coding enviornment."""

    def __init__(self):
        self.pwd = Path().absolute()
        self.on_unix = False if platform.system() == "Windows" else True

    def osvalue(self, unix, windows):
        """Return a value based on os."""
        return unix if self.on_unix else windows

    def mkdir(self, *folders):
        """Create folders in the root directory."""
        for folder in folders:
            if not Path(folder).exists():
                Path(folder).mkdir()

    def configure_git(self, level: str = "local", additional: dict = {}):
        """Sets up the git configurations."""
        configs = {
            "user.name": "Anonymous",
            "user.email": "anonymous@example.com",
            "core.editor": "code --wait",
            "core.autocrlf": self.osvalue("input", "true"),
            "init.defaultBranch": "main",
            "credential.helper": "store",
            "diff.tool": "vscode",
            "difftool.vscode.cmd": "code --wait --diff $LOCAL $REMOTE",
            "difftool.prompt": "false",
            "alias.pushit": "bundle create Dhanush.git --all",
        }

        for key, value in additional.items():
            configs[key] = value

        for key, value in configs.items():
            command = ["git", "config", f"--{level}", key, value]
            subprocess.run(command)

    def pwsh(self):
        """Some pwsh setup(WIP)."""
        pwsh_profile = Path(
            r"C:\Users\admin\Documents\PowerShell\Microsoft.PowerShell_profile.ps1"
        )
        cmd = r'oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\powerlevel10k_rainbow.omp.json" | Invoke-Expression'
        pwsh_profile.write_text(cmd)
