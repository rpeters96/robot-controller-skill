from mycroft import MycroftSkill, intent_file_handler
import RPi.GPIO as GPIO
from time import sleep


class RobotController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)

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
            GPIO.output(7,1)
            sleep(2)
            return True
        elif self.voc_match(direction, 'right'):
            # move right
            self.log.info("right")
            GPIO.output(7,0)
            sleep(2)
            return True
        elif self.voc_match(direction, 'forward'):
            # move forward
            self.log.info("forward")
            GPIO.output(7,1)
            sleep(2)
            return True
        elif self.voc_match(direction, 'backward'):
            # move backward
            self.log.info("backward")
            GPIO.output(7,1)
            sleep(2)
            return True 
        else:
            return False

def stop(self):
    #stop moving
    self.log.info("stopping")
    GPIO.output(7,1)

def create_skill():
    return RobotController()
    

