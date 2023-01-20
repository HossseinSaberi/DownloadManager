class Downloadexception(Exception):
    pass

class QualityError(Downloadexception):
    pass

class FileBroken(Downloadexception):
    pass