from data import db_session
from data.users import Users
from data.news import News
from data.category import Category

db_session.global_init("db/blogs.sqlite")
session = db_session.create_session()

news = session.query(News)
print(news)