import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
notebooks = glob("ToegepasteAnalogeElektronica/*.ipynb", recursive=True)
notebooks+= glob("AnalogeElektronica2/*.ipynb", recursive=True)
notebooks+= glob("AnalogDesignTechniques/*.ipynb", recursive=True)

for ipath in notebooks:
    print("file om te zetten: ",ipath)
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)
    
    # voor alle code cellen: als niet gesloten --> sluiten
    
    for index,cell in enumerate(ntbk.cells):
        if "code" in cell.get('cell_type', {}):
            cell.metadata|={"jupyter": {"source_hidden": True}}

    nbf.write(ntbk, ipath)