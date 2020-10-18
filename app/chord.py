import data.music_theory as music_data
from app.note import Note
from app.base import Base

class Chord(Base):
    """

    """
    def __init__(self, root, quality ='major', interval = None, inversion = None):
        self.validate_arguments()
        super().__init__()
        self._root = Note(root)
        self._quality = quality
        self._interval = interval
        self._inversion = inversion
        quality_name = music_data.chord_qualities[self._quality]
        self.name = f'{self._root}{quality_name}'
        if self._interval:
            self.name += f'{self._interval}'
        chrom_scale = self.get_chromatic_scale(self._root.accidental) * 2
        root_index = chrom_scale.index(self._root)
        chrom_scale = chrom_scale[root_index:]
        if self._interval:
            chord_degrees = music_data.chords_types[f'{self._quality}{self._interval}']
        else:
            chord_degrees = music_data.chords_types[f'{self._quality}']
        chord_notes = [chrom_scale[x] for x in chord_degrees]
        if self._inversion:
            self.chord_notes = self.invert_chord(chord_notes, self._inversion)
        else:
            self.chord_notes = chord_notes

    def invert_chord(self, chord, inversion = 'root'):
        """

        Args:
            chord (list): The notes of the chord
            inversion (str): The inversion name (root, first, second; third for 4-note chords)

        Returns:
            list: The notes of the inverted chord
        """
        if inversion == 'root':
            return chord
        elif len(chord) == 3:
            if inversion == 'first':
                return chord[1], chord[2], chord[0]
            elif inversion == 'second':
                return chord[2], chord[0], chord[1]
        elif len(chord) == 4:
            if inversion == 'first':
                return chord[1], chord[2], chord[3], chord[0]
            elif inversion == 'second':
                return chord[2], chord[3], chord[0], chord[1]
            elif inversion == 'third':
                return chord[3], chord[0], chord[1], chord[2]
        return chord

    def __repr__(self):
        return self.name

    def validate_arguments(self):
        pass
