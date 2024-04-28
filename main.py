from pypdf import PdfWriter, PdfReader
import os


def read_raw_md_file(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        # root 是当前遍历的目录路径（字符串类型）。
        # dirs 是一个包含当前目录下所有子目录的列表（字符串类型的列表）。
        # files 是一个包含当前目录下所有文件的列表（字符串类型的列表）。
        for file in files:
            if '.pdf' in file:  # 只读取包含课程名的md文件
                add_water_marker(input_dir, output_dir, file)
                print(file+'已处理完。')


def add_water_marker(input_dir, output_dir, pdf_file):
    writer = PdfWriter(clone_from=str(os.path.join(input_dir, pdf_file)))
    for page in writer.pages:  # 给每一页添加水印
        # 这里设置为True是因为无法保证原始文档pdf是背景透明的，
        # 所以必须把水印设为透明背景然后盖在原始pdf上方。
        page.merge_page(stamp, over=True)
    # 输出的文件名与原始文件名相同
    writer.write(str(os.path.join(output_dir, pdf_file)))


# 记住作为水印的pdf背景一定要是透明的！
# 如果用ppt制作pdf的话：PPT→设置背景格式→纯色填充→透明度100%
stamp = PdfReader("water_marker.pdf").pages[0]

input_pdf_dir = 'input_pdf'
output_pdf_dir = 'output_pdf'

if __name__ == '__main__':
    read_raw_md_file(input_pdf_dir, output_pdf_dir)
