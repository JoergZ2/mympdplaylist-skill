from mycroft import MycroftSkill, intent_file_handler


class Mympdplaylist(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mympdplaylist.intent')
    def handle_mympdplaylist(self, message):
        self.speak_dialog('mympdplaylist')


def create_skill():
    return Mympdplaylist()

