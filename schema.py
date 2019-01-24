from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///id.sqlite"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, db.Sequence('user_seq'), primary_key=True)
    uuid = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    _password = db.Column(db.Text, nullable=False)

    registered = db.Column(db.Boolean, nullable=False)
    expiration = db.Column(db.Date, nullable=False)
    token = db.Column(db.Text)

    def __init__(self, password=None, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if password:
            self.password = password

    @property
    def password(self):
        raise ValueError("password is write only.")

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value, method='pbkdf2:sha256')

    def verify_password(self, password):
        return check_password_hash(self._password, password)


class Name(db.Model):
    __tablename__ = 'name'

    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text)
    middle_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    current = db.Column(db.Boolean)  # Is this name current?
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class Email(db.Model):
    __tablename__ = 'email'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text)
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)  # Protected = Hidden and secured
    tags = db.Column(db.Text)  # Tags for the Row


class Phone(db.Model):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, unique=True)  # Phone Number stored in db.Text
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)  # Protected = Hidden and secured
    tags = db.Column(db.Text)  # Tags for the Row


class Gender(db.Model):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    gender = db.Column(db.Text)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class DOB(db.Model):
    __tablename__ = 'dob'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    dob = db.Column(db.Date)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class Height(db.Model):
    __tablename__ = 'height'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    height_ft = db.Column(db.Integer)
    height_in = db.Column(db.Integer)
    height_date = db.Column(db.Date)
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class Weight(db.Model):
    __tablename__ = 'weight'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    pounds = db.Column(db.Text)
    date = db.Column(db.Date)
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class Eyes(db.Model):
    __tablename__ = 'eyes'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    color = db.Column(db.Text)
    date = db.Column(db.Date)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class Hair(db.Model):
    __tablename__ = 'hair'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    color = db.Column(db.Text)
    date = db.Column(db.Date)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    address_text = db.Column(db.Text)  # Full db.Text for the address
    address_number = db.Column(db.Text)
    address_street = db.Column(db.Text)
    address_district = db.Column(db.Text)
    address_county = db.Column(db.Text)
    address_postal = db.Column(db.Text)
    address_country = db.Column(db.Text)
    address_coordinates_lat = db.Column(db.Text)
    address_coordinates_lon = db.Column(db.Text)
    checked = db.Column(db.Boolean)  # Checked with an address database like Google
    converted = db.Column(db.Boolean)  # Checked if address has been converted from db.Text to Parse mode
    residence_type = db.Column(db.Text)  # Own, Rent, Sublet, Lodge
    residence_use = db.Column(db.Text)  # NONE, primary residence, rental, unused << If residence_type == Own
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class SSN(db.Model):
    __tablename__ = 'ssn'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    ssn = db.Column(db.Text)  # SSN
    name = db.Column(db.Text)  # Points at the Name Table. Create a new one if not there
    image = db.Column(db.Text)  # Upload a new picture
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class DL(db.Model):
    __tablename__ = 'dl'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    dln = db.Column(db.Text)								# DL number
    ssn = db.Column(db.Text)  # Points at the SSN Table. Create a new one if not there
    state = db.Column(db.Text)
    dl_class = db.Column(db.Text)							# DL class
    name = db.Column(db.Text)  # Points at the Name Table. Create a new one if not there
    address = db.Column(db.Text)  # Points at the Address Table. Create a new one if not there
    dob = db.Column(db.Text)  # Points at the DOB Table. Create a new one if not there
    hair = db.Column(db.Text)  # Points at the hair Table. Create a new one if not there
    eyes = db.Column(db.Text)  # Points at the eyes Table. Create a new one if not there
    height = db.Column(db.Text)  # Points at the height Table. Create a new one if not there
    weight = db.Column(db.Text)  # Points at the weight Table. Create a new one if not there
    sex = db.Column(db.Text)  # Points at the gender Table. Create a new one if not there
    duplicates = db.Column(db.Integer)
    medical = db.Column(db.Text)
    organ_donor = db.Column(db.Text)
    non_resident = db.Column(db.Text)
    issued = db.Column(db.Date)
    expires = db.Column(db.Date)
    restriction = db.Column(db.Text)
    endorse = db.Column(db.Text)
    replaced = db.Column(db.Date)
    document_discriminator = db.Column(db.Text)
    image = db.Column(db.Text)
    converted = db.Column(db.Boolean)						# Checked if ID has been converted from image to Parse mode
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    registration = db.Column(db.Text)  # Points at the registration Table. Create a new one if not there
    title = db.Column(db.Text)  # Points at the title Table. Create a new one if not there
    plate = db.Column(db.Text)  # Points at the plate Table. Create a new one if not there
    ownership_type = db.Column(db.Text)  # Lease, Own, Rent
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class VehicleTitle(db.Model):
    __tablename__ = 'vehicle_title'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    title_number = db.Column(db.Text)  # Points at the registration Table. Create a new one if not there
    vin_number = db.Column(db.Text)
    year = db.Column(db.Text)  # Points at the title Table. Create a new one if not there
    make = db.Column(db.Text)  # Points at the plate Table. Create a new one if not there
    model = db.Column(db.Text)
    body = db.Column(db.Text)
    document_number = db.Column(db.Text)
    color = db.Column(db.Text)
    weight = db.Column(db.Text)
    fuel = db.Column(db.Text)
    cylinders = db.Column(db.Text)
    new = db.Column(db.Boolean)
    used = db.Column(db.Boolean)
    demo = db.Column(db.Boolean)
    title_type = db.Column(db.Text)
    issued_date = db.Column(db.Date)
    purchase_date = db.Column(db.Date)
    liens = db.Column(db.Text)
    odometer = db.Column(db.Text)
    list_price = db.Column(db.Text)
    owner_name = db.Column(db.Text)  # Points at the Name Table and the OtherNames Table, stores them in a List
    owner_address = db.Column(db.Text)  # Points at the Address Table and the OtherAddress Table, stores them in a List
    image = db.Column(db.Text)
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


class VehicleRegistration(db.Model):
    __tablename__ = 'vehicle_registration'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Text, nullable=False)
    mailing_address = db.Column(db.Text)
    plate = db.Column(db.Text)
    decal = db.Column(db.Text)
    expires = db.Column(db.Text)
    year = db.Column(db.Text)
    make = db.Column(db.Text)
    body = db.Column(db.Text)
    color = db.Column(db.Text)
    tax_month = db.Column(db.Text)
    vin = db.Column(db.Text)
    plate_type = db.Column(db.Text)
    net_weight = db.Column(db.Text)
    dln = db.Column(db.Text)
    issued_date = db.Column(db.Text)
    issued_plate = db.Column(db.Text)
    image = db.Column(db.Text)
    priority = db.Column(db.Integer, unique=True)
    protection = db.Column(db.Boolean)
    tags = db.Column(db.Text)


db.create_all()
