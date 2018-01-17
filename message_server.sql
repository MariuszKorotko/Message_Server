USE message_server_db;

CREATE TABLE Users(
    id INT(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(80) NOT NULL,
    PRIMARY KEY(id)
);
