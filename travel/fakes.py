from travel.extensions import db
from travel.models import User, Flight, Car, Hotel


def fake_users():
    # 管理员
    user = User(
        username='admin',
        name='管理员',
        is_admin=True
    )
    user.set_password('111')
    db.session.add(user)

    # 20个用户
    for i in range(20):
        user = User(
            username='user'+str(i+1),
            name='user'+str(i+1),
        )
        user.set_password('111')
        db.session.add(user)

    db.session.commit()


def fake_flights():
    db.session.add(Flight(from_addr='苏州', to_addr='西安', total_sites=100, avail_sites=100, price=100))
    db.session.add(Flight(from_addr='苏州', to_addr='西安', total_sites=50, avail_sites=50, price=50))
    db.session.add(Flight(from_addr='苏州', to_addr='西安', total_sites=120, avail_sites=120, price=120))

    db.session.add(Flight(from_addr='西安', to_addr='郑州', total_sites=100, avail_sites=100, price=100))
    db.session.add(Flight(from_addr='西安', to_addr='郑州', total_sites=50, avail_sites=50, price=50))
    db.session.add(Flight(from_addr='西安', to_addr='郑州', total_sites=120, avail_sites=120, price=120))

    db.session.add(Flight(from_addr='郑州', to_addr='深圳', total_sites=100, avail_sites=100, price=100))
    db.session.add(Flight(from_addr='郑州', to_addr='深圳', total_sites=50, avail_sites=50, price=50))
    db.session.add(Flight(from_addr='郑州', to_addr='深圳', total_sites=120, avail_sites=120, price=120))

    db.session.add(Flight(from_addr='苏州', to_addr='北京', total_sites=100, avail_sites=100, price=100))
    db.session.add(Flight(from_addr='苏州', to_addr='北京', total_sites=50, avail_sites=50, price=50))
    db.session.add(Flight(from_addr='苏州', to_addr='北京', total_sites=120, avail_sites=120, price=120))

    db.session.add(Flight(from_addr='北京', to_addr='深圳', total_sites=100, avail_sites=100, price=100))
    db.session.add(Flight(from_addr='北京', to_addr='深圳', total_sites=50, avail_sites=50, price=50))
    db.session.add(Flight(from_addr='北京', to_addr='深圳', total_sites=120, avail_sites=120, price=120))

    db.session.add(Flight(from_addr='深圳', to_addr='西安', total_sites=100, avail_sites=100, price=100))
    db.session.add(Flight(from_addr='深圳', to_addr='西安', total_sites=50, avail_sites=50, price=50))
    db.session.add(Flight(from_addr='深圳', to_addr='西安', total_sites=120, avail_sites=120, price=120))

    db.session.add(Flight(from_addr='西安', to_addr='成都', total_sites=100, avail_sites=100, price=100))
    db.session.add(Flight(from_addr='西安', to_addr='成都', total_sites=50, avail_sites=50, price=50))
    db.session.add(Flight(from_addr='西安', to_addr='成都', total_sites=120, avail_sites=120, price=120))

    db.session.commit()


def fake_cars():
    db.session.add(Car(location='苏州', car_type='滴滴', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='西安', car_type='滴滴', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='郑州', car_type='滴滴', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='上海', car_type='滴滴', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='深圳', car_type='滴滴', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='北京', car_type='滴滴', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='成都', car_type='滴滴', total_cars=100, avail_cars=100, price=100))

    db.session.add(Car(location='苏州', car_type='曹操出行', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='西安', car_type='曹操出行', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='郑州', car_type='曹操出行', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='上海', car_type='曹操出行', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='深圳', car_type='曹操出行', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='北京', car_type='曹操出行', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='成都', car_type='曹操出行', total_cars=100, avail_cars=100, price=100))

    db.session.add(Car(location='苏州', car_type='快的', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='西安', car_type='快的', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='郑州', car_type='快的', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='上海', car_type='快的', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='深圳', car_type='快的', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='北京', car_type='快的', total_cars=100, avail_cars=100, price=100))
    db.session.add(Car(location='成都', car_type='快的', total_cars=100, avail_cars=100, price=100))

    db.session.commit()


def fake_hotels():
    db.session.add(Hotel(location='苏州', name='如家', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='西安', name='如家', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='郑州', name='如家', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='上海', name='如家', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='深圳', name='如家', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='北京', name='如家', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='成都', name='如家', total_rooms=100, avail_rooms=100, price=100))

    db.session.add(Hotel(location='苏州', name='速8', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='西安', name='速8', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='郑州', name='速8', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='上海', name='速8', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='深圳', name='速8', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='北京', name='速8', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='成都', name='速8', total_rooms=100, avail_rooms=100, price=100))

    db.session.add(Hotel(location='苏州', name='7天', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='西安', name='7天', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='郑州', name='7天', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='上海', name='7天', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='深圳', name='7天', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='北京', name='7天', total_rooms=100, avail_rooms=100, price=100))
    db.session.add(Hotel(location='成都', name='7天', total_rooms=100, avail_rooms=100, price=100))

    db.session.commit()
