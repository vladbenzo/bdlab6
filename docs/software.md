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
'''

_seed.sql_

```sql
BEGIN;




