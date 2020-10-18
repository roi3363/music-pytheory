from itertools import cycle
from collections import Counter
from app.chord import Chord
from app.note import Note


class Guitar:
    """

    """
    def __init__(self):
        self.guitar_strings = ("E", "A", "D", "G", "B", "e")
        self.guitar_notes = self.set_guitar_notes()

    def get_chord_positions(self, chord):
        """

        Args:
            chord (Chord): Chord object

        Returns:

        """
        chord_notes = chord.get_chord(chord_name, mode, quality, inversion)
        root = None
        root_found = False
        chord = {}
        counter = Counter()
        for i,string in enumerate(self.guitar_strings):
            # First find the root note, then the rest of the strings
            if not root_found:
                note = self.find_note(chord_notes, string, (0, 5), root=True)
                if note:
                    root = {'position': note['position'], 'note': note['note']}
                    chord.update({ string: root })
                    root_found = True
                else:
                    chord.update({string: None})
            else:
                min_fret = max(root['position'] - 3, 0)
                max_fret = min_fret + 4
                note = self.find_note(chord_notes, string, (min_fret, max_fret))
                if note and note['note'] in chord_notes:
                    chord.update({string: {'position': note['position'], 'note': note['note']}})
                else:
                    chord.update({string: None})

        chord_positions = [x['position'] if x else None for x in chord.values()]
        multiple_frets = None
        for note in chord.values():
            if note:
                if chord_positions.count(note['position']) >= 2:
                    multiple_frets = note['position']
        if multiple_frets:
            for string,j in chord.items():
                 if j and j['position'] < multiple_frets:
                    note = self.find_note(chord_notes, string, (multiple_frets, multiple_frets + 3))
                    chord.update({string: note})
                    break

        return chord

    def set_guitar_notes(self):
        """

        Returns:

        """
        notes = {}
        choromatic_scale = self.note_obj.get_chromatic_scale("sharp")
        notes_cycle = cycle(choromatic_scale)
        for string in self.guitar_strings:
            for k,j in enumerate(notes_cycle):
                if string.upper() == j:
                    notes[string] = {0:j}
                    notes[string].update({x:next(notes_cycle) for x in range(1, 11)})
                    break
        return notes

    def find_note(self, chord_notes, string, fret_range, root = False):
        """

        Args:
            chord_notes:
            root:
            string:
            fret_range:

        Returns:

        """
        for i in range(fret_range[0], fret_range[1]):
            guitar_note = self.guitar_notes[string][i]
            if root:
                if chord_notes[0] == guitar_note:
                    return {'position': i, 'note': guitar_note}
            else:
                if guitar_note in chord_notes:
                    return {'position': i, 'note': guitar_note}
        return {}