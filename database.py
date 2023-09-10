import sqlite3


def insert(paper_info):
    conn = sqlite3.connect('papers.db')
    c = conn.cursor()
    print('=' * 20)
    print("Opened database successfully")
    print(paper_info)
    c.execute("INSERT INTO Paper ("
              "arxiv_id,"
              "authors,"
              "title,"
              "abstract,"
              "submit_time,"
              "comment,"
              "cite) \
          VALUES ({0})".format(str(paper_info).strip('[').strip(']')))
    conn.commit()
    print("Records created successfully")
    conn.close()
