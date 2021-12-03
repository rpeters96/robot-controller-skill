from mycroft import MycroftSkill, intent_file_handler
try:
    import RPi.GPIO as GPIO
    """This is trapped so you can still run without RPi.GPIO
    GPIO will be checked before use
    """
    pi_interface = True
except:
    pi_interface = False
    pass
from time import sleep


class RobotController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):    
        LED_GPIO = 4
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_GPIO, GPIO.OUT)
        GPIO.output(LED_GPIO, False)

    @intent_file_handler('controller.robot.intent')
    def handle_controller_robot(self, message):
        direction_type = message.data.get('direction.type')
        if direction_type is not None:
            self.move_direction(direction_type)
        else:
            self.speak_dialog('which.direction')

    def converse(self, message):
        return self.move_direction(message.data['utterances'][0])

    def move_direction(self, direction):
        if self.voc_match(direction, 'left'):
            # move left
            self.log.info("left")
            GPIO.output(LED_GPIO, True)
            sleep(2)
            return True
        elif self.voc_match(direction, 'right'):
            # move right
            self.log.info("right")
            GPIO.output(LED_GPIO, False)
            sleep(2)
            return True
        elif self.voc_match(direction, 'forward'):
            # move forward
            self.log.info("forward")
            GPIO.output(LED_GPIO, True)
            sleep(2)
            return True
        elif self.voc_match(direction, 'backward'):
            # move backward
            self.log.info("backward")
            GPIO.output(LED_GPIO, True)
            sleep(2)
            return True 
        else:
            return False

def stop(self):
    #stop moving
    self.log.info("stopping")
    GPIO.output(LED_GPIO, False)

def create_skill():
    return RobotController()
    

