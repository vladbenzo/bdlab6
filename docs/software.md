# Реалізація інформаційного та програмного забезпечення


## SQL-скрипт для створення початкового наповнення бази даних

```init.sql

CREATE TABLE Tag (
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL
);

CREATE TABLE Role (
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL,
	description VARCHAR(45) NOT NULL
);

CREATE TABLE Permission (
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL
);

CREATE TABLE Profile (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(45) NOT NULL,
	last_name VARCHAR(45) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL
);

CREATE TABLE Source (
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL,
	url VARCHAR(255) NOT NULL
);

CREATE TABLE MediaContent (
	id SERIAL PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	description TEXT,
	body TEXT NOT NULL,
	content_type VARCHAR(45) NOT NULL,
	created_at DATE DEFAULT CURRENT_DATE,
	profile_id INT NOT NULL,
	FOREIGN KEY (profile_id) REFERENCES Profile (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE AnalysisReport (
	id SERIAL PRIMARY KEY,
	title VARCHAR(45) NOT NULL,
	body VARCHAR(255) NOT NULL,
	created_at DATE DEFAULT CURRENT_DATE,
	profile_id INT NOT NULL,
	FOREIGN KEY (profile_id) REFERENCES Profile (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE AnalysisResult (
	id SERIAL PRIMARY KEY,
	title VARCHAR(45) NOT NULL,
	description VARCHAR(255),
	body VARCHAR(255) NOT NULL,
	created_at DATE DEFAULT CURRENT_DATE,
	analysisReport_id INT NOT NULL,
	profile_id INT NOT NULL,
	FOREIGN KEY (analysisReport_id) REFERENCES AnalysisReport (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (profile_id) REFERENCES Profile (id) ON DELETE CASCADE ON UPDATE CASCADE
);
