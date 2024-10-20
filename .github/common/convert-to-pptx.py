import base64
import io
import nbformat as nbf
from glob import glob
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE, PP_PLACEHOLDER
from PIL import UnidentifiedImageError
from IPython.lib.latextools import latex_to_png

# Collect a list of all notebooks in the content folder
notebooks = glob("ToegepasteAnalogeElektronica/*.ipynb", recursive=True)
notebooks+= glob("AnalogeElektronica2/*.ipynb", recursive=True)
notebooks+= glob("AnalogDesignTechniques/*.ipynb", recursive=True)

def find_between( s, first, last ):
    try:
        start = s.index( first )
        end = s.index( last, start+len(first) )+len(last)
        return s[start:end]
    except ValueError:
        return ""

def maketitle(cell,slide):
    st = cell.metadata.KULeuvenSlides["slide_title"]
    slide.shapes.title.text=st.replace("<BR>","\n")
    #slide.shapes.title.text_frame.fit_text()  #problem font file on linux
    if "<BR>" in st:
        slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(20)
        slide.shapes.title.text_frame.paragraphs[1].font.size = Pt(20)
    elif len(st)>70:
       slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(20)
    elif len(st)>60:
       slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(24)
    elif len(st)>50:
       slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(28)
    elif len(st)>40:
       slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(32)                                           
for ipath in notebooks:
    print("file om te zetten: ",ipath)
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)
#    prs = Presentation("./.github/common/KULeuventemplate.pptx")
    prs = Presentation("./.github/common/KULeuven_600TEMPLATE.pptx")
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
        subtitle.text_frame.paragraphs[0].font.size = Pt(24)
        subtitle.text_frame.paragraphs[0].font.color.rgb = (RGBColor(255, 255, 255))  # White text
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
                        for content_type, content in output.get("data", {}).items():                           
                            if content_type.startswith("image/png"):
                                slide = prs.slides.add_slide(prs.slide_layouts[6])
                                if "KULeuvenSlides" in cell.get('metadata', {}):
                                    if "slide_title" in cell.metadata.get('KULeuvenSlides', {}):
                                        maketitle(cell,slide)                                 
                                image_stream = io.BytesIO(base64.b64decode(output.data[content_type]))
                                try:
                                    pictp=slide.shapes.add_picture(image_stream, Inches(1), Inches(1.29), height=Inches(5.5)) 
                                    if pictp.width>prs.slide_width:
                                        pictp.width=prs.slide_width
                                        pictp.left=Inches(0)
                                    else:
                                        pictp.left=(prs.slide_width-pictp.width)//2
                                except UnidentifiedImageError:
                                    print("  "+content_type+"  error for cell number "+str(index))
                            #elif content_type.startswith("image/")::
                                #print("  "+content_type+"  error for cell number "+str(index))
                            #else:
                                #print("  "+content_type+"  error for cell number "+str(index))
                                
        if "markdown" in cell.get('cell_type', {}) and not("remove_cell4pptx" in cell.metadata.get('tags', {})):
            if "slide_type" in cell.metadata.get('slideshow', {}):
                if  cell.metadata.slideshow.get("slide_type", ())=="slide":
                    slide = prs.slides.add_slide(prs.slide_layouts[6])
                    latexheight=Inches(1.28)
                    if "KULeuvenSlides" in cell.get('metadata', {}):
                        if "slide_title" in cell.metadata.get('KULeuvenSlides', {}):
                            maketitle(cell,slide)
                        if "eq_vertical" in cell.metadata.get('KULeuvenSlides', {}):
                            latexheight+=Inches(cell.metadata.KULeuvenSlides["eq_vertical"])
                if  cell.metadata.slideshow.get("slide_type", ())=="slide" or cell.metadata.slideshow.get("slide_type", ())=="fragment": 
                    latexpng=find_between( "".join(cell.get('source', {})) , "$$", "$$" )
                    latexpng2=find_between( "".join(cell.get('source', {})) , "\begin{equation}", "\end{equation}" )
                    if len(latexpng2)>0:
                        latexpng=latexpng2
                    if len(latexpng)>0:
                        try:
                            pictp=slide.shapes.add_picture(io.BytesIO(latex_to_png(latexpng,backend="dvipng",scale=2)), Inches(1),latexheight) 
                            if pictp.width>prs.slide_width:
                                pictp.width=prs.slide_width
                                pictp.left=Inches(0)
                            else:
                                pictp.left=(prs.slide_width-pictp.width)//2
                            latexheight+=pictp.height+Inches(0.3)
                        except UnidentifiedImageError:
                            print("   latex error for cell number "+str(index))
    slide = prs.slides.add_slide(prs.slide_layouts[10])
    slide = prs.slides.add_slide(prs.slide_layouts[9])
    prs.save(ipath[:-6]+".pptx")