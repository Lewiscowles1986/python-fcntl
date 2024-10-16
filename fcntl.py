import sys

if all([
    sys.platform != "linux",
    sys.platform != "darwin"
]):
    print("fcntl package is only available on *nix systems. Try Docker?", file=sys.stderr)
    exit(1)
