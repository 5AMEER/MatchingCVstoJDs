import csv
import PyPDF2, pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

file_path = "training_data.csv"


#Function to load csv data in the form of list (JD data)
def read_csv_to_list_of_lists(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file_object:
        reader_object = csv.reader(file_object)
        list_of_lists = []
        for row_list in reader_object:
            list_of_lists.append(row_list)
    return list_of_lists


CV = "CV.pdf"
CV_file = open(CV, "rb")
script = PyPDF2.PdfReader(CV_file)
pages = len(script.pages)

Script = []
with pdfplumber.open(CV_file) as pdf:
    for i in range(0,pages):
        page=pdf.pages[i]
        text=page.extract_text()
        # print(text)
        Script.append(text)


Script=''.join(Script)
CV_Clear = Script.replace("\n","")
# print(CV_Clear)


jd = read_csv_to_list_of_lists(file_path)
# print(jd[2])

for i in range(1, len(jd)):
    jd_ = [x.lower() for x in jd[i]]
    jd__ = [x.replace("\n"," ") for x in jd_]
    # print(jd__)
    jd_clean = ' '.join([str(elem) for elem in jd__])
    # print(type(jd_clean))

    Match_Test = [CV_Clear, jd_clean]

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(Match_Test)
    # print('Similarity is :',cosine_similarity(count_matrix))

    MatchPercentage = cosine_similarity(count_matrix)[0][1]*100
    MatchPercentage = round(MatchPercentage,2)
    print(f'Match Percentage for JD{i} is : {MatchPercentage}% to Requirement')