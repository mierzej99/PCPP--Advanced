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
        if len(text) < 40 and text.isalnum():
            return True
        return False
        # raise Exception


print(Watch.get_number_of_watches_created())
watch = Watch()
print(Watch.get_number_of_watches_created())
try:
    if Watch.validate('siema123'):
        watcheng = Watch.dedicated_watch('siema123')
    print(Watch.get_number_of_watches_created())
    if Watch.validate('d@pa'):
        watcheng2 = Watch.dedicated_watch('d@pa')
    print(Watch.get_number_of_watches_created())
except Exception as e:
    print("Engraving is not so good", e)
