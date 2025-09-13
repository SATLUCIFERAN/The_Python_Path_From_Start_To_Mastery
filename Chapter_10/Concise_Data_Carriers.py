
# A standard class for a simple data container

class MissionReport:
    def __init__(self, name, date, jedi):
        self.name = name
        self.date = date
        self.jedi = jedi

    def __repr__(self):
        return f"MissionReport(name={self.name}, date={self.date},"\
               f"jedi={self.jedi})"




