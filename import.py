import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine(os.getenv("postgres://gkqnaycnzoxloq:009e02b3b5400397108924bff624ddb191a1d1cff0303f5f394f58736783e8cd@ec2-174-129-29-101.compute-1.amazonaws.com:5432/decdgi6h9sh68s"))
db = scoped_session(sessionmaker(bind = engine))
def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.excute("INSERT INTO books (isbn,title,author,year) VALUES (:isbn,:title,:author,:year)",{"isbn":isbn,"title":title,"author":author,"year":year})
        print(f"Added book of isbn = {isbn} titled {title} written {author} in year {year}")
        db.commit()

if __name__=="__main__":
    main()
