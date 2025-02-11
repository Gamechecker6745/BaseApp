from imports import *


class Utils:
    @staticmethod
    def constrain(value: int | float, constraints: iter, overflow=False) -> int | float:
        minV, maxV = constraints

        if value < minV:
            value = constraints[overflow]
        elif value > maxV:
            value = constraints[not overflow]
        return value

    @staticmethod
    def align_position(dimensions, pos, align):
        pos = np.array(pos, 'float64')

        match align:
            case 0:
                pass
            case 1:
                pos -= np.array(dimensions, 'float64') / 2
            case 2:
                pos -= np.array(dimensions, 'float64')
            case _:
                warn('Invalid align value')
        return pos

    @staticmethod
    def load_image(file_path):
        try:
            image = pg.image.load(file_path)
            image.convert_alpha()

            return image.convert()

        except FileNotFoundError:
            warnings.warn(f"{file_path} not found.")

    @classmethod
    def files_in_directory(cls, directory):
        files = []

        for filename in os.listdir(directory):
            if '.' not in filename:
                files += cls.files_in_directory(directory + '/' + filename)
            else:
                files.append(filename)
        return files
