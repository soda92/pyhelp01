from app import database, Employee, app

with app.app_context():
    database.create_all()

    e1 = Employee(employee_id=1, first_name = "Cris",
    last_name="Soda", email_address="sodacris@example.com",
    phone_number = "123", first_aid_trained=True, password="yep")

    database.session.add(e1)
    database.session.commit()
