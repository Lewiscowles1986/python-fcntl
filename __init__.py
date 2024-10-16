# main.py (or whatever your entry script is called)

import sys
import importlib
import os

class FcntlBlocker:
    def find_spec(self, fullname, path, target=None):
        if fullname == "fcntl":
            if sys.platform == "linux" or sys.platform == "darwin":
                # Block fcntl from being imported on Linux/macOS
                print("Blocking fnctl import on Unix-like systems", file=sys.stderr)
                return None  # This prevents fnctl from being imported
        return None  # Allow all other modules to load as normal

# Add the custom finder to sys.meta_path
sys.meta_path.insert(0, FcntlBlocker())

# Now the import will behave based on the platform
try:
    import fcntl
except ImportError as e:
    print(e)
