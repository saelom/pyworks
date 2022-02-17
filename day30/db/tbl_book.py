# 도서 db 만들기
import sqlite3

def getconn():
    #데이터베이스 생성 및 접속
    conn = sqlite3.connect("./book.db")
    return conn


def create_table():
    # 테이블 생성
    con = getconn()
    cursur = con.cursor()
    sql = """
        CREATE TABLE book( 
            book_no integer PRIMARY KEY AUTOINCREMENT,
            title text NOT NULL,
            publisher text NOT NULL,
            page    integer                   
        );
    """
    cursur.execute(sql)
    con.commit()
    con.close()

def insert_book():
    # 도서 추가
    con = getconn()
    cursor = con.cursor()
    sql = "INSERT INTO book(title , publisher, page) VALUES (?, ?, ?)"
    # book_no는 자동이므로 입력하면 안됨
    cursor.execute(sql, ('점프 투 파이썬', '박응용', 350))
    con.commit()
    con.close()

def select_book():
    # 도서 전체 검색
    con = getconn()
    cursor = con.cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    for i in rs:
        print(i)
    con.close()

def select_one():
    # 특정 도서 검색
    con = getconn()
    cursor = con.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursor.execute(sql, (2,))   # 튜플 1개일때 콤마 붙임
    rs = cursor.fetchone()
    print(rs)
    con.close()

def update_book():
    con = getconn()
    cursor = con.cursor()
    sql = "UPDATE book SET page = ? WHERE book_no = ?"
    cursor.execute(sql, (400, 2))
    con.commit()
    con.close()

def delete_book():
    # 도서 삭제
    con = getconn()
    cursor = con.cursor()
    sql = "DELETE FROM book WHERE book_no = ?"
    cursor.execute(sql, (1, ))
    con.commit()
    con.close()

if __name__ =="__main__":
    # conn = getconn()
    # print(conn, "연결됨")
    # create_table()
    # insert_book()
    # select_one()
    # update_book()
    delete_book()
    select_book()



