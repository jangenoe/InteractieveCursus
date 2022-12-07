import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
notebooks = glob("ToegepasteAnalogeElektronica/*.ipynb", recursive=True)

for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

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
                "top": "1.1%",
                "width": "20.4%"
               }
              }
             }
        },
        "jupyterlab-deck": {"layer": "slide"},
        "tags": ["remove_cell","remove_cell4reveal"]
    }
    ntbk.cells.insert(1, u)

#### hier nog alle andere headerinfo [auteur, datum, .... ] invoegen nadat de juiste styles gedefinieerd zijn.

    preslides=3
    u=nbf.v4.new_markdown_cell(source=["######  Overzicht\n"])
    u.metadata={
        "slideshow": {"slide_type": "slide"},
        "tags": ["remove_cell","remove_cell4reveal"]
    }
    ntbk.cells.insert(preslides, u)
    
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
                "bottom": "1%",
                "position": "fixed",
                "right": "11%",
                "width": "6%"
               }
              }
             }
        },
        "jupyterlab-deck": {"layer": "deck"},
        "tags": ["remove_cell","remove_cell4reveal"]
    }
    ntbk.cells.insert(preslides+2, u)
    
    for index,cell in enumerate(ntbk.cells):
        if 'KULeuvenSlides' in cell.get('metadata', {}):
            if 'slide_title' in cell.get('metadata', {}).get('KULeuvenSlides', {}):
                st=cell.get('metadata', {}).get('KULeuvenSlides', {}).get('slide_title', ".")
                if "<BR>" in st:
                    u=nbf.v4.new_markdown_cell(source=["##### "+cell.get('metadata', {}).get('KULeuvenSlides', {}).get('slide_title', ".")])
                else:
                    u=nbf.v4.new_markdown_cell(source=["###### "+cell.get('metadata', {}).get('KULeuvenSlides', {}).get('slide_title', ".")])
                u.metadata={"slideshow": {"slide_type": "slide"},"tags": ["remove_cell"]}
                cell.metadata.KULeuvenSlides.pop('slide_title')
                if 'slideshow' in cell.get('metadata', {}):
                    cell.metadata.pop('slideshow')             
                ntbk.cells.insert(index, u)
            if 'slide_ref' in cell.get('metadata', {}).get('KULeuvenSlides', {}):
                u=nbf.v4.new_markdown_cell(source=["1 "+cell.get('metadata', {}).get('KULeuvenSlides', {}).get('slide_ref', ".")])
                u.metadata.tags=["remove_cell","remove_cell4reveal"]
                ntbk.cells.insert(index, u)  
    nbf.write(ntbk, ipath)