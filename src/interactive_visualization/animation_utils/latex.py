import numpy
import os


class Matrix:
    def __init__(self, array, precision=None):
        self.entry_ = numpy.array(array)
        self.precision = precision

    def __str__(self):
        lines = []
        lines.append("\\left(")
        lines.append(f"\\begin{{array}}{{{''.join('c')}}}")
        for i in range(self.entry_.shape[0]):
            if self.precision:
                lines.append(
                    ' & '.join([f"{self.entry_[i, j]}" for j in range(self.entry_.shape[1])]) + ' \\\\'
                )
            else:
                lines.append(
                    ' & '.join([f"{self.entry_[i, j]:.3f}" for j in range(self.entry_.shape[1])]) + ' \\\\'
                )

        lines.append(f"\\end{{array}}")
        lines.append("\\right)")
        return os.linesep.join(lines)


def import_as_beamer_images(outlist, imagedir, preffix, frame_name=""):
    latex_lines = []
    if not os.path.isdir(imagedir):
        os.makedirs(imagedir)
    for i, graph_repr in enumerate(outlist):
        latex_lines.append(f'\\begin{{frame}}{{frame_name}}')
        graph_repr.render(filename=os.path.join(imagedir, preffix + str(i)),
                          format='pdf')
        latex_lines.append(f'\t\\includegraphics[width=\\textwidth]{{{imagedir}/{preffix}{str(i)}.pdf}}')
        latex_lines.append(f'\\end{{frame}}')
    return latex_lines
