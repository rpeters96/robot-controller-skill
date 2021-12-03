from mycroft import MycroftSkill, intent_file_handler
try:
    import GPIO
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
´´

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
            GPIO.set("GPIO4","On")
            sleep(2)
            return True
        elif self.voc_match(direction, 'right'):
            # move right
            self.log.info("right")
            GPIO.set("GPIO4","Off")
            sleep(2)
            return True
        elif self.voc_match(direction, 'forward'):
            # move forward
            self.log.info("forward")
            GPIO.set("GPIO4","Off")
            sleep(2)
            return True
        elif self.voc_match(direction, 'backward'):
            # move backward
            self.log.info("backward")
            GPIO.set("GPIO4","On")
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
    

