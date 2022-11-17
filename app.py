from flask import Flask,render_template,request
import PyPDF2
from flask import send_file
app=Flask(__name__)

@app.route('/')

def index():
    # return "hello world"
    return render_template("index.html")

@app.route('/pdf',methods=["POST",'GET'])

def index1():
    if request.method=="POST":
        print(request.form.get("content"),request.form.get("file"))
        file = request.files["file"]
        print(file)
        print(file.save("abcc.pdf"))

        pdf_in = open('abcc.pdf', 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_in)
        pdf_writer = PyPDF2.PdfFileWriter()

        number=int(request.form.get("page_number"))
        angle=int(request.form.get("angle"))

        # print(number,angle)

        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            if pagenum == number-1:
                page.rotateClockwise(angle)
            pdf_writer.addPage(page)
        pdf_out = open('rotated.pdf', 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        path = "rotated.pdf"
        return send_file(path, as_attachment=True)
        # return "Done"
    else:

        return "GET"

if __name__=="__main__":
    app.run(debug=True)
