# Copyright (c) 2023 Jules aka Netherfield
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import csv
import app.utils.prequel as prequel

def batch(l:list, sample:int):
    """
    Processes a splicable object in chunks of sample size
    until only the tail is left
    """
    while l:
        # prova a tornare il primo sample e riassegna a l il restante
        try:
          ret = l[:sample]
          yield ret
          l = l[sample:]
        # se l'indice e' fuori dal range allora ritorna tutta la l rimanente
        except IndexError:
          return l
    return None


generelookup = dict()
gen_id = 1

def main():
    
    def getgenres(conn, genre) -> list[list[int,int]]:
        ret = []
        global gen_id
        global generelookup
        for g in genre:
            try:
                ret.append(generelookup[g])
            except:
                generelookup[g] = gen_id
                genrequery = f"""INSERT INTO `genres` VALUES ({str(gen_id)}, "{g}")"""
                # print("Adding genre via query")
                # print(genrequery)
                prequel.execute_query(conn, genrequery)
                ret.append(gen_id)
                gen_id += 1
                # print(generelookup)
        return ret
            
    conn = prequel.create_db_connection('localhost', 'root', '', 'daitv')
    with open("load/Elenco Movies Pulito.csv", "r", encoding="utf-8", newline="") as fp:
        reader = csv.reader(fp)
        reader.__next__()

        
        movielist = list(reader)
        for lines in batch(movielist, 100):
            moviebatch = []
            moviegenrebatch = []
            for id,title,original,year,genre in lines:
                id = int(id)
                year = int(year)
                # print(lines)
                if "|" in genre:
                    genre = genre.split("|")
                else:
                    genre = [genre]
                # print(genre)
                moviebatch += [[str(id), title, original, year]]
                moviegenrebatch += [ [str(id), str(genreid)] for genreid in getgenres(conn, genre)]
                # print(moviegenrebatch)
                # input("these are the genres")
            moviequery ="""INSERT INTO `films` VALUES (%s, %s, %s, %s)"""
            moviegenrequery ="""INSERT INTO `moviegenre` (`MovieID`, `GenreID`) VALUES (%s, %s)"""
            # for m in moviebatch:
            #     print(m)
            #     for i in range(len(moviegenrebatch)):
            #         if(m[0] == moviegenrebatch[i][0]):
            #             print(moviegenrebatch[i])
            prequel.execute_insert(conn, moviequery, moviebatch)
            prequel.execute_insert(conn, moviegenrequery, moviegenrebatch)
            print("Done 100 queries")
        print("done")



        




            










if __name__ == "__main__":
    main()


