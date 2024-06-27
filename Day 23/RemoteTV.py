class RemoteTv():
    def __init__(self):
        self.switchIsOn = False
        self.volume = 10

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def  VolumeUp(self):
        if self.volume < 100:
            self.volume = self.volume + 1

    def VolumeDown(self):
        if self.volume > 0:
            self.volume = self.volume - 1

# Extra method for debugging
    def show(self):
        print('Switch is on ?', self.switchIsOn)
        print('Volume is:', self.volume)

# Main code
remoteSatu = RemoteTv()
# Turn switch on, and Up the Volume 3 times
remoteSatu.turnOn()
remoteSatu.VolumeUp()
remoteSatu.VolumeUp()
remoteSatu.VolumeUp()
remoteSatu.show()

# Down the Volume 1 times, and turn switch off
remoteSatu.VolumeDown()
remoteSatu.turnOff()
remoteSatu.show()