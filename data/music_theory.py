chromatic_scale = (
    ('A',),
    ('A#','Bb'),
    ('B'),
    ('C',),
    ('C#','Db'),
    ('D',),
    ('D#','Eb'),
    ('E',),
    ('F',),
    ('F#','Gb'),
    ('G',),
    ('G#','Ab')
)

enharmonic_notes = (
    ('A#', 'Bb'),
    ('C#', 'Db'),
    ('D#', 'Eb'),
    ('F#', 'Gb'),
    ('G#', 'Ab'),
)
chord_qualities = {
    'major': 'maj',
    'minor': 'min',
    'diminished': 'dim',
    'augmented': 'aug',
    'dominant': 'dom',
}
# Numbers represents the interval
chords_types = {
    'major': (0, 4, 7),
    'minor': (0, 3, 7),
    'half_diminished': (0, 3, 7),
    'diminished': (0, 3, 7),
    'augmented': (0, 3, 7),
    'major7': (0, 4, 7, 11),
    'minor7': (0, 3, 7, 10),
    'majorsus2': (0, 1, 4),
    'majorsus4': (0, 3, 4),
    'minorsus2': (0, 1, 4),
    'minorsus4': (0, 3, 4),
    '6th': (0, 2, 4, 5),
    'add9': (0, 2, 4, 1),
    'add11': (0, 2, 4, 3),
}
chords_positions = (
    [0, 2, 4, 6],
    [1, 3, 5, 0],
    [2, 4, 6, 1],
    [3, 5, 0, 2],
    [4, 6, 1, 3],
    [5, 0, 2, 4],
    [6, 1, 3, 5],
)
interval_names = {
    0: {'id': 'unison', 'Name': 'Unison'},
    1: {'id': 'minor_second', 'Name': 'Minor second'},
    2: {'id': 'major_second', 'Name': 'Major second'},
    3: {'id': 'minor_third', 'Name': 'Minor third'},
    4: {'id': 'major_third', 'Name': 'Major third'},
    5: {'id': 'fourth', 'Name': 'Perfect fourth'},
    6: {'id': 'tritone', 'Name': 'Tritone'},
    7: {'id': 'fifth', 'Name': 'Perfect fifth'},
    8: {'id': 'minor_sixth', 'Name': 'Minor sixth'},
    10: {'id': 'major_sixth', 'Name': 'Major sixth'},
    11: {'id': 'minor_seventh', 'Name': 'Minor seventh'},
    12: {'id': 'major_seventh', 'Name': 'Major seventh'},
}
scales = {
    'diatonic_minor': (0, 2, 3, 5, 7, 8, 10),
    'diatonic_major': (0, 2, 4, 5, 7, 9, 11),
    'pentatonic_minor': (0, 3, 5, 7, 10),
    'pentatonic_major': (0, 2, 4, 7, 9),
}
roman_major = ('I','ii','iii','IV','V','vi','viio')
roman_minor = ('i','iio','III','iv','v','VI','VII')

fifths = ('C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F#')
roman_numers_major = {y:chords_positions[x] for x,y in enumerate(roman_major)}
roman_numers_minor = {y:chords_positions[x] for x,y in enumerate(roman_minor)}








