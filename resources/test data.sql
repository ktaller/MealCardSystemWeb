INSERT IGNORE INTO `studentportal_student` (`reg_no`, `first_name`, `last_name`, `email`, `phone`, `rfid`, `balance`) VALUES
    ('SC201/1294/2020', 'John', 'Smith', 'smith@campus.ac.ke', '0704547856', '0xa920447a', 10),
    ('SC201/1295/2020', 'John', 'Doe', 'john@campus.ac.ke', '0704847856', '0x15ce5302', 10),
    ('SC201/1296/2020', 'Jane', 'Doe', 'jane@campus.ac.ke', '0706547856', '0x1b4c4c4c', 10);

INSERT IGNORE INTO `studentportal_meals` (`name`, `price`) VALUES
    ('Chapati', 50),
    ('Ugali', 30),
    ('Rice', 40),
    ('Pilau', 60),
    ('Beef', 100),
    ('Chicken', 80),
    ('Fish', 70);