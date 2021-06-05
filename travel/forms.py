from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 128)])
    name = StringField('姓名', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('注册')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField('保持登录状态')
    submit = SubmitField('登录')


class SearchFlightForm(FlaskForm):
    from_addr = StringField('出发地', validators=[DataRequired(), Length(1, 64)])
    to_addr = StringField('目的地', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('查询')


class SearchCarForm(FlaskForm):
    location = StringField('位置', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('查询')


class SearchHotelForm(FlaskForm):
    location = StringField('位置', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('查询')


class AddFlightForm(FlaskForm):
    from_addr = StringField('出发地', validators=[DataRequired(), Length(1, 64)])
    to_addr = StringField('目的地', validators=[DataRequired(), Length(1, 64)])
    total_sites = IntegerField('座位数', validators=[DataRequired()])
    price = IntegerField('价格', validators=[DataRequired()])
    submit = SubmitField('添加')


class AddCarForm(FlaskForm):
    location = StringField('位置', validators=[DataRequired(), Length(1, 64)])
    car_type = StringField('出租车类型', validators=[DataRequired(), Length(1, 64)])
    total_cars = IntegerField('出租车数', validators=[DataRequired()])
    price = IntegerField('价格', validators=[DataRequired()])
    submit = SubmitField('添加')


class AddHotelForm(FlaskForm):
    location = StringField('位置', validators=[DataRequired(), Length(1, 64)])
    name = StringField('宾馆名称', validators=[DataRequired(), Length(1, 64)])
    total_rooms = IntegerField('房间数', validators=[DataRequired()])
    price = IntegerField('价格', validators=[DataRequired()])
    submit = SubmitField('添加')


class EditFlightForm(FlaskForm):
    total_sites = IntegerField('总座位数', validators=[DataRequired()])
    price = IntegerField('价格', validators=[DataRequired()])
    submit = SubmitField('更新')


class EditCarForm(FlaskForm):
    total_cars = IntegerField('出租车总数', validators=[DataRequired()])
    price = IntegerField('价格', validators=[DataRequired()])
    submit = SubmitField('更新')


class EditHotelForm(FlaskForm):
    total_rooms = IntegerField('房间总数', validators=[DataRequired()])
    price = IntegerField('价格', validators=[DataRequired()])
    submit = SubmitField('更新')


class SearchUserForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('查找')


class EditUserForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('更新')
