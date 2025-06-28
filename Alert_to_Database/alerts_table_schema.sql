CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    signature VARCHAR(255),
    priority INT,
    src_ip VARCHAR(45),
    dst_ip VARCHAR(45),
    message TEXT
);
