import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
notebooks = glob("ToegepasteAnalogeElektronica/*.ipynb", recursive=True)
notebooks+ = glob("AnalogeElektronica2/*.ipynb", recursive=True)
notebooks+ = glob("AnalogDesignTechniques/*.ipynb", recursive=True)

for ipath in notebooks:
    print("file om te zetten: ",ipath)
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)
    
    ntbk.cells[0].metadata.pop('slideshow')
    ntbk.cells[0].metadata|={"@deathbeds/jupyterlab-fonts": {
             "styles": {
              "": {
               "body[data-jp-deck-mode='presenting'] &": {
                "position": "fixed",
                "top": "-17.5%"
               }
              }
             }
        }}
    
    u=nbf.v4.new_markdown_cell(source=["<div style = \"height: 700px; width:100%; background-color:#1D8DB0; color:#fff\"></div>"])
    u.metadata={
        "@deathbeds/jupyterlab-fonts": {
             "styles": {
              "": {
               "body[data-jp-deck-mode='presenting'] &": {
                "height": "82%",
                "left": "-4%",
                "position": "fixed",
                "top": "7.5%",
                "width": "110%"
               }
              }
             }
        },
        "slideshow": {"slide_type": "slide"},
        "jupyterlab-deck": {"layer": "slide"},
        "tags": ["remove_cell","remove_cell4reveal"]
    }
    ntbk.cells.insert(0, u)

    u=nbf.v4.new_markdown_cell(source=["<img src=\"./images/KULeuven.png\" >"])
    u.metadata={
        "@deathbeds/jupyterlab-fonts": {
             "styles": {
              "": {
               "body[data-jp-deck-mode='presenting'] &": {
                "height": "13.7%",
                "left": "9.2%",
                "position": "fixed",
                "top": "-15%",
                "width": "20.4%"
               }
              }
             }
        },
        "jupyterlab-deck": {"layer": "slide"},
        "tags": ["remove_cell","remove_cell4reveal"]
    }
    ntbk.cells.insert(1, u)

    preslides=3
    
    u=nbf.v4.new_markdown_cell(source=["<div style = \"height: 50px; width:100%; background-color:#1D8DB0;\"></div>"])
    u.metadata={
        "@deathbeds/jupyterlab-fonts": {
             "styles": {
              "": {
               "body[data-jp-deck-mode='presenting'] &": {
                "height": "11%",
                "left": "-4%",
                "position": "fixed",
                "top": "95%",
                "width": "110%"
               }
              }
             }
        },
        "jupyterlab-deck": {"layer": "deck"},
        "tags": ["remove_cell","remove_cell4reveal"]
    }
    ntbk.cells.insert(preslides+1, u)
    
    u=nbf.v4.new_markdown_cell(source=["<img src=\"./images/KULeuven.png\" >"])
    u.metadata={
        "@deathbeds/jupyterlab-fonts": {
             "styles": {
              "": {
               "body[data-jp-deck-mode='presenting'] &": {
                "top": "60%",
                "position": "fixed",
                "left": "91%",
                "width": "6%"
               }
              }
             }
        },
        "jupyterlab-deck": {"layer": "deck"},
        "tags": ["remove_cell","remove_cell4reveal"]
    }
    ntbk.cells.insert(preslides+2, u)
    
    # voor alle code cellen: als niet gesloten --> sluiten
    
    for index,cell in enumerate(ntbk.cells):
        if "code" in cell.get('cell_type', {}):
            cell.metadata|={"jupyter": {"source_hidden": True}}

    nbf.write(ntbk, ipath)