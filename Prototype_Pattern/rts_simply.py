class Knight(object):
    """Knight class that is generated from the Barracks() class"""

    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.unit_type = "Knight"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return (
            "Unit Type: {0}\n"
            "Life: {1}\n"
            "Speed: {2}\n"
            "Attack Power: {3}\n"
            "Attack Range: {4}\n"
            "Weapon: {5}".format(
                self.unit_type,
                self.life,
                self.speed,
                self.attack_power,
                self.attack_range,
                self.weapon,
            )
        )


class Archer(object):
    """Archer class that is generated from the barracks() class"""

    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.unit_type = "Archer"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return (
            "Unit Type: {0}\n"
            "Life: {1}\n"
            "Speed: {2}\n"
            "Attack Power: {3}\n"
            "Attack Range: {4}\n"
            "Weapon: {5}".format(
                self.unit_type,
                self.life,
                self.speed,
                self.attack_power,
                self.attack_range,
                self.weapon,
            )
        )


class Barracks(object):
    """Barracks class that is used for generating units"""

    def generate_knight(self):
        return Knight(400, 5, 3, 1, "short sword")

    def generate_archer(self):
        return Archer(200, 7, 1, 5, "short bow")


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.generate_knight()
    archer1 = barracks.generate_archer()
    print("[**knight1**]\n{}".format(knight1))
    print("[**Archer1**]\n{}".format(archer1))
