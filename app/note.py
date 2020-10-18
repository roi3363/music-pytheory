import data.music_theory as music_data
from exceptions import InvalidNoteException
from app.base import Base





class Note(Base):
    def __init__(self, name):
        self.validate_note(name)
        self.name = self.name
        self.name = name
        self._accidental = None

    def validate_note(self, name):
        pass

    def accidental(self):
        if self.is_flat():
            return 'flat'
        elif self.is_sharp():
            return 'sharp'
        else:
            return 'natural'

    def is_valid_note(self):
        chromatic_scale = self.get_chromatic_scale()
        note_exists = not any(x for x in chromatic_scale if self.name in x)
        if not note_exists:
            raise InvalidNoteException("Note is invalid")

    def is_sharp(self):
        if self.is_valid_note():
            if 'b' in self.name:
                return False
            else:
                return True
        else:
            raise InvalidNoteException("Note is invalid")

    def is_flat(self):
        return True if "b" in self.name else False

    def has_accidental(self):
        if self.is_sharp() or self.is_flat():
            return True
        else:
            return False

    def convert_accidentals(self, note):
        is_sharp = self.is_sharp()
        for i in music_data.enharmonic_notes:
            if note in i:
                return i[1] if is_sharp else i[0]

    def augment_note(self, note):
        return note

    def diminish_note(self, note):
        return note

    def get_intervals_in_half_steps(self, note):
        steps = 0
        desired_note = False
        accidental = self.accidental
        chromatic_scale = self.get_chromatic_scale(accidental) * 2

        for i in chromatic_scale:
            if i == self.name:
                desired_note = True
            if desired_note:
                steps += 1
            if desired_note and i == note:
                return steps - 1

        return steps

    def get_intervals_in_name(self, note1, note2):
        interval_in_half_steps = self.get_intervals_in_half_steps(note1)
        if interval_in_half_steps:
            return music_data.interval_names[interval_in_half_steps]

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other