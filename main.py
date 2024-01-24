import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(folder_path, output_path):
    pdf_writer = PdfWriter()

    for item in os.listdir(folder_path):
        if item.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, item)
            pdf_reader = PdfReader(pdf_path)
            
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

    print(f'Merged PDFs into {output_path}')

# Define o caminho da pasta e o nome do arquivo PDF de saída 
folder_path = r'C:\diretorio' #preencha aqui o diretório
output_path = r'C:\diretorio\pdf_merge.pdf' #preencha aqui o diretório

# Chama a função
merge_pdfs(folder_path, output_path)
