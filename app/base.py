import data.music_theory as music_data

class Base:

    def get_chromatic_scale(self, sharp_or_flat = 'sharp'):
        """Get the chromatic scale, either with sharp or flat representation
        Args:
            sharp_or_flat (str):

        Returns:
            list: The chromatic scale
        """
        notes = []
        for i in music_data.chromatic_scale:
            if sharp_or_flat == 'flat' and len(i) == 2:
                notes.append(i[1])
            elif sharp_or_flat == 'sharp':
                notes.append(i[0])
        return notes

