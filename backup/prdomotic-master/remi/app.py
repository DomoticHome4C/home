import remi.gui as gui
from remi import start, App
import serial

ser = serial.Serial('/dev/ttyACM0', 115200)

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        while True:
            if(ser.in_waiting >0):
                line = ser.readline()
                container = gui.VBox(width=400, height=400)
                self.lbl = gui.Label(line)
                self.bt = gui.Button('Update')

                # setting the listener for the onclick event of the button
                self.bt.onclick.connect(self.on_button_pressed)

                # appending a widget to another, the first argument is a string key
                container.append(self.lbl)
                container.append(self.bt)

                # returning the root widget
                return container

    # listener function
    def on_button_pressed(self, widget):
        line = ser.readline()
        self.lbl.set_text(line)

# starts the web server
start(MyApp, update_interval=0)
