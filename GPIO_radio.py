from gpiozero import Device, LED, Button, MCP3008 #MCP3008 er ADCen
from gpiozero.pins.mock import MockFactory

Device.pin_factory = MockFactory()

button1 = Button(17) #This button is connected to GPIO17 (Not pin 17)
potensiometer = MCP3008(12)


def next_station()
    print("next station")

button1.when_pressed = next_station #No function call(), but assigning the "when pressed" to this function

#todo:
# Add shebang
# Add analog read function
# Make all the buttons
# find out how to play/pause/volume adjust/mute /next station/previous station
