import base64
import os

def decode_and_save(input_txt, output_pdf):
    with open(input_txt, 'r') as f:
        b64_data = f.read().strip()
    
    with open(output_pdf, 'wb') as f:
        f.write(base64.b64decode(b64_data))

if __name__ == "__main__":
    decode_and_save('scratch/n05_base64.txt', 'bibliography/nuevos/P05_computers_xai_analyzing_ids_2025.pdf')
    print("Success")
