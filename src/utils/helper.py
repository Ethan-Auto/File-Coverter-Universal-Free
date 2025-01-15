def validate_file_format(file_name, supported_formats):
    """Check if the file format is supported."""
    return file_name.split('.')[-1].lower() in supported_formats

def get_supported_formats():
    """Return a list of supported file formats for conversion."""
    return [
        'pdf', 'txt', 'csv', 'doc', 'docx', 'rtf', 'odt', 'xls', 'xlsx', 'ods',
        'ppt', 'pptx', 'odp', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff',
        'mp3', 'wav', 'aac', 'ogg', 'mp4', 'avi', 'mov', 'mkv', 'wmv',
        'html', 'htm', 'css', 'js'
    ]