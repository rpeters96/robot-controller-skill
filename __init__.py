from mycroft import MycroftSkill, intent_file_handler


class RobotController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

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
            return True
        elif self.voc_match(direction, 'right'):
            # move right
            self.log.info("right")
            return True
        elif self.voc_match(direction, 'forward'):
            # move forward
            self.log.info("forward")
            return True
        elif self.voc_match(direction, 'backward'):
            # move backward
            self.log.info("backward")
            return True 
        else:
            return False

def create_skill():
    return RobotController()
    

