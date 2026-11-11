import subprocess

def run(cmd):
    """Run a shell command and return its output."""
    return subprocess.check_output(cmd, shell=True).decode()

def parse_port(s):
    return int(s)
