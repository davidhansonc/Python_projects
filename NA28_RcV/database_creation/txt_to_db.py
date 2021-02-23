import re
import psycopg2


def verses_to_db(db_connection, path_to_file, regex_dict, bible_version):
    with open(path_to_file, 'r') as text:
        for line in text:
            line.strip()
            db_verse_insert(regex_dict, line, bible_version)


def db_verse_insert(regex_dict, verse_data, bible_version):
    sql_insert = """INSERT INTO new_testament(book, chapter, verse, {}) 
                    VALUES ({}, {}, {}, {})
                    ON CONFLICT (book, chapter, verse) DO UPDATE
                    SET {} = {};"""
    cursor = conn.cursor()
    for book_name, regex in regex_dict.items():
        if re.match(regex, verse_data):
            match = re.search(regex, verse_data)
            verse_text = match.group(4).strip().replace("'", "''")

            version_col = bible_version
            book = repr(book_name)
            chapter = repr(match.group(2))
            verse = repr(match.group(3))
            verse_for_sql = f"'{verse_text}'"

            sql = sql_insert.format(
                bible_version,
                book, 
                chapter, 
                verse, 
                verse_for_sql,
                bible_version,
                verse_for_sql
            )
            cursor.execute(sql)


def create_table(db_connection):
    cursor = conn.cursor()
    cursor.execute(open('create_nt_table.sql', 'r').read())


if __name__ == '__main__':
    rcv_txt = 'rcv.txt'
    gk_txt = './nestle1904/nestle1904.txt'
    nt_regex = {
        'Matthew': '(^M[a-z]*t[a-z]*)[ .](\d+):(\d+)(.+)',
        'Mark': '(^M[a-z]*k[a-z]*)[ .](\d+):(\d+)(.+)',
        'Luke': '(^L[a-z]*k[a-z]*)[ .](\d+):(\d+)(.+)',
        'John': '(^J[a-z]*n[a-z]*)[ .](\d+):(\d+)(.+)',
        'Acts': '(^A[a-z]*c[a-z]*)[ .](\d+):(\d+)(.+)',
        'Romans': '(^R[a-z]*m[a-z]*)[ .](\d+):(\d+)(.+)',
        'First Corinthians': '(^1C[a-z]*o[a-z]*)[ .](\d+):(\d+)(.+)',
        'Second Corinthians': '(^2C[a-z]*o[a-z]*)[ .](\d+):(\d+)(.+)',
        'Galatians': '(^G[a-z]*a[a-z]*)[ .](\d+):(\d+)(.+)',
        'Ephesians': '(^E[a-z]*p[a-z]*)[ .](\d+):(\d+)(.+)',
        'Philippians': '(^P[a-z]*)[ .](\d+):(\d+)(.+)',
        'Colossians': '(^C[a-z]*o[a-z]*)[ .](\d+):(\d+)(.+)',
        'First Thessalonians': '(^1Th[a-z]*)[ .](\d+):(\d+)(.+)',
        'Second Thessalonians': '(^2Th[a-z]*)[ .](\d+):(\d+)(.+)',
        'First Timothy': '(^1Ti[a-z]*)[ .](\d+):(\d+)(.+)',
        'Second Timothy': '(^2Ti[a-z]*)[ .](\d+):(\d+)(.+)',
        'Titus': '(^T[a-z]*t[a-z]*)[ .](\d+):(\d+)(.+)',
        'Philemon': '(^P[a-z]*m[a-z]*)[ .](\d+):(\d+)(.+)',
        'Hebrews': '(^H[a-z]*e[a-z]*)[ .](\d+):(\d+)(.+)',
        'James': '(^J[a-z]*a[a-z]*)[ .](\d+):(\d+)(.+)',
        'First Peter': '(^1P[a-z]*)[ .](\d+):(\d+)(.+)',
        'Second Peter': '(^2P[a-z]*)[ .](\d+):(\d+)(.+)',
        'First John': '(^1J[a-z]*)[ .](\d+):(\d+)(.+)',
        'Second John': '(^2J[a-z]*)[ .](\d+):(\d+)(.+)',
        'Third John': '(^3J[a-z]*)[ .](\d+):(\d+)(.+)',
        'Jude': '(^J[a-z]*d[a-z]*)[ .](\d+):(\d+)(.+)',
        'Revelation': '(^R[a-z]*v[a-z]*)[ .](\d+):(\d+)(.+)',
    }
    conn = psycopg2.connect(
        host='localhost',
        database='na28_rcv',
        user='postgres',
        password=''
    )
    conn.set_session(autocommit=True)

    create_table(conn)
    verses_to_db(conn, rcv_txt, nt_regex, 'recovery_version')
    verses_to_db(conn, gk_txt, nt_regex, 'nestle1904')