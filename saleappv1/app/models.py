from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg')

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
<<<<<<< HEAD
        db.create_all()

        import hashlib
        u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
=======
        c1 = Category(name='Mobile')
        c2 = Category(name='Tablet')

        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()
>>>>>>> 01dae9c619b16595e334ffb64663443053e05f32

        # p1 = Product(name='iPhone 15', price=20000000, category_id=1,
        #              image='https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg')
        # p2 = Product(name='iPad 15', price=45000000, category_id=1,
        #              image='https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg')
        # p3 = Product(name='Galaxy S23', price=27000000, category_id=1,
        #              image='https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg')
        # p4 = Product(name='iPad Pro', price=33000000, category_id=2,
        #              image='https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg')
        # p5 = Product(name='iPhone 14', price=54000000, category_id=1,
        #              image='https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg')
        # p6 = Product(name='iPhone 13', price=20000000, category_id=2,
        #              image='https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg')
        #
        # db.session.add_all([p1, p2, p3, p4, p5, p6])
        # db.session.commit()

<<<<<<< HEAD
=======
        db.session.add_all([p1, p2, p3, p4, p5, p6])
        db.session.commit()
        # db.create_all()
>>>>>>> 01dae9c619b16595e334ffb64663443053e05f32
