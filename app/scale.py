from itertools import cycle

from app.chord import Chord
from app.note import Note
import data.music_theory as music_data
from app.base import Base


class Scale(Base):
    def __init__(self, key, mode = 'major', scale_type = 'diatonic'):
        super().__init__()
        self.key = key
        # scales are named diatonic_major, pentatonic_major etc.
        self.positions = music_data.scales[f'{scale_type}_{mode}']

    def get_scale_notes(self):
        # doubles the chromatic scale for looping over it twice, if necessary
        chrom_scale = self.get_chromatic_scale(self.note.accidental) * 2
        a = chrom_scale[chrom_scale.index(self.note):]
        for i in self.positions:
            obj = Chord(a[i])
            print(obj)

    def get_scale_chords(self, with_7th = False):
        scale_notes = self.get_scale_notes()


    def get_inverted_scale_chords(self, key, mode, with_7th=False):
        scale_chords = self.get_scale_chords(key, mode, with_7th)
        new_scale = {}
        for roman_numer,root_position in scale_chords.items():
            first_inversion = self.invert_chord(root_position, inversion='first')
            second_inversion = self.invert_chord(root_position, inversion='second')
            if with_7th:
                third_inversion = self.invert_chord(root_position, inversion='third')
                new_scale.update({roman_numer: [root_position, first_inversion, second_inversion, third_inversion]})
            else:
                new_scale.update({roman_numer: [root_position, first_inversion, second_inversion]})
        return new_scale

    def get_chords_with_same_bass(self, key, mode, with_7th=False):
        scale_chords = self.get_inverted_scale_chords(key, mode, with_7th)
        final_list = {x[0][0]: [] for x in scale_chords.values()}  # {'C': [], 'D': [], ...}
        for k in final_list.keys():
            chords_list = []
            for i, scale_chord in enumerate(cycle(scale_chords.items())):
                roman, chords = scale_chord
                a = [x for x in chords if x[0] == k]
                chords_list.extend(a)
                if i == 6:
                    final_list[k] = chords_list
                    break
        return final_list



