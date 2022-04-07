from di2008 import AnalogPort, Di2008

class DataQ():
    def __init__(self, thermocoupleInfo):
        self.thermocouples = []
        for info in thermocoupleInfo:
            self.thermocouples.append(AnalogPort(info[0], thermocouple_type=info[1], filter='average'))
        self.daq = Di2008()
        self.daq.create_scan_list(self.thermocouples)
    
    def start(self):
        self.daq.start()

    def getThermocouple(self, index):
        return self.thermocouples[index].value
