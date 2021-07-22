
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id int IDENTITY(1,1) PRIMARY KEY,
    last_name varchar(255) NOT NULL,
    first_name varchar(255) NOT NULL,
    address varchar(255),
    city varchar(255),
    email varchar(255)
);

DROP TABLE IF EXISTS vehicles;

CREATE TABLE vehicles (
    vehicle_id int IDENTITY(1,1) PRIMARY KEY,
    license_plate varchar(255) NOT NULL,
    vehicle_make varchar(255) NOT NULL,
    vehicle_color varchar(255) NOT NULL,
    vehicle_details varchar(255) NOT NULL
 
);

DROP TABLE IF EXISTS shipping;

CREATE TABLE shipping (
    shipping_id int IDENTITY(1,1) PRIMARY KEY,
    customer_id int NOT NULL,
    lot_id varchar(255),
    shipping_date datetime,
    outbound_order_number varchar(255),
    product_order_number varchar(255),
    shipping_address varchar(255),
    billing_address varchar(255),
    vehicle_id int NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);


DROP TABLE IF EXISTS devices;

CREATE TABLE devices (
    device_id int IDENTITY(1,1) PRIMARY KEY,
    device_source_id varchar(255) NOT NULL UNIQUE,
    device_type varchar(255) NOT NULL,
    device_brand varchar(255) NOT NULL,
    device_details varchar(255)
);


DROP TABLE IF EXISTS camera_detection_history;

CREATE TABLE camera_detection_history (
    reference_id int IDENTITY(1,1) PRIMARY KEY,
    device_source_id varchar(255),
    date_detection DATETIME DEFAULT SYSDATETIMEOFFSET() AT TIME ZONE 'Eastern Standard Time',
    vehicle_license_plate varchar(255),
    vehicle_direction varchar(255),
    vehicle_other varchar(255),
    image_url varchar(255),
    date_insert DATETIME DEFAULT SYSDATETIMEOFFSET() AT TIME ZONE 'Eastern Standard Time',
    FOREIGN KEY (device_source_id) REFERENCES devices(device_source_id),
);


GO

begin

INSERT INTO customers (last_name, first_name , address, city, email)
VALUES
    (
        'Recasens',
        'Javier',
        '5534 Highland Preserve Dr',
        'Mableton',
        'javier.recasens@outlook.com'
    ),
    (
        'Pedro',
        'Aguirre',
        '123 abc',
        'Atlanta',
        'recarrete@gmail.com'
    );

INSERT INTO vehicles (license_plate, vehicle_make, vehicle_color, vehicle_details)
VALUES
    (
        '123456',
        'Mercedes Benz',
        'White',
        'Big old truck from the 80s'
    );

INSERT INTO shipping (customer_id, lot_id, shipping_date, outbound_order_number, product_order_number, shipping_address, billing_address, vehicle_id)
VALUES
    (
        1,
        'LOD 1234',
        '01/11/2020 00:00:00',
        '5252452',
        '436345345',
        'Cali 1234',
        '',
        1
    );


INSERT INTO devices (device_source_id, device_type, device_brand, device_details)
VALUES
    (
        'sample_device',
        'camera',
        'sony',
        'background'
    );


INSERT INTO camera_detection_history (device_source_id, date_detection, vehicle_license_plate, vehicle_direction, vehicle_other, image_url)
VALUES
    (
        'sample_device',
        '02/02/2021 00:00:00',
        '123456',
        'Entrando',
		'',
        'https://storagetestdelete123.blob.core.windows.net/publiccontainer/logo-solid-blue.png'
    );

end;
