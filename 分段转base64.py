import base64

def convert_pdf_to_base64(pdf_path, output_path, chunk_size=8192):
    with open(pdf_path, 'rb') as pdf_file:
        with open(output_path, 'wb') as output_file:
            while True:
                chunk = pdf_file.read(chunk_size)
                if not chunk:
                    break
                encoded_chunk = base64.b64encode(chunk)
                output_file.write(encoded_chunk)

# 使用方法
pdf_path = "./说明文件/征信模板.pdf"
output_path = "./data/征信模板_base64_encode.txt"
convert_pdf_to_base64(pdf_path, output_path)
print("finish")

###########################################################################

import base64

def convert_base64_to_pdf(input_path, output_path, chunk_size=8192):
    with open(input_path, 'rb') as input_file:
        with open(output_path, 'wb') as pdf_file:
            while True:
                chunk = input_file.read(chunk_size)
                if not chunk:
                    break
                decoded_chunk = base64.b64decode(chunk)
                pdf_file.write(decoded_chunk)

# 使用方法
input_path = "./data/征信模板_base64_encode.txt"  # 这应该是之前Base64编码的文本文件
output_path = "./data/征信模板_from_base64.pdf"
convert_base64_to_pdf(input_path, output_path)
print("finish")