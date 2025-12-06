DROP TABLE IF EXISTS users;
CREATE TABLE users(
Username varchar(30) PRIMARY KEY,
hashed_password TEXT NOT NULL,
Roles varchar(10) NOT NULL
);

INSERT INTO users (username, hashed_password, Roles)
VALUES
('john_doe', 'john12', 'client'),
('priya_dharshini', 'priy123', 'client'),
('arun_kumar', 'arun123', 'support'),
('anand_s', 'anan123', 'client'),
('dhanya_j', 'dhan123', 'support'),
('chithra_s', 'chit123', 'client'),
('vijay_k', 'vija123', 'support'),
('pugal_r', 'puga123', 'client'),
('jayaraman_v', 'jaya123', 'support'),
('sasikala_j', 'sasi123', 'client');

UPDATE users
SET hashed_password='e47a8b20929515a2a38624aa552ebbdc935d84cc9508d23f59c4f0941fcbe4c7'
WHERE username='john_doe';
UPDATE users
SET hashed_password='bbef9874d041772c70dd3e82d6277f9c2caad99edc59eb583c8b80b71ec3f34c'
WHERE username='priya_dharshini';
UPDATE users
SET hashed_password='1f1d5f931045a65e39114639ae0567c60cd8fa32f43ce275a73375735d350fbb'
WHERE username='arun_kumar';
UPDATE users
SET hashed_password='4fb72462ff2546fa211a0eea3cfbc35f4a19d48f09f5119527bee62974eee43e'
WHERE username='anand_s';
UPDATE users
SET hashed_password='e24884bcc720cec74d28b469423de8d4ba75d845c80916c3bd788dcd99441d0d'
WHERE username='dhanya_j';
UPDATE users
SET hashed_password='a2de0d6519483039d11a1ff9eadeeaa315083e2cd0501970876dd661b32c583c'
WHERE username='chithra_s';
UPDATE users
SET hashed_password='1e04daa09a9c3feb91bc2a4205fa3611b475adbe4ef836d902f55a2d7782dee9'
WHERE username='vijay_k';
UPDATE users
SET hashed_password='ac16c8d9297db9be1c3b6d4dbce5f1e789831543e35a1733955edd802b2a7fe5'
WHERE username='pugal_r';
UPDATE users
SET hashed_password='620d784dc2bbb0d554fecc32dc5b37f65231d0e497202492666a4c95a8d014c0'
WHERE username='jayaraman_v';
UPDATE users
SET hashed_password='0a9f3471c824dba739e8e800a684007dbe846bc00e2c7578ae4022095dfba9be'
WHERE username='sasikala_j';


SELECT * FROM users;