# File Conversion Application

This project is a file conversion application that allows users to convert files between different formats. The application is designed to be user-friendly and will feature a graphical user interface (GUI) for easy interaction.

## Project Structure

```
file-conversion-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── converters
│   │   └── converter.py      # Contains conversion logic
│   ├── ui
│   │   └── main_window.py     # User interface components
│   └── utils
│       └── helper.py         # Utility functions for file handling
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Features

- Convert files to various formats.
- User-friendly GUI for selecting files and initiating conversions.
- Utility functions for validating file formats and handling file operations.

## Supported File Types

- **Input Formats**:
  - DOC, DOCX - Microsoft Word documents
  - PDF - Portable Document Format
  - TXT - Plain text files
  - RTF - Rich Text Format
  - ODT - OpenDocument Text
  - XLS, XLSX - Microsoft Excel spreadsheets
  - ODS - OpenDocument Spreadsheet
  - PPT, PPTX - Microsoft PowerPoint presentations
  - ODP - OpenDocument Presentation
  - JPG, JPEG - JPEG images
  - PNG - Portable Network Graphics
  - GIF - Graphics Interchange Format
  - BMP - Bitmap image file
  - TIFF - Tagged Image File Format
  - MP3 - MPEG Audio Layer 3
  - WAV - Waveform Audio File Format
  - AAC - Advanced Audio Coding
  - OGG - Ogg Vorbis
  - MP4 - MPEG-4 Part 14
  - AVI - Audio Video Interleave
  - MOV - QuickTime File Format
  - MKV - Matroska Video
  - WMV - Windows Media Video
  - HTML, HTM - Hypertext Markup Language
  - CSS - Cascading Style Sheets
  - JS - JavaScript

- **Output Formats**:
  - DOC, DOCX - Microsoft Word documents
  - PDF - Portable Document Format
  - TXT - Plain text files
  - RTF - Rich Text Format
  - ODT - OpenDocument Text
  - XLS, XLSX - Microsoft Excel spreadsheets
  - ODS - OpenDocument Spreadsheet
  - PPT, PPTX - Microsoft PowerPoint presentations
  - ODP - OpenDocument Presentation
  - JPG, JPEG - JPEG images
  - PNG - Portable Network Graphics
  - GIF - Graphics Interchange Format
  - BMP - Bitmap image file
  - TIFF - Tagged Image File Format
  - MP3 - MPEG Audio Layer 3
  - WAV - Waveform Audio File Format
  - AAC - Advanced Audio Coding
  - OGG - Ogg Vorbis
  - MP4 - MPEG-4 Part 14
  - AVI - Audio Video Interleave
  - MOV - QuickTime File Format
  - MKV - Matroska Video
  - WMV - Windows Media Video
  - HTML, HTM - Hypertext Markup Language
  - CSS - Cascading Style Sheets
  - JS - JavaScript

## Prerequisites

Before running the application, ensure that the following dependencies are installed and added to your system path:

1. **ffmpeg**: Download and install from [ffmpeg.org](https://ffmpeg.org/download.html).
2. **poppler**: Download and install from [poppler.freedesktop.org](https://poppler.freedesktop.org/).

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd file-conversion-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Future Enhancements

- Develop an advanced GUI with additional features and improved user experience.
- Implement more file formats for conversion and additional functionalities.

## Creator Info
My name is Ethan. I made this so that I can use it, but I figure other people can too. Cheers. 

## License

This project is licensed under the MIT License.