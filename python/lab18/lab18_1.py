# Experiments with Python and Bluetooth

import bluetooth

# Obtain the Bluetooth addresses of nearby devices
devices = bluetooth.discover_devices()

for device in devices:
  print(device)
