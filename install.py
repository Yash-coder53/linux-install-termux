import subprocess
import json

# Load configuration
with open('config.json') as f:
    config = json.load(f)

# Define installation functions
def install_ubuntu():
    subprocess.run(['sh', 'linux-distros/ubuntu/install.sh'])

def install_debian():
    subprocess.run(['sh', 'linux-distros/debian/install.sh'])

# Main installation function
def install_linux(dist):
    if dist == 'ubuntu':
        install_ubuntu()
    elif dist == 'debian':
        install_debian()
    else:
        print("Unsupported distribution")

# Run installation
if __name__ == '__main__':
    dist = config['distro']
    install_linux(dist)


# config.json

{
    "distro": "ubuntu"
}
