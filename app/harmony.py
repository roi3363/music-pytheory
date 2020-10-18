from app.chord import Chord
import random

class Harmony:
    """

    """
    def __init__(self):
        self.chord = Chord()
        
    def get_random_bassline(self, scale_notes):
        """

        Args:
            scale_notes:
        """
        bassline = [scale_notes[0]] # the root as the first note
        bassline.extend([random.choice(scale_notes) for _ in range(7)])
        print(bassline)
        print(random.choice([1, 2, 3]))

        
    def get_1_4_5(self, key, mode, with_7th=False):
        """

        Args:
            key:
            mode:
        """
        scale = self.chord.get_scale_chords(key, mode, with_7th)
        return scale['I'], scale['IV'], scale['V']


