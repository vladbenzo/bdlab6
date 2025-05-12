# Реалізація інформаційного та програмного забезпечення


## SQL-скрипт для створення початкового наповнення бази даних

_init.sql_

```sql
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

CREATE TABLE UserRole (
	profile_id INT NOT NULL,
	role_id INT NOT NULL,
	PRIMARY KEY (profile_id, role_id),
	FOREIGN KEY (profile_id) REFERENCES Profile (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (role_id) REFERENCES Role (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE RolePermission (
	role_id INT NOT NULL,
	permission_id INT NOT NULL,
	PRIMARY KEY (role_id, permission_id),
	FOREIGN KEY (role_id) REFERENCES Role (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (permission_id) REFERENCES Permission (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE MediaContentSource (
	source_id INT NOT NULL,
	mediaContent_id INT NOT NULL,
	PRIMARY KEY (source_id, mediaContent_id),
	FOREIGN KEY (source_id) REFERENCES Source (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (mediaContent_id) REFERENCES MediaContent (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE MediaContentTag (
	tag_id INT NOT NULL,
	mediaContent_id INT NOT NULL,
	PRIMARY KEY (tag_id, mediaContent_id),
	FOREIGN KEY (tag_id) REFERENCES Tag (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (mediaContent_id) REFERENCES MediaContent (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE SourceTag (
	tag_id INT NOT NULL,
	source_id INT NOT NULL,
	PRIMARY KEY (tag_id, source_id),
	FOREIGN KEY (tag_id) REFERENCES Tag (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (source_id) REFERENCES Source (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE AnalysisReportTag (
	analysisReport_id INT NOT NULL,
	tag_id INT NOT NULL,
	PRIMARY KEY (analysisReport_id, tag_id),
	FOREIGN KEY (analysisReport_id) REFERENCES AnalysisReport (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (tag_id) REFERENCES Tag (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE AnalysisResultTag (
	analysisResult_id INT NOT NULL,
	tag_id INT NOT NULL,
	PRIMARY KEY (analysisResult_id, tag_id),
	FOREIGN KEY (analysisResult_id) REFERENCES AnalysisResult (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (tag_id) REFERENCES Tag (id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE MediaContentAnalysisResult (
	mediaContent_id INT NOT NULL,
	analysisResult_id INT NOT NULL,
	PRIMARY KEY (mediaContent_id, analysisResult_id),
	FOREIGN KEY (mediaContent_id) REFERENCES MediaContent (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (analysisResult_id) REFERENCES AnalysisResult (id) ON DELETE CASCADE ON UPDATE CASCADE
);


```seed.sql

```sql
BEGIN;
INSERT INTO Profile (id, first_name, last_name, email, password) VALUES
(1, 'Kyrylo', 'Lopushenko', 'lopushenko.kyrylo@gmail.com', adminadmin'),
(2, 'VLadyslav', 'TSV', 'vladonerovich03@gmail.com', 'vladbenzo'),
(3, 'Andrey', 'Kekuh', 'kekukhaleksandr@gmail.com', 'papor33'),
(4, 'John', 'Jo', 'jonjo2@gmail.com', '3321445'),
(5, 'Shvedenko', 'Ivan ', 'shvedenko.ivan2006@gmail.com', 'ivan32232323'),
(6, 'David', 'Goliath', 'davidgol@gmail.com', 'sleepingtime'),
(7, 'Taras', 'Tarasovich', 't.tarasov@gmail.com', 'slon5252'),
(8, 'Denis, 'Bakaev', 'tankist_is7_maus@gmail.com', 'qwerty21345'),
(8, 'Anastasia', 'Golovchenko', '3321.d.anasnata@gmail.com', 'passwordpassword'),
(9, 'Alexey', 'Kovalenko', 'alexey.kovalenko@gmail.com', 'kovalenko88'),
(10, 'Primo', 'Petrenko', 'prim.petr@yahoo.com', 'pass2s123');

INSERT INTO Tag (id, name) VALUES
(1, 'Science'),
(2, 'Technology'),
(3, 'Health'),
(4, 'Travel'),
(5, 'Environment'),
(6, 'Space Exploration'),
(7, 'Quantum Computing'),
(8, 'Renewable Energy'),
(9, 'Gaming'),
(10, 'Medicine'),
(11, 'Market Analysis'),
(12, 'Customer Insights'),
(13, 'Product Launch'),
(14, 'Sales Projections'),
(15, 'Employee Feedback'),
(16, 'Social Media'),
(17, 'Competitor Analysis'),
(18, 'Logistics'),
(19, 'User Experience');

INSERT INTO Source (id, name, url) VALUES
(1, 'National Geographic', 'https://www.nationalgeographic.com'),
(2, 'TechCrunch', 'https://techcrunch.com'),
(3, 'NASA', 'https://www.nasa.gov'),
(4, 'Healthline', 'https://www.healthline.com'),
(5, 'Quanta Magazine', 'https://www.quantamagazine.org'),
(6, 'TripAdvisor', 'https://www.tripadvisor.com'),
(7, 'YouTube', 'https://www.youtube.com'),
(8, 'GameSpot', 'https://www.gamespot.com'),
(9, 'PlayStation Blog', 'https://blog.playstation.com'),
(10, 'MedTech News', 'https://www.medtechnews.com');

INSERT INTO Role (id, name, description) VALUES
(1, 'User', 'Standard user with basic permissions'),
(2, 'TechnicalExpert', 'Specialist responsible for technical aspects and content management');

INSERT INTO Permission (id, name) VALUES
(1, 'user.role.promote'),
(2, 'user.delete'),
(3, 'content.create'),
(4, 'content.search'),
(5, 'content.update'),
(6, 'content.delete');



COMMIT;

