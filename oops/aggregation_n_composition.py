# In object-oriented programming, both aggregation and composition allow for creating relationships between classes without using inheritance.

# Inheritance:
# - Inheritance is an "is-a" relationship.

# Aggregation:
# - Aggregation is a "has-a" relationship, where an object contains another object but does not own it, meaning the contained object can exist independently of the parent object.
# - Ex: Team contains players but does not own them, meaning the player can exist independently of the team.


class Player:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)


# Composition:
# - Composition is a "has-a" relationship, where an object contains another object and owns it, meaning the contained object cannot exist independently of the parent object.
# - Ex: Ex: Email contains attachments and owns them, meaning the attachment cannot exist independently of the Email (i.e., attachments are part of the Email and don’t make sense without it and have no purpose outside of it).


class Attachment:
    def __init__(self, filename):
        self.filename = filename


class Email:
    def __init__(self, subject):
        self.subject = subject
        self.attachments = []

    def add_attachment(self, filename):
        attachment = Attachment(filename)
        self.attachments.append(attachment)
