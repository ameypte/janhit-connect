CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    pass VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    state VARCHAR(100),
    city VARCHAR(100),
    ward_no VARCHAR(50)
);


ALTER TABLE `user`
ADD COLUMN role VARCHAR(50);
