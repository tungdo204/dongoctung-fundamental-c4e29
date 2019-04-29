from pymongo import MongoClient
from bson.objectid import ObjectId
import matplotlib.pyplot as plt

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.c4e
customers = db.customers
posts = db.posts
# my_post = [
#     {
#     'title': 'Triệu Đóa Hồng Remix',
#     'author': 'Khá Bảnh',
#     'content':'\n Vườn hồng ngày xưa đã úa! \n Teng teng téng tèng teng tèng tèng teng teng téng teng x 3.14',
# },
#     {
#     'title': 'Review',
#     'author': 'DNT',
#     'content': 'Khóa học rất hay và ý nghĩa, hãy mua vé tháng đến muộn để tiết kiệm được nhiều hơn :D'
# }]
# posts.insert_many(my_post)

event = customers.find({'ref':'events'})
e=event.count()
ad = customers.find({'ref':'ads'})
a=ad.count()
wom = customers.find({'ref':'wom'})
w=wom.count()

labels =  'Events','Advertisement','Word of Mouth'
sizes = [e,a,w]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()


