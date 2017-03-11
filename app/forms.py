import re
from flask_wtf import Form
from wtforms import (
    widgets,
    StringField,
    SelectField,
    TextField,
    TextAreaField,
    PasswordField,
    BooleanField,
    ValidationError
)
from wtforms.validators import DataRequired, Length, EqualTo, URL

class ClientForm(Form):
    source = SelectField('来源', [DataRequired()])
    name = StringField('姓名', [DataRequired()])
    phone_num = StringField('电话号码', [DataRequired()])
    puyuan_id = StringField('谱元ID', [DataRequired()])
    original_id = StringField('原始ID', [DataRequired()])
    gender = StringField('性别', [DataRequired()])
    age = StringField('年龄', [DataRequired()])
    height = StringField('身高', [DataRequired()])
    weight = StringField('体重', [DataRequired()])
    bmi = StringField('BMI', [DataRequired()])
    inspector = StringField('送检员', [DataRequired()])
    auditor = StringField('审核员', [DataRequired()])
    smoke = StringField('吸烟', [DataRequired()])
    drink = StringField('饮酒', [DataRequired()])
    sampling_date = StringField('采样日期', [DataRequired()])
    receive_date = StringField('收样日期', [DataRequired()])
    inspect_date = StringField('检测日期', [DataRequired()])
    report_date = StringField('报告日期', [DataRequired()])
    report = StringField('是否已出具报告', [DataRequired()])
    triglyceride = StringField('甘油三酯', [DataRequired()])
    cholesterol = StringField('总胆固醇', [DataRequired()])
    h_lipoprotein = StringField('高密度脂蛋白', [DataRequired()])
    l_lipoprotein = StringField('低密度脂蛋白', [DataRequired()])
    fbg = StringField('空腹血糖', [DataRequired()])
    defecate = StringField('排便', [DataRequired()])
    medical_history = StringField('病史', [DataRequired()])
    family_history = StringField('家族病史', [DataRequired()])
    medicine = StringField('用药历史', [DataRequired()])
    remarks = StringField('备注', [DataRequired()])