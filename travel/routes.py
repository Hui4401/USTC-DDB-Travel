from flask import Flask, request, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from travel.forms import *
from travel.models import *
from travel.utils import redirect_back


def init_routes(app: Flask):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            remember = form.remember.data

            user = User.query.filter_by(username=username).first()
            if not user or not user.check_password(password):
                flash('用户名或密码错误', 'warning')
                return redirect(url_for('login'))

            login_user(user, remember)
            flash('登录成功', 'success')
            return redirect_back()

        return render_template('login.html', form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            name = form.name.data

            user = User.query.filter_by(username=username).first()
            if user:
                flash('该用户名已存在', 'warning')
                return redirect(url_for('register'))

            user = User(
                username=username,
                name=name
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('注册成功', 'success')
            return redirect(url_for('login'))

        return render_template('register.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('已退出', 'info')
        return redirect(url_for('index'))

    @app.route('/reservations')
    @login_required
    def reservations():
        res = Reservation.query.filter_by(username=current_user.username).order_by(Reservation.res_time.desc()).all()
        return render_template('reservations.html', reservations=res)

    @app.route('/search_flight', methods=['GET', 'POST'])
    def search_flight():
        form = SearchFlightForm()
        if form.validate_on_submit():
            from_addr = form.from_addr.data
            to_addr = form.to_addr.data

            flights = Flight.query.filter_by(from_addr=from_addr, to_addr=to_addr).all()
            return render_template('search_flight.html', form=form, flights=flights)

        return render_template('search_flight.html', form=form)

    @app.route('/search_car', methods=['GET', 'POST'])
    def search_car():
        form = SearchCarForm()
        if form.validate_on_submit():
            location = form.location.data

            cars = Car.query.filter_by(location=location).all()
            return render_template('search_car.html', form=form, cars=cars)

        return render_template('search_car.html', form=form)

    @app.route('/search_hotel', methods=['GET', 'POST'])
    def search_hotel():
        form = SearchHotelForm()
        if form.validate_on_submit():
            location = form.location.data

            hotels = Hotel.query.filter_by(location=location).all()
            return render_template('search_hotel.html', form=form, hotels=hotels)

        return render_template('search_hotel.html', form=form)

    @app.route('/res_flight', methods=['GET', 'POST'])
    @login_required
    def res_flight():
        from_addr = request.args.get('from_addr')
        to_addr = request.args.get('to_addr')
        form = SearchFlightForm()
        if form.validate_on_submit():
            from_addr = form.from_addr.data
            to_addr = form.to_addr.data

            flights = Flight.query.filter_by(from_addr=from_addr, to_addr=to_addr).all()
            return render_template('res_flight.html', form=form, flights=flights)

        if from_addr and to_addr:
            flights = Flight.query.filter_by(from_addr=from_addr, to_addr=to_addr).all()
            return render_template('res_flight.html', form=form, flights=flights)
        return render_template('res_flight.html', form=form)

    @app.route('/res_flight_do')
    @login_required
    def res_flight_do():
        flight_id = request.args.get('id')
        from_addr = request.args.get('from_addr')
        to_addr = request.args.get('to_addr')

        flight = Flight.query.get(flight_id)
        if flight.avail_sites < 1:
            flash('座位数不足!', 'warning')
        else:
            res_flight_model = ResFlight(username=current_user.username, flight_id=flight_id)
            db.session.add(res_flight_model)
            db.session.flush()
            reservation = Reservation(username=current_user.username, res_type='航班', res_id=res_flight_model.id)
            db.session.add(reservation)
            flight.avail_sites -= 1
            db.session.commit()
            flash('预订成功', 'success')
        return redirect(url_for('res_flight')+'?from_addr='+from_addr+'&to_addr='+to_addr)

    @app.route('/res_car', methods=['GET', 'POST'])
    @login_required
    def res_car():
        location = request.args.get('location')
        form = SearchCarForm()
        if form.validate_on_submit():
            location = form.location.data

            cars = Car.query.filter_by(location=location).all()
            return render_template('res_car.html', form=form, cars=cars)

        if location:
            cars = Car.query.filter_by(location=location).all()
            return render_template('res_car.html', form=form, cars=cars)
        return render_template('res_car.html', form=form)

    @app.route('/res_car_do')
    @login_required
    def res_car_do():
        location = request.args.get('location')
        car_type = request.args.get('car_type')

        car = Car.query.filter_by(location=location, car_type=car_type).first()
        if car.avail_cars < 1:
            flash('出租车数不足!', 'warning')
        else:
            res_car_model = ResCar(username=current_user.username, car_location=location, car_type=car_type)
            db.session.add(res_car_model)
            db.session.flush()
            reservation = Reservation(username=current_user.username, res_type='出租车', res_id=res_car_model.id)
            db.session.add(reservation)
            car.avail_cars -= 1
            db.session.commit()
            flash('预订成功', 'success')
        return redirect(url_for('res_car')+'?location='+location)

    @app.route('/res_hotel', methods=['GET', 'POST'])
    @login_required
    def res_hotel():
        location = request.args.get('location')
        form = SearchHotelForm()
        if form.validate_on_submit():
            location = form.location.data

            hotels = Hotel.query.filter_by(location=location).all()
            return render_template('res_hotel.html', form=form, hotels=hotels)

        if location:
            hotels = Hotel.query.filter_by(location=location).all()
            return render_template('res_hotel.html', form=form, hotels=hotels)
        return render_template('res_hotel.html', form=form)

    @app.route('/res_hotel_do')
    @login_required
    def res_hotel_do():
        location = request.args.get('location')
        name = request.args.get('name')

        hotel = Hotel.query.filter_by(location=location, name=name).first()
        if hotel.avail_rooms < 1:
            flash('房间数不足!', 'warning')
        else:
            res_hotel_model = ResHotel(username=current_user.username, hotel_location=location, hotel_name=name)
            db.session.add(res_hotel_model)
            db.session.flush()
            reservation = Reservation(username=current_user.username, res_type='宾馆', res_id=res_hotel_model.id)
            db.session.add(reservation)
            hotel.avail_rooms -= 1
            db.session.commit()
            flash('预订成功', 'success')
        return redirect(url_for('res_hotel')+'?location='+location)

    @app.route('/manage_flight', methods=['GET', 'POST'])
    @login_required
    def manage_flight():
        form = SearchFlightForm()
        if form.validate_on_submit():
            from_addr = form.from_addr.data
            to_addr = form.to_addr.data

            flights = Flight.query.filter_by(from_addr=from_addr, to_addr=to_addr).all()
            return render_template('manage_flight.html', form=form, flights=flights)

        return render_template('manage_flight.html', form=form)

    @app.route('/manage_car', methods=['GET', 'POST'])
    @login_required
    def manage_car():
        form = SearchCarForm()
        if form.validate_on_submit():
            location = form.location.data

            cars = Car.query.filter_by(location=location).all()
            return render_template('manage_car.html', form=form, cars=cars)

        return render_template('manage_car.html', form=form)

    @app.route('/manage_hotel', methods=['GET', 'POST'])
    @login_required
    def manage_hotel():
        form = SearchHotelForm()
        if form.validate_on_submit():
            location = form.location.data

            hotels = Hotel.query.filter_by(location=location).all()
            return render_template('manage_hotel.html', form=form, hotels=hotels)

        return render_template('manage_hotel.html', form=form)

    @app.route('/add_flight', methods=['GET', 'POST'])
    @login_required
    def add_flight():
        form = AddFlightForm()
        if form.validate_on_submit():
            from_addr = form.from_addr.data
            to_addr = form.to_addr.data
            total_sites = form.total_sites.data
            price = form.price.data

            flight = Flight(from_addr=from_addr, to_addr=to_addr, total_sites=total_sites, avail_sites=total_sites, price=price)
            db.session.add(flight)
            db.session.flush()
            flash('添加成功，航班号：'+str(flight.id), 'success')
            db.session.commit()

        return render_template('add_flight.html', form=form)

    @app.route('/add_car', methods=['GET', 'POST'])
    @login_required
    def add_car():
        form = AddCarForm()
        if form.validate_on_submit():
            location = form.location.data
            car_type = form.car_type.data
            total_cars = form.total_cars.data
            price = form.price.data

            car = Car.query.filter_by(location=location, car_type=car_type).first()
            if car:
                flash('该地区已有该类型出租车数据，您可尝试修改', 'warning')
                return render_template('add_car.html', form=form)
            car = Car(location=location, car_type=car_type, total_cars=total_cars, avail_cars=total_cars, price=price)
            db.session.add(car)
            db.session.commit()
            flash('添加成功', 'success')

        return render_template('add_car.html', form=form)

    @app.route('/add_hotel', methods=['GET', 'POST'])
    @login_required
    def add_hotel():
        form = AddHotelForm()
        if form.validate_on_submit():
            location = form.location.data
            name = form.name.data
            total_rooms = form.total_rooms.data
            price = form.price.data

            hotel = Hotel.query.filter_by(location=location, name=name).first()
            if hotel:
                flash('该地区已存在该宾馆，您可尝试修改', 'warning')
                return render_template('add_hotel.html', form=form)
            hotel = Hotel(location=location, name=name, total_rooms=total_rooms, avail_rooms=total_rooms, price=price)
            db.session.add(hotel)
            db.session.commit()
            flash('添加成功', 'success')

        return render_template('add_hotel.html', form=form)

    @app.route('/edit_flight', methods=['GET', 'POST'])
    @login_required
    def edit_flight():
        flight_id = request.args.get('id')
        flight = Flight.query.get(flight_id)
        form = EditFlightForm()
        if form.validate_on_submit():
            total_sites = form.total_sites.data
            price = form.price.data
            if total_sites < flight.total_sites:
                sub = flight.total_sites - total_sites
                if sub > flight.avail_sites:
                    flash('减少的座位数不能大于当前可用座位数', 'warning')
                    return render_template('edit_flight.html', form=form, flight=flight)
            add = total_sites - flight.total_sites
            flight.avail_sites += add
            flight.total_sites = total_sites
            flight.price = price
            db.session.commit()
            flash('更新成功', 'success')
            flights = Flight.query.filter_by(from_addr=flight.from_addr, to_addr=flight.to_addr).all()
            return render_template('manage_flight.html', form=SearchFlightForm(), flights=flights)
        return render_template('edit_flight.html', form=form, flight=flight)

    @app.route('/edit_car', methods=['GET', 'POST'])
    @login_required
    def edit_car():
        location = request.args.get('location')
        car_type = request.args.get('car_type')
        car = Car.query.filter_by(location=location, car_type=car_type).first()
        form = EditCarForm()
        if form.validate_on_submit():
            total_cars = form.total_cars.data
            price = form.price.data
            if total_cars < car.total_cars:
                sub = car.total_cars - total_cars
                if sub > car.avail_cars:
                    flash('减少的出租车数不能大于当前可用出租车数', 'warning')
                    return render_template('edit_car.html', form=form, car=car)
            add = total_cars - car.total_cars
            car.avail_cars += add
            car.total_cars = total_cars
            car.price = price
            db.session.commit()
            flash('更新成功', 'success')
            cars = Car.query.filter_by(location=car.location, car_type=car.car_type).all()
            return render_template('manage_car.html', form=SearchCarForm(), cars=cars)
        return render_template('edit_car.html', form=form, car=car)

    @app.route('/edit_hotel', methods=['GET', 'POST'])
    @login_required
    def edit_hotel():
        location = request.args.get('location')
        name = request.args.get('name')
        hotel = Hotel.query.filter_by(location=location, name=name).first()
        form = EditHotelForm()
        if form.validate_on_submit():
            total_rooms = form.total_rooms.data
            price = form.price.data
            if total_rooms < hotel.total_rooms:
                sub = hotel.total_rooms - total_rooms
                if sub > hotel.avail_rooms:
                    flash('减少的房间数不能大于当前可用房间数', 'warning')
                    return render_template('edit_hotel.html', form=form, hotel=hotel)
            add = total_rooms - hotel.total_rooms
            hotel.avail_rooms += add
            hotel.total_rooms = total_rooms
            hotel.price = price
            db.session.commit()
            flash('更新成功', 'success')
            hotels = Hotel.query.filter_by(location=hotel.location, name=hotel.name).all()
            return render_template('manage_hotel.html', form=SearchHotelForm(), hotels=hotels)
        return render_template('edit_hotel.html', form=form, hotel=hotel)

    @app.route('/manage_user', methods=['GET', 'POST'])
    @login_required
    def manage_user():
        form = SearchUserForm()
        if form.validate_on_submit():
            username = form.username.data

            users = User.query.filter_by(username=username).all()
            return render_template('manage_user.html', form=form, users=users)

        return render_template('manage_user.html', form=form)

    @app.route('/edit_user', methods=['GET', 'POST'])
    @login_required
    def edit_user():
        username = request.args.get('username')
        user = User.query.filter_by(username=username).first()
        form = EditUserForm()
        if form.validate_on_submit():
            name = form.name.data
            user.name = name
            db.session.commit()
            flash('更新成功', 'success')
            users = User.query.filter_by(username=user.username).all()
            return render_template('manage_user.html', form=SearchUserForm(), users=users)
        return render_template('edit_user.html', form=form, user=user)

    @app.route('/travel_route', methods=['GET', 'POST'])
    @login_required
    def travel_route():
        username = request.args.get('username')
        user = User.query.filter_by(username=username).first()
        reservations = ResFlight.query.filter_by(username=user.username).all()
        routes = []
        if reservations:
            flight_id0 = reservations[0].flight_id
            flight0 = Flight.query.get(flight_id0)
            routes.append(flight0.from_addr)
            routes.append(flight0.to_addr)
            for reservation in reservations[1:]:
                flight_id = reservation.flight_id
                flight = Flight.query.get(flight_id)
                if flight.from_addr == routes[-1]:
                    routes.append(flight.to_addr)
        routes = ' -> '.join(routes)
        return render_template('travel_route.html', user=user, routes=routes)


