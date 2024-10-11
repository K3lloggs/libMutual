import requests
import PyPDF2


def main():
    # PDF URLs
    pdf_links = [
        "https://www.libertymutualgroup.com/about-lm/investor-relations/documents/q2-2024-earnings-release1.pdf",
        "https://www.libertymutualgroup.com/about-lm/investor-relations/documents/q1-2024-earnings-release.pdf",
        "https://www.libertymutualgroup.com/about-lm/investor-relations/documents/q3-2023-earnings-release.pdf",
        "https://www.libertymutualgroup.com/about-lm/investor-relations/documents/q2-2023-earnings-release.pdf",
        "https://www.libertymutualgroup.com/about-lm/investor-relations/documents/q1-2023-earnings-release.pdf"
    ]
 
    for idx, pdf_url in enumerate(pdf_links):
        pdf_filename = f"financial_report_{idx+1}.pdf"
        download_pdf(pdf_url, pdf_filename)



   
    file_paths = [
        "financial_report_1.pdf",
        "financial_report_2.pdf",
        "financial_report_3.pdf",
        "financial_report_4.pdf",
        "financial_report_5.pdf"
    ]

    
    compiled_text = ""


    for file_path in file_paths:

        print(f"Extracting text from: {file_path}")
        pdf_text = extract_text_from_pdf(file_path)

  
        compiled_text += f"\n\n===== Extracted Text from {file_path} =====\n\n"
        compiled_text += pdf_text



    output_file = "compiled_financial_reports.txt"
    with open(output_file, "w") as text_file:
        text_file.write(compiled_text)

    print(f"Saved compiled text to: {output_file}")

def download_pdf(url, filename):
    response = requests.get(url)

    with open(filename, 'wb') as pdf_file:
        pdf_file.write(response.content)
    print(f"Downloaded {filename}")



def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        
        reader = PyPDF2.PdfReader(file)
        all_text = ""
        
       
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            all_text += page.extract_text()
        return all_text


if __name__ == "__main__":
    main()
