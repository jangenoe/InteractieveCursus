import base64
import io
import nbformat as nbf
from glob import glob
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE, PP_PLACEHOLDER, MSO_SHAPE_TYPE
from PIL import UnidentifiedImageError
from IPython.lib.latextools import latex_to_png

# Collect a list of all notebooks in the content folder
notebooks = glob("ToegepasteAnalogeElektronica/*.ipynb", recursive=True)
notebooks+= glob("AnalogeElektronica2/*.ipynb", recursive=True)
notebooks+= glob("AnalogDesignTechniques/*.ipynb", recursive=True)

#slidetemplate="./.github/common/KULeuventemplate.pptx"
slidetemplate="./.github/common/KULeuven_600TEMPLATE.pptx"

report_all_shapes_in_template=True
if report_all_shapes_in_template:
    prs = Presentation(slidetemplate)
    for i1,lay in enumerate(prs.slide_layouts):
        slide = prs.slides.add_slide(lay)
        for i2,shap in enumerate(slide.shapes):
            if shap.shape_type==14:
                print(i1,i2,shap.shape_type,shap.placeholder_format.type)
            else:
                print(i1,i2,shap.shape_type) 

def find_between( s, first, last ):
    try:
        start = s.index( first )
        end = s.index( last, start+len(first) )+len(last)
        return s[start:end]
    except ValueError:
        return ""

def maketitle(cell,slide):
    if "KULeuvenSlides" in cell.get('metadata', {}):
        if "slide_title" in cell.metadata.get('KULeuvenSlides', {}):
            st = cell.metadata.KULeuvenSlides["slide_title"]
            slide.shapes.title.text=st.replace("<BR>","\n")
            slide.shapes.title.text_frame.fit_text(font_family="Arial",max_size=32,bold=True, font_file=r".github/common/fonts/arialbd.ttf")         
    
for ipath in notebooks:
    print("file om te zetten: ",ipath)
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)
    prs = Presentation(slidetemplate)
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    if "title" in ntbk.metadata.get('KULeuvenSlides', {}):
        title_shape = slide.shapes.title
        title_shape.text = ntbk.metadata.KULeuvenSlides["title"].replace("<BR>","\n")
        #title_shape.text_frame.fit_text()
        #title_shape.text_frame.paragraphs[0].font.size = Pt(44)
        #title_shape.text_frame.paragraphs[0].font.bold = True
        #title_shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)  # White text
        #title_shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    if "subtitle" in ntbk.metadata.get('KULeuvenSlides', {}):
        subtitle= slide.shapes.add_textbox(Inches(7),Inches(4), Inches(5),Inches(2.0))  #left, top, width, height
        subtitle.text = ntbk.metadata.KULeuvenSlides["subtitle"].replace("<BR>","\n")
        #subtitle.text_frame.fit_text()
        for par in subtitle.text_frame.paragraphs:
            par.font.size = Pt(24)
            par.font.color.rgb = (RGBColor(255, 255, 255))  # White text
        #subtitle.text_frame.paragraphs[0].alignment = (PP_ALIGN.CENTER)
    if "authors" in ntbk.metadata.get('KULeuvenSlides', {}):
        txBox = slide.shapes.add_textbox(Inches(7),Inches(6.1), Inches(2),Inches(0.5))  #left, top, width, height
        tf = txBox.text_frame
        tf.text = ntbk.metadata.KULeuvenSlides["authors"]
        #tf.paragraphs[0].font.size = Pt(24)
        tf.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
        #tf.paragraphs[0].alignment = PP_ALIGN.CENTER        
    if "date" in ntbk.metadata.get('KULeuvenSlides', {}):
        txBox = slide.shapes.add_textbox(Inches(7),Inches(6.3), Inches(2),Inches(0.5))  #left, top, width, height
        tf = txBox.text_frame
        tf.text = ntbk.metadata.KULeuvenSlides["date"]
        #tf.paragraphs[0].font.size = Pt(24)
        tf.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
        #tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    
    for index,cell in enumerate(ntbk.cells):
        if "code" in cell.get('cell_type', {}) and not("remove_cell4pptx" in cell.metadata.get('tags', {})):
            if "slide_type" in cell.metadata.get('slideshow', {}):
                if  cell.metadata.slideshow.get("slide_type", ())=="slide":
                   for output_idx, output in enumerate(cell.get("outputs", ())):
                        if "image/png" in output.get("data", {}):                           
                            slide = prs.slides.add_slide(prs.slide_layouts[6])
                            maketitle(cell,slide)  
                            image_stream = io.BytesIO(base64.b64decode(output.data["image/png"]))
                            try:                            
                                pictp=slide.shapes.add_picture(image_stream, Inches(1), Inches(1.29), height=Inches(5.5)) 
                                if pictp.width>prs.slide_width:
                                    pictp.width=prs.slide_width
                                    pictp.left=Inches(0)
                                else:
                                    pictp.left=(prs.slide_width-pictp.width)//2
                            except UnidentifiedImageError:
                                print("  image/png  error for cell number "+str(index))
                        elif "image/jpeg" in output.get("data", {}):                           
                            slide = prs.slides.add_slide(prs.slide_layouts[6])
                            maketitle(cell,slide)  
                            image_stream = io.BytesIO(base64.b64decode(output.data["image/jpeg"]))
                            try:                            
                                pictp=slide.shapes.add_picture(image_stream, Inches(1), Inches(1.29), height=Inches(5.5)) 
                                if pictp.width>prs.slide_width:
                                    pictp.width=prs.slide_width
                                    pictp.left=Inches(0)
                                else:
                                    pictp.left=(prs.slide_width-pictp.width)//2
                            except UnidentifiedImageError:
                                print("  image/jpeg  error for cell number "+str(index))
                        elif "text/plain" in output.get("data", {}):
                            if len(output["text"]<20):
                                slide = prs.slides.add_slide(prs.slide_layouts[5])
                                maketitle(cell,slide) 
                                slide.shapes[0].text="".join(output["text/plain"])
                                for par in slide.shapes[0].text_frame.paragraphs:
                                    par.line_spacing = Pt(8)
                                    par.font.color.rgb = RGBColor(0, 0, 0)
                                slide.shapes[0].text_frame.fit_text(font_family="Courier",max_size=30, font_file=r".github/common/fonts/cour.ttf") 
                            else:
                                slide = prs.slides.add_slide(prs.slide_layouts[5])
                                maketitle(cell,slide) 
                                slide.shapes[0].text="".join(output["text/plain"][:20])
                                for par in slide.shapes[0].text_frame.paragraphs:
                                    par.line_spacing = Pt(8)
                                    par.font.color.rgb = RGBColor(0, 0, 0)
                                slide.shapes[0].text_frame.fit_text(font_family="Courier",max_size=30, font_file=r".github/common/fonts/cour.ttf")      
                                slide = prs.slides.add_slide(prs.slide_layouts[5])
                                maketitle(cell,slide) 
                                slide.shapes[0].text="".join(output["text/plain"][20:])
                                for par in slide.shapes[0].text_frame.paragraphs:
                                    par.line_spacing = Pt(8)
                                    par.font.color.rgb = RGBColor(0, 0, 0)
                                slide.shapes[0].text_frame.fit_text(font_family="Courier",max_size=30, font_file=r".github/common/fonts/cour.ttf")
                        elif "text" in output:
                            if len(output["text"]<20):
                                slide = prs.slides.add_slide(prs.slide_layouts[5])
                                maketitle(cell,slide) 
                                slide.shapes[0].text="".join(output["text"])
                                for par in slide.shapes[0].text_frame.paragraphs:
                                    par.line_spacing = Pt(8)
                                    par.font.color.rgb = RGBColor(0, 0, 0)
                                slide.shapes[0].text_frame.fit_text(font_family="Courier",max_size=30, font_file=r".github/common/fonts/cour.ttf") 
                            else:
                                slide = prs.slides.add_slide(prs.slide_layouts[5])
                                maketitle(cell,slide) 
                                slide.shapes[0].text="".join(output["text"][:20])
                                for par in slide.shapes[0].text_frame.paragraphs:
                                    par.line_spacing = Pt(8)
                                    par.font.color.rgb = RGBColor(0, 0, 0)
                                slide.shapes[0].text_frame.fit_text(font_family="Courier",max_size=30, font_file=r".github/common/fonts/cour.ttf")           
                                slide = prs.slides.add_slide(prs.slide_layouts[5])
                                maketitle(cell,slide) 
                                slide.shapes[0].text="".join(output["text"][20:])
                                for par in slide.shapes[0].text_frame.paragraphs:
                                    par.line_spacing = Pt(8)
                                    par.font.color.rgb = RGBColor(0, 0, 0)
                                slide.shapes[0].text_frame.fit_text(font_family="Courier",max_size=30, font_file=r".github/common/fonts/cour.ttf")           
                                
                        #else:
                                #print("  "+content_type+"  error for cell number "+str(index))
                                
        if "markdown" in cell.get('cell_type', {}) and not("remove_cell4pptx" in cell.metadata.get('tags', {})):
            if "slide_type" in cell.metadata.get('slideshow', {}):
                if  cell.metadata.slideshow.get("slide_type", ())=="slide":
                    slide = prs.slides.add_slide(prs.slide_layouts[6])
                    maketitle(cell,slide)
                    running_height=Inches(2.28)
                    if "KULeuvenSlides" in cell.get('metadata', {}):
                         if "eq_vertical" in cell.metadata.get('KULeuvenSlides', {}):
                            running_height+=Inches(cell.metadata.KULeuvenSlides["eq_vertical"])
                if  cell.metadata.slideshow.get("slide_type", ())=="slide" or cell.metadata.slideshow.get("slide_type", ())=="fragment": 
                    latexpng=find_between( "".join(cell.get('source', {})) , "$$", "$$" )
                    latexpng2=find_between( "".join(cell.get('source', {})) , "\begin{equation}", "\end{equation}" )
                    if len(latexpng2)>0:
                        latexpng=latexpng2
                    if len(latexpng)>0:
                        try:
                            pictp=slide.shapes.add_picture(io.BytesIO(latex_to_png(latexpng,backend="dvipng",scale=2)), Inches(1),running_height) 
                        except UnidentifiedImageError:
                            print("   latex error for cell number "+str(index))
                        if pictp.width>prs.slide_width:
                            pictp.width=prs.slide_width
                            pictp.left=Inches(0)
                        else:
                            pictp.left=(prs.slide_width-pictp.width)//2
                        running_height+=pictp.height+Inches(0.3)
                    else:
                        box= slide.shapes.add_textbox(Inches(1),running_height, Inches(10),Inches(2.0))
                        box.text="".join(cell.get('source', {}))
                        #for par in box.text_frame.paragraphs:
                            #par.font.color.rgb = RGBColor(0, 0, 0)
                        if len(box.text)>0:
                            try:
                                box.text_frame.fit_text(font_family="Calibri",max_size=30, font_file=r".github/common/fonts/calibri.ttf")
                            except:
                                print("   text_fit error for cell number "+str(index))

                        running_height+=box.height+Inches(0.3)

    slide = prs.slides.add_slide(prs.slide_layouts[10])
    slide = prs.slides.add_slide(prs.slide_layouts[9])
    prs.save(ipath[:-6]+".pptx")