class Watch:
    __watches_created = 0
    def __init__(self):
        Watch.__watches_created += 1

    @classmethod
    def dedicated_watch(cls, text):
        _watch = cls()
        _watch.engraving = text
        return _watch
    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created

    @staticmethod
    def validate(text):
        if len(text) < 40:
            pass
        else:
            return False