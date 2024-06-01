class MotorPair:
    def __init__(self, port1: str, port2: str):
        pass

    def start(self, speed: int, steering: int):
        pass


class ColorSensor:
    def __init__(self, port: str):
        pass

    def get_reflected_light(self):
        pass


class ForceSensor:
    def __init__(self, port: str):
        pass

    def wait_until_released(self):
        pass

    def wait_until_pressed(self):
        pass

    def is_pressed(self):
        pass


class DistanceSensor:
    def __init__(self, port: str):
        pass
