import base64
import sys

def save_pdf(b64_data, output_path):
    with open(output_path, 'wb') as f:
        f.write(base64.b64decode(b64_data))

if __name__ == "__main__":
    # The base64 string is too long for arguments, so we'll read from a file or stdin
    # But for now, let's just write a script that has the data embedded or reads from a temp file.
    pass
