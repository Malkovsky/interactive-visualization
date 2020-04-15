import os

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