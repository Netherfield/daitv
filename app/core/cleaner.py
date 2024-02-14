import csv
import re



# was missing 'O', 'O Convento'
art = ['A', 'I', 'O', 'Le', 'Il', 'An', 'The', 'El', 'La', "L'",'Les', 'Der', 'Das']

def article_rearrange(s:str|None) -> str | None:
    temp_t = s
    # allow None values for compatibility
    if temp_t is not None and "," in temp_t:
        parts = temp_t.split(",")
        for a in art:
            # parts 1 assumes one comma, parts -1 generic
            if parts[-1].strip().startswith(a):
                # {a}<space>{parts} not valid for apostrophe
                temp_t = f"{a} {",".join(parts[0:-1])}" if "'" not in a else f"{a}{",".join(parts[0:-1])}"
        # if len(parts) > 2:
        #     print(parts)
        #     print(temp_t)
        #     input()
    return temp_t


def cleaner(row:list[str]):
    cl_row = [row[0]]
    
    # original_pattern = re.compile(r"(?<=\()[^\(\)]+(?=\))")
    original_pattern = re.compile(r"(?<=\().+(?=\))") # to keep the double original titles
    title = row[1]
    original = original_pattern.search(title)
    titles = [title, None]
    
    if original is not None:
        original = original.group(0)
        if ") (" in original:
            original = original.replace(") (", "|")
        if "a.k.a. " in original:
            original = original.replace("a.k.a. ", "")
        elif "a.k.a." in original:
            original = original.replace("a.k.a.", "")
        ind_original = title.find("(")
        title = title[:ind_original-1]
        titles = [title, original]

    # probably more performing version but UNTESTED
    # cl_titles = [article_rearrange(titles[0]),article_rearrange(titles[1])]
    cl_titles = []
    for t in titles:
        cl_titles.append(article_rearrange(t))
    cl_row += cl_titles + [ row[2], row[3]]
    return cl_row
    


fout = open('Elenco Movies Pulito.csv', 'w', encoding='utf-8', newline='')
with open('Elenco Movies definitivo.csv', 'r', encoding='utf-8', newline='') as fp:
    reader = csv.reader(fp)
    writer = csv.writer(fout)
    titles = ['MovieID', 'Title', 'Original', 'Year', 'Genres']
    writer.writerow(titles)
    reader.__next__()
    for row in reader:
        # print(row)
        cleaned = cleaner(row)
        writer.writerow(cleaned)
fout.close()

