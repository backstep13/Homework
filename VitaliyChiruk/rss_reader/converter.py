import fpdf
import os


def convert_to_pdf(list_data, path):
    """
    INPUT: list_data, path
    OUTPUT: file "RSS_Reader.pdf"
    """
    app_path = os.path.dirname(__file__)
    if not os.path.exists(path):
        print(f"Error: attempt to convert news, {path} not exists. Please, enter true path")
    else:
        directory = os.path.sep.join((path, "RSS_Reader.pdf"))
        pdf = fpdf.FPDF()
        pdf.add_page()  # Add a page, font, size
        pdf.add_font("DejaVu", "", os.path.join(app_path, "DejaVuSansCondensed.ttf"), uni=True)
        pdf.set_font("DejaVu", "", 11)
        for i in list_data:
            title = i.get("title")
            date = i.get("date")
            link = i.get("link")
            description = i.get("description")
            text = str(title) + "\n" + str(date) + "\n" + str(link) + "\n" + str(description) + "\n\n\n"
            pdf.multi_cell(w=0, h=5, txt=text)
            pdf.output(directory)  # save the pdf with name .pdf


def convert_to_html(list_data, path):
    """
    INPUT: list_data, path
    OUTPUT: file "RSS_Reader.html"
    """
    directory = os.path.sep.join((path, "RSS_Reader.html"))
    header = "<!Doctype html><html><head><title>RSS-Reader</title></head><body>"
    footer = "</table></body></html>"

    with open(directory, "a") as file:
        file.write(header)

    for i in list_data:
        title = i.get("title")
        date = i.get("date")
        link = i.get("link")
        description = i.get("description")
        text = "<b>" + str(title) + "</b><br>" + str(date) + "<br>" + \
            "<a href=" + str(link) + ">" + str(link) + "</a><br>" + str(description) + "<br><br><br>"
        with open(directory, "a") as f:
            f.write(text)

    with open(directory, "a") as file:
        file.write(footer)
