-- script that converts hbtn_0c_0 database, Table first_table and Field name in first_table to UTF8

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8;
ALTER TABLE first_table MODIFY name VARCHAR(255) CHARACTER SET utf8;
