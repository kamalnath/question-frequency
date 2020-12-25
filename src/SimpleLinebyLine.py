import PyPDF4
import re
import io

start_regex = r"([\d])\."
reg = r"([ \d+\d ]+)"
question_dict ={}
for i in range(1,4):
    pdfFileObj = open(r'MPC-002 ('+str(i)+').PDF', 'rb')
    #pdfFileObj = open(r'MPC-002 (2).PDF', 'rb')
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
    pages = pdfReader.numPages

    for i in range(pages):
        pageObj = pdfReader.getPage(i)
        pages_text = pageObj.extractText()
        start_flag = False;
        question_found = ""
        for line in io.StringIO(pages_text):
            line = line.replace("  \n", "").strip()
            # print(" line {}",line)
            if re.search(start_regex, line):
                # print("starting found");
                question_found = question_found + " " + line
                start_flag = True;
                continue
            if start_flag:
                question_found = question_found + " " + line
                if line.endswith('.'):
                    question_found = question_found[question_found.find(".") + 1:].strip()
                    strreplace = ''.join(re.findall(reg, question_found)).strip()
                    question_found=question_found.replace(strreplace, "")

                    print(question_found)
                    if question_found in question_dict:
                        count = question_dict[question_found]+1
                        question_dict[question_found] = count
                        #print(question_found,count)
                    else:
                        question_dict[question_found]=1

                    question_found = ""
                    start_flag = False

