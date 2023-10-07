# Problem
Merge pdf fies with appropriate page numbers choosing option
# Solution
import PyPDF2

def combine_selected_pages(output_filename, *pdfs_and_pages):
    output_pdf = PyPDF2.PdfWriter()
    for pdf_file, page_numbers in pdfs_and_pages:
        with open(pdf_file, 'rb') as pdf:
            pdf_reader = PyPDF2.PdfReader(pdf)
            for page_num in page_numbers:
                page = pdf_reader.pages[page_num - 1]  # Page numbers are 1-indexed
                output_pdf.add_page(page)
    with open(output_filename, 'wb') as output_file:
        output_pdf.write(output_file)

if __name__ == "__main__":
    pdfs_and_pages = [
        ("document1.pdf", [1, 3]),  # Select pages 1 and 3 from document1.pdf
        ("document2.pdf", [2, 4]),  # Select pages 2 and 4 from document2.pdf
        # Add more PDFs and page numbers as needed
    ]
    output_filename = "combined_output.pdf"
    combine_selected_pages(output_filename, *pdfs_and_pages)
    print(f"Selected pages from PDFs combined and saved as '{output_filename}'")

## Changes proposed in this Pull Request :
-  `1.`<!-- transform property added to box-item on hover -->
-  `..`
