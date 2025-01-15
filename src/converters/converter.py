import pdfkit
import csv
from docx import Document
from PIL import Image
import pydub
from moviepy.video.io.VideoFileClip import VideoFileClip
# import pandas as pd  # For Excel conversions
from pptx import Presentation  # For PowerPoint conversions
from odf.opendocument import OpenDocumentText, OpenDocumentSpreadsheet, OpenDocumentPresentation  # For ODT, ODS, ODP conversions
from pdf2image import convert_from_path  # For converting PDF to images
import img2pdf  # For converting images to PDF
import os

class FileConverter:
    def __init__(self):
        self.supported_conversions = {
            'doc': ['pdf', 'txt', 'docx'],
            'docx': ['pdf', 'txt', 'doc'],
            'pdf': ['txt', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
            'txt': ['pdf', 'doc', 'docx'],
            'rtf': ['pdf', 'txt', 'doc', 'docx'],
            'odt': ['pdf', 'txt', 'doc', 'docx'],
            # 'xls': ['pdf', 'csv', 'xlsx'],
            # 'xlsx': ['pdf', 'csv', 'xls'],
            # 'ods': ['pdf', 'csv', 'xls', 'xlsx'],
            'ppt': ['pdf', 'pptx'],
            'pptx': ['pdf', 'ppt'],
            'odp': ['pdf', 'ppt', 'pptx'],
            'jpg': ['png', 'gif', 'bmp', 'tiff', 'pdf'],
            'jpeg': ['png', 'gif', 'bmp', 'tiff', 'pdf'],
            'png': ['jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'pdf'],
            'gif': ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'pdf'],
            'bmp': ['jpg', 'jpeg', 'png', 'gif', 'tiff', 'pdf'],
            'tiff': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'pdf'],
            'mp3': ['wav', 'aac', 'ogg'],
            'wav': ['mp3', 'aac', 'ogg'],
            'aac': ['mp3', 'wav', 'ogg'],
            'ogg': ['mp3', 'wav', 'aac'],
            'mp4': ['avi', 'mov', 'mkv', 'wmv', 'mp3'],
            'avi': ['mp4', 'mov', 'mkv', 'wmv', 'mp3'],
            'mov': ['mp4', 'avi', 'mkv', 'wmv', 'mp3'],
            'mkv': ['mp4', 'avi', 'mov', 'wmv', 'mp3'],
            'wmv': ['mp4', 'avi', 'mov', 'mkv', 'mp3'],
            'html': ['htm', 'pdf'],
            'htm': ['html', 'pdf'],
            'css': ['pdf'],
            'js': ['pdf']
      }

    def is_conversion_supported(self, input_format, output_format):
        """Check if the conversion from input_format to output_format is supported."""
        return output_format in self.supported_conversions.get(input_format, [])

    def convert_to_pdf(self, input_file, output_file):
        # Logic to convert input_file to PDF format
        pdfkit.from_file(input_file, output_file)

    def convert_to_txt(self, input_file, output_file):
        # Logic to convert input_file to TXT format
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write(infile.read())

    def convert_to_csv(self, input_file, output_file):
        # Logic to convert input_file to CSV format
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                writer.writerow(row)

    def convert_to_docx(self, input_file, output_file):
        doc = Document(input_file)
        doc.save(output_file)

    def convert_to_rtf(self, input_file, output_file):
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write(infile.read())

    def convert_to_odt(self, input_file, output_file):
        # Logic to convert input_file to ODT format
        textdoc = OpenDocumentText()
        with open(input_file, 'r') as infile:
            textdoc.text.addElement(textdoc.text.P(text=infile.read()))
        textdoc.save(output_file)

    # def convert_to_xlsx(self, input_file, output_file):
    #     # Logic to convert input_file to XLSX format
    #     df = pd.read_csv(input_file)
    #     df.to_excel(output_file, index=False)

    # def convert_to_ods(self, input_file, output_file):
    #     # Logic to convert input_file to ODS format
    #     df = pd.read_csv(input_file)
    #     ods = OpenDocumentSpreadsheet()
    #     table = ods.spreadsheet.Table(name="Sheet1")
    #     ods.spreadsheet.addElement(table)
    #     for row in df.values:
    #         tr = ods.spreadsheet.TableRow()
    #         table.addElement(tr)
    #         for cell in row:
    #             tc = ods.spreadsheet.TableCell()
    #             tr.addElement(tc)
    #             tc.addElement(ods.text.P(text=str(cell)))
    #     ods.save(output_file)

    def convert_to_pptx(self, input_file, output_file):
        # Logic to convert input_file to PPTX format
        prs = Presentation(input_file)
        prs.save(output_file)

    def convert_to_odp(self, input_file, output_file):
        # Logic to convert input_file to ODP format
        presentation = OpenDocumentPresentation()
        with open(input_file, 'r') as infile:
            slide = presentation.presentation.Slide()
            presentation.presentation.addElement(slide)
            slide.addElement(presentation.text.P(text=infile.read()))
        presentation.save(output_file)

    def convert_to_jpg(self, input_file, output_file):
        image = Image.open(input_file)
        image.save(output_file, 'JPEG')

    def convert_to_png(self, input_file, output_file):
        image = Image.open(input_file)
        image.save(output_file, 'PNG')

    def convert_to_gif(self, input_file, output_file):
        image = Image.open(input_file)
        image.save(output_file, 'GIF')

    def convert_to_bmp(self, input_file, output_file):
        image = Image.open(input_file)
        image.save(output_file, 'BMP')

    def convert_to_tiff(self, input_file, output_file):
        image = Image.open(input_file)
        image.save(output_file, 'TIFF')

    def convert_to_mp3(self, input_file, output_file):
        audio = pydub.AudioSegment.from_file(input_file)
        audio.export(output_file, format='mp3')

    def convert_to_wav(self, input_file, output_file):
        audio = pydub.AudioSegment.from_file(input_file)
        audio.export(output_file, format='wav')

    def convert_to_aac(self, input_file, output_file):
        audio = pydub.AudioSegment.from_file(input_file)
        audio.export(output_file, format='aac')

    def convert_to_ogg(self, input_file, output_file):
        audio = pydub.AudioSegment.from_file(input_file)
        audio.export(output_file, format='ogg')

    def convert_to_mp4(self, input_file, output_file):
        video = VideoFileClip(input_file)
        video.write_videofile(output_file)

    def convert_to_avi(self, input_file, output_file):
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='png')

    def convert_to_mov(self, input_file, output_file):
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264')

    def convert_to_mkv(self, input_file, output_file):
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264')

    def convert_to_wmv(self, input_file, output_file):
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='wmv')

    def convert_to_html(self, input_file, output_file):
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write(infile.read())

    def convert_to_css(self, input_file, output_file):
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write(infile.read())

    def convert_to_js(self, input_file, output_file):
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write(infile.read())

    def convert_pdf_to_image(self, input_file, output_file, image_format):
        # Convert PDF to images
        poppler_path = r"C:\Program Files\poppler-24.08.0\Library\bin"  # Ensure this path matches your system path
        images = convert_from_path(input_file, poppler_path=poppler_path)
        for i, image in enumerate(images):
            image.save(f"{output_file}_{i}.{image_format}", image_format.upper())

    def convert_image_to_pdf(self, input_file, output_file):
        # Convert images to PDF
        if isinstance(input_file, list):
            with open(output_file, "wb") as f:
                f.write(img2pdf.convert(input_file))
        else:
            with open(output_file, "wb") as f:
                f.write(img2pdf.convert([input_file]))
