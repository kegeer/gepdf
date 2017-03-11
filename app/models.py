from flask_sqlalchemy import SQLAlchemy
import datetime
from uuid import uuid4
db = SQLAlchemy()


class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.String(45), primary_key=True)
    source = db.Column(db.SmallInteger())
    name = db.Column(db.String(255))
    phone_num = db.Column(db.String(45), nullable=True)
    puyuan_id = db.Column(db.String(45), index=True)
    original_id = db.Column(db.String(45))
    gender = db.Column(db.SmallInteger())
    age = db.Column(db.SmallInteger())
    height = db.Column(db.Float(), nullable=True)
    weight = db.Column(db.Float(), nullable=True)
    bmi = db.Column(db.Float(), nullable=True)
    inspector = db.Column(db.SmallInteger())
    auditor = db.Column(db.SmallInteger())
    smoke = db.Column(db.Boolean(), default=False)
    drink = db.Column(db.Boolean(), default=False)
    sampling_date = db.Column(db.DateTime(), nullable=True)
    receive_date = db.Column(db.DateTime(), nullable=True)
    inspect_date = db.Column(db.DateTime(), nullable=True)
    report_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    report = db.Column(db.Boolean(), default=True)
    triglyceride = db.Column(db.Float(), nullable=True)
    cholesterol = db.Column(db.Float(), nullable=True)
    h_lipoprotein = db.Column(db.Float(), nullable=True)
    l_lipoprotein = db.Column(db.Float(), nullable=True)
    fbg = db.Column(db.Float(), nullable=True)
    defecate = db.Column(db.SmallInteger(), nullable=True)
    medical_history = db.Column(db.Text(), nullable=True)
    family_history = db.Column(db.Text(), nullable=True)
    medicine = db.Column(db.Text(), nullable=True)
    remarks = db.Column(db.Text(), nullable=True)

    # define relationship with result
    results = db.relationship(
        'Result',
        backref='client',
        lazy='dynamic'
    )

    def __init__(self, name):
        self.id = str(uuid4())
        self.name = name

    def __repr__(self):
        return "<Model Client `{}`>".format(self.name)


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.String(45), primary_key=True)
    client_id = db.Column(db.String(45), db.ForeignKey('clients.id'))
    content = db.Column(db.JSON())

    def __init__(self):
        self.id = str(uuid4())

    def __repr__(self):
        return "<Model Result `{}`>".format(self.client_id)


class Info(db.Model):
    __tablename__ =  'infos'
    id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(255), nullable=True)
    e_name = db.Column(db.String(255), nullable=True)
    type = db.Column(db.String(50), nullable=True)
    desc = db.Column(db.Text(), nullable=True)
    ref_min = db.Column(db.Float, nullable=True)
    ref_max = db.Column(db.Float, nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'info',
        'polymorphic_on': type,
        'with_polymorphic': '*'
    }
    refs = db.relationship(
        'Ref',
        backref='info',
        lazy='dynamic'
    )
    def __init__(self, c_name, e_name):
        self.c_name = c_name
        self.e_name =e_name
            


    def __repr__(self):
        return "<Model Info `{}`>".format(self.c_name)


class General(Info):

    __tablename__ = 'general'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    gn_type = db.Column(db.String(25))

    __mapper_args__ = {
        'polymorphic_identity': 'gn'
    }

    def __init__(self):
        pass

    def __repr__(self):
        return "<Model General `{}`>".format(self.gn_type)


class Metabolism(Info):

    __tablename__ = 'metabolism'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    me_type = db.Column(db.String(10))
    __mapper_args__ = {
        'polymorphic_identity': 'metabolism'
    }

    def __init__(self):
        super(Metabolism, self).__init__()

    def __repr__(self):
        return "<Model Metabolism `{}`>".format(self.me_type)


class Genus(Info):

    __tablename__ = 'genus'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    ge_type = db.Column(db.String(10))
    __mapper_args__ = {
        'polymorphic_identity': 'ge'
    }

    def __init__(self):
        pass

    def __repr__(self):
        return "<Model Genus `{}`>".format(self.ge_type)


class Species(Info):

    __tablename__ = 'species'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    sp_type = db.Column(db.String(10))

    __mapper_args__ = {
        'polymorphic_identity': 'sp'
    }
    def __init__(self):
        pass

    def __repr__(self):
        return "<Model Species `{}`>".format(self.sp_type)


class Disease(Info):

    __tablename__ = 'disease'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    di_type = db.Column(db.String(10))
    __mapper_args__ = {
        'polymorphic_identity': 'di'
    }

    def __init__(self):
        pass

    def __repr__(self):
        return "<Model Disease `{}`>".format(self.Disease)


class Ref(db.Model):

    __tablename__ = 'refs'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    info_id = db.Column(db.Integer, db.ForeignKey('infos.id'))
    status = db.Column(db.SmallInteger())
    color = db.Column(db.SmallInteger())
    img = db.Column(db.SmallInteger())
    desc = db.Column(db.Text())

    def __init__(self):
        pass

    def __repr__(self):
        return "<Model Ref `{}`>".format(self.info_id)