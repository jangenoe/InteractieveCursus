import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
notebooks = glob("ToegepasteAnalogeElektronica/*.ipynb", recursive=True)
notebooks+= glob("AnalogeElektronica2/*.ipynb", recursive=True)
notebooks+= glob("AnalogDesignTechniques/*.ipynb", recursive=True)
notebooks+= glob("MicroEnNanoTechnologie/*.ipynb", recursive=True)

for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)
    for index,cell in enumerate(ntbk.cells):
        if "remove-cell4BOOK" in cell.metadata.get('tags', []):
            cell.metadata.tags=cell.metadata.tags[:-1]
    nbf.write(ntbk, ipath)