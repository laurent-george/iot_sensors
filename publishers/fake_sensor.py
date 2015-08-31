import time


class Sensor(object):
    def __init__(self, name='dummy'):
        self.name = name
        self.seq_number = 0
        self.value = 0

    def update(self):
        self.value += 2

    def publish_data(self):
        self.update()  # we update after each get for the dummy
        data = {}
        data['sensor_name'] = self.name
        data['value'] = self.value
        data['timestamp'] = time.time()

        # do sql publish
        print(data)



def main():
    try:
        sensor = Sensor('Fake Temp 1')
        wait_time = 2.0  # 2 seconds
        while True:
            sensor.publish_data()
            time.sleep(wait_time)
    except KeyboardInterrupt:
        print("User pressed ctrl-c, quitting.")

if __name__ == "__main__":
    main()
