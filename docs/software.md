# Реалізація інформаційного та програмного забезпечення


## SQL-скрипт для створення початкового наповнення бази даних

_init.sql_

```sql
CREATE TABLE Tag (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);

CREATE TABLE Role (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	description VARCHAR(255) NOT NULL
);

CREATE TABLE Permission (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);

CREATE TABLE Profile (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL
);

CREATE TABLE Source (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	url VARCHAR(255) NOT NULL
);

CREATE TABLE MediaContent (
	id SERIAL PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	description TEXT,
	body TEXT NOT NULL,
	content_type VARCHAR(255) NOT NULL,
	created_at DATE DEFAULT CURRENT_DATE,
	profile_id INT NOT NULL,
	FOREIGN KEY (profile_id) REFERENCES Profile (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE AnalysisReport (
	id SERIAL PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	body VARCHAR(255) NOT NULL,
	created_at DATE DEFAULT CURRENT_DATE,
	profile_id INT NOT NULL,
	FOREIGN KEY (profile_id) REFERENCES Profile (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE AnalysisResult (
	id SERIAL PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
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


_seed.sql_

```sql
BEGIN;

INSERT INTO Profile (id, first_name, last_name, email, password) VALUES
(1, 'Kyrylo', 'Lopushenko', 'lopushenko.kyrylo@gmail.com', 'adminadmin'),
(2, 'Vladyslav', 'TSV', 'vladonerovich03@gmail.com', 'vladbenzo'),
(3, 'Andrey', 'Kekuh', 'kekukhaleksandr@gmail.com', 'papor33'),
(4, 'John', 'Jo', 'jonjo2@gmail.com', '3321445'),
(5, 'Shvedenko', 'Ivan ', 'shvedenko.ivan2006@gmail.com', 'ivan32232323'),
(6, 'David', 'Goliath', 'davidgol@gmail.com', 'sleepingtime'),
(7, 'Taras', 'Tarasovich', 't.tarasov@gmail.com', 'slon5252'),
(8, 'Denis', 'Bakaev', 'tankist_is7_maus@gmail.com', 'qwerty21345'),
(9, 'Anastasia', 'Golovchenko', '3321.d.anasnata@gmail.com', 'passwordpassword'),
(10, 'Alexey', 'Kovalenko', 'alexey.kovalenko@gmail.com', 'kovalenko88');

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

INSERT INTO MediaContent (id, title, description, body, content_type, created_at, profile_id) VALUES
(1, 'Exploring the Ocean Depths', 'An in-depth exploration into the mysteries of the deep sea environment.', 'The ocean's vast depths hold secrets yet to be fully uncovered, from unique bioluminescent creatures to vast uncharted trenches. This piece reveals some of the enigmatic wonders found beneath the waves.', 'Article', '2025-11-01', 1),
(2, 'Advancements in AI', 'Exploring the latest breakthroughs in artificial intelligence and machine learning.', 'AI advancements continue to reshape our world, powering everything from smart assistants to autonomous vehicles. Cutting-edge algorithms and deep learning models are driving this technological revolution forward.', 'Article', '2025-11-02', 2),
(3, 'A Brief History of Space Exploration', 'From early rockets to modern Mars missions.', 'https://youtu.be/3JuKR7jf46o?si=-eG_l82dAemgaZdW', 'Video', '2025-11-03', 3),
(4, 'Tips for a Healthy Lifestyle', 'Simple, actionable steps to improve overall health and wellbeing.', 'https://www.healthline.com/health/how-to-maintain-a-healthy-lifestyle', 'Blog Post', '2025-11-04', 4),
(5, 'Understanding Quantum Computing', 'A primer on the fundamental principles of quantum computation.', 'Quantum computing leverages quantum mechanics to process information in new ways, holding the potential for exponential speedups in solving complex problems beyond the reach of classical computers.', 'Article', '2025-11-05', 5),
(6, 'Top 25 Global Travel Destinations', 'An curated list of must-visit places around the world for travelers.', 'https://www.tripadvisor.com/TravelersChoice-Destinations-cTop-g1', 'Blog Post', '2025-12-06', 6),
(7, 'The Future of Renewable Energy', 'Examining how sustainable energy sources are shaping our global future.', 'https://youtu.be/zZheOMvPWGc?si=3C6qQHf-jUApOgB0', 'Video', '2025-12-07', 7),
(8, 'Cyberpunk Cityscape Concept', 'A visual concept of a futuristic city filled with neon lights, advanced tech, high-rise buildings, flying vehicles, and bustling streets.', 'https://www.gamespot.com/a/uploads/original/1179/11799911/4363244-cyberpunk1.jpg', 'Image', '2025-12-08', 8),
(9, 'Fantasy Battle in Snowy Mountains', 'Artwork depicting an intense battle between a warrior and a formidable opponent in a frozen, mountainous landscape.', 'https://blog.playstation.com/tachyon/2025/09/c31c0e1cae38ef6a23c353e31d87e8b1cd57b700.jpeg', 'Image', '2025-12-09', 9),
(10, 'Innovations in Modern Healthcare', 'Highlighting new technologies and approaches improving patient care and outcomes.', 'Healthcare innovations, including telemedicine, AI diagnostics, and personalized medicine, are revolutionizing patient care, improving accessibility, and leading to better outcomes for various medical conditions.', 'Article', '2025-12-10', 10);

INSERT INTO AnalysisReport (id, title, body, created_at, profile_id) VALUES
(1, 'Q1 Performance Review', 'A detailed analysis of key performance indicators for the first quarter.', '2025-01-01', 1),
(2, 'Market Trend Analysis Report', 'An overview of significant market trends observed during the current quarter.', '2025-01-02', 2),
(3, 'Customer Feedback Synthesis', 'A summary and analysis of customer feedback collected over the recent period.', '2025-01-03', 1),
(4, 'New Product Launch Assessment', 'Post-launch analysis evaluating the market reception and initial success of the latest product.', '2025-01-04', 3),
(5, 'Annual Revenue Forecast Analysis', 'Revenue projection for the upcoming year based on historical data and current market trends.', '2025-01-05', 2),
(6, 'Employee Satisfaction Survey Report', 'Analysis of results from the recent employee satisfaction and engagement survey.', '2025-01-06', 4),
(7, 'Social Media Campaign Impact Study', 'An assessment of the reach, engagement, and overall impact of recent social media campaigns.', '2025-01-07', 1),
(8, 'Competitor Product Benchmarking', 'A comparative analysis of our core product features against key competitors.', '2025-01-08', 3),
(9, 'Supply Chain Efficiency Evaluation', 'An assessment of the current supply chain performance, identifying key strengths and bottlenecks.', '2025-01-09', 4),
(10, 'Website User Behavior Analysis', 'Insights into website traffic sources, user navigation patterns, and engagement metrics.', '2025-01-10', 2);

INSERT INTO AnalysisResult (id, title, description, body, created_at, analysisReport_id, profile_id) VALUES
(1, 'Key Q1 Growth Drivers', 'Identification of the primary factors contributing to business growth in Q1.', 'The analysis highlights market expansion and product innovation as key growth drivers.', '2025-02-01', 1, 1),
(2, 'Emerging Market Opportunities', 'Assessment of potential high-growth emerging markets.', 'Summary identifies Southeast Asia and Latin America as key regions with favorable trends.', '2025-02-02', 2, 2),
(3, 'Analysis of Top Customer Concerns', 'Breakdown of the most frequent issues raised by customers via support channels.', 'Detailed analysis points to usability and feature requests as common themes in customer feedback.', '2025-02-03', 3, 1),
(4, 'Initial Product Launch Performance', 'Evaluation of key performance indicators during the product launch window.', 'In-depth analysis shows strong initial adoption rates and positive user sentiment.', '2025-02-04', 4, 3),
(5, 'Q3 Sales Projections', 'Forecasted sales figures for the upcoming third quarter.', 'Data-driven sales projections indicate a potential 15% increase based on current trends.', '2025-02-05', 5, 2),
(6, 'Employee Morale Trend Analysis', 'Insights derived from qualitative and quantitative employee feedback.', 'Analysis indicates a positive trend in overall employee morale compared to the previous period.', '2025-02-06', 6, 4),
(7, 'Social Media Engagement Metrics', 'Performance overview of recent social media marketing campaigns.', 'Highlights include increased follower engagement rates and wider content reach.', '2025-02-07', 7, 1),
(8, 'Competitive Pricing Benchmark', 'Comparison of our product pricing structure against main competitors.', 'Comparative analysis reveals opportunities for adjustment in specific market segments.', '2025-02-08', 8, 3),
(9, 'Logistics Bottleneck Identification', 'Review of logistics processes and identification of efficiency issues.', 'Identified delays primarily occur during the final-mile delivery stage in specific regions.', '2025-02-09', 9, 4),
(10, 'Website User Journey Mapping', 'Analysis of user navigation paths and interaction patterns on the website.', 'Detailed report maps common user journeys and identifies key conversion points and drop-offs.', '2025-02-10', 10, 2);
INSERT INTO MediaContent (id, title, description, body, content_type, created_at, profile_id) VALUES
(1, 'Exploring the Ocean Depths', 'An in-depth exploration into the mysteries of the deep sea environment.', 'The ocean's vast depths hold secrets yet to be fully uncovered, from unique bioluminescent creatures to vast uncharted trenches. This piece reveals some of the enigmatic wonders found beneath the waves.', 'Article', '2025-11-01', 1),
(2, 'Advancements in AI', 'Exploring the latest breakthroughs in artificial intelligence and machine learning.', 'AI advancements continue to reshape our world, powering everything from smart assistants to autonomous vehicles. Cutting-edge algorithms and deep learning models are driving this technological revolution forward.', 'Article', '2025-11-02', 2),
(3, 'A Brief History of Space Exploration', 'From early rockets to modern Mars missions.', 'https://youtu.be/3JuKR7jf46o?si=-eG_l82dAemgaZdW', 'Video', '2025-11-03', 3),
(4, 'Tips for a Healthy Lifestyle', 'Simple, actionable steps to improve overall health and wellbeing.', 'https://www.healthline.com/health/how-to-maintain-a-healthy-lifestyle', 'Blog Post', '2025-11-04', 4),
(5, 'Understanding Quantum Computing', 'A primer on the fundamental principles of quantum computation.', 'Quantum computing leverages quantum mechanics to process information in new ways, holding the potential for exponential speedups in solving complex problems beyond the reach of classical computers.', 'Article', '2025-11-05', 5),
(6, 'Top 25 Global Travel Destinations', 'An curated list of must-visit places around the world for travelers.', 'https://www.tripadvisor.com/TravelersChoice-Destinations-cTop-g1', 'Blog Post', '2025-12-06', 6),
(7, 'The Future of Renewable Energy', 'Examining how sustainable energy sources are shaping our global future.', 'https://youtu.be/zZheOMvPWGc?si=3C6qQHf-jUApOgB0', 'Video', '2025-12-07', 7),
(8, 'Cyberpunk Cityscape Concept', 'A visual concept of a futuristic city filled with neon lights, advanced tech, high-rise buildings, flying vehicles, and bustling streets.', 'https://www.gamespot.com/a/uploads/original/1179/11799911/4363244-cyberpunk1.jpg', 'Image', '2025-12-08', 8),
(9, 'Fantasy Battle in Snowy Mountains', 'Artwork depicting an intense battle between a warrior and a formidable opponent in a frozen, mountainous landscape.', 'https://blog.playstation.com/tachyon/2025/09/c31c0e1cae38ef6a23c353e31d87e8b1cd57b700.jpeg', 'Image', '2025-12-09', 9),
(10, 'Innovations in Modern Healthcare', 'Highlighting new technologies and approaches improving patient care and outcomes.', 'Healthcare innovations, including telemedicine, AI diagnostics, and personalized medicine, are revolutionizing patient care, improving accessibility, and leading to better outcomes for various medical conditions.', 'Article', '2025-12-10', 10);

INSERT INTO AnalysisReport (id, title, body, created_at, profile_id) VALUES
(1, 'Q1 Performance Review', 'A detailed analysis of key performance indicators for the first quarter.', '2025-01-01', 1),
(2, 'Market Trend Analysis Report', 'An overview of significant market trends observed during the current quarter.', '2025-01-02', 2),
(3, 'Customer Feedback Synthesis', 'A summary and analysis of customer feedback collected over the recent period.', '2025-01-03', 1),
(4, 'New Product Launch Assessment', 'Post-launch analysis evaluating the market reception and initial success of the latest product.', '2025-01-04', 3),
(5, 'Annual Revenue Forecast Analysis', 'Revenue projection for the upcoming year based on historical data and current market trends.', '2025-01-05', 2),
(6, 'Employee Satisfaction Survey Report', 'Analysis of results from the recent employee satisfaction and engagement survey.', '2025-01-06', 4),
(7, 'Social Media Campaign Impact Study', 'An assessment of the reach, engagement, and overall impact of recent social media campaigns.', '2025-01-07', 1),
(8, 'Competitor Product Benchmarking', 'A comparative analysis of our core product features against key competitors.', '2025-01-08', 3),
(9, 'Supply Chain Efficiency Evaluation', 'An assessment of the current supply chain performance, identifying key strengths and bottlenecks.', '2025-01-09', 4),
(10, 'Website User Behavior Analysis', 'Insights into website traffic sources, user navigation patterns, and engagement metrics.', '2025-01-10', 2);

INSERT INTO AnalysisResult (id, title, description, body, created_at, analysisReport_id, profile_id) VALUES
(1, 'Key Q1 Growth Drivers', 'Identification of the primary factors contributing to business growth in Q1.', 'The analysis highlights market expansion and product innovation as key growth drivers.', '2025-02-01', 1, 1),
(2, 'Emerging Market Opportunities', 'Assessment of potential high-growth emerging markets.', 'Summary identifies Southeast Asia and Latin America as key regions with favorable trends.', '2025-02-02', 2, 2),
(3, 'Analysis of Top Customer Concerns', 'Breakdown of the most frequent issues raised by customers via support channels.', 'Detailed analysis points to usability and feature requests as common themes in customer feedback.', '2025-02-03', 3, 1),
(4, 'Initial Product Launch Performance', 'Evaluation of key performance indicators during the product launch window.', 'In-depth analysis shows strong initial adoption rates and positive user sentiment.', '2025-02-04', 4, 3),
(5, 'Q3 Sales Projections', 'Forecasted sales figures for the upcoming third quarter.', 'Data-driven sales projections indicate a potential 15% increase based on current trends.', '2025-02-05', 5, 2),
(6, 'Employee Morale Trend Analysis', 'Insights derived from qualitative and quantitative employee feedback.', 'Analysis indicates a positive trend in overall employee morale compared to the previous period.', '2025-02-06', 6, 4),
(7, 'Social Media Engagement Metrics', 'Performance overview of recent social media marketing campaigns.', 'Highlights include increased follower engagement rates and wider content reach.', '2025-02-07', 7, 1),
(8, 'Competitive Pricing Benchmark', 'Comparison of our product pricing structure against main competitors.', 'Comparative analysis reveals opportunities for adjustment in specific market segments.', '2025-02-08', 8, 3),
(9, 'Logistics Bottleneck Identification', 'Review of logistics processes and identification of efficiency issues.', 'Identified delays primarily occur during the final-mile delivery stage in specific regions.', '2025-02-09', 9, 4),
(10, 'Website User Journey Mapping', 'Analysis of user navigation paths and interaction patterns on the website.', 'Detailed report maps common user journeys and identifies key conversion points and drop-offs.', '2025-02-10', 10, 2);

INSERT INTO UserRole (profile_id, role_id) VALUES
(1, 1), (1, 2),
(2, 2),
(3, 1), (3, 2),
(4, 1),
(5, 2),
(6, 1),
(7, 2),
(8, 1), (8, 2);


INSERT INTO RolePermission (role_id, permission_id) VALUES
(2, 1),
(2, 2),
(1, 3),
(2, 3),
(1, 4),
(2, 4),
(1, 5),
(2, 5),
(1, 6),
(2, 6);

INSERT INTO SourceTag (tag_id, source_id) VALUES
(1, 1),
(1, 3),
(1, 4),
(1, 10),
(2, 2),
(2, 3),
(2, 4),
(2, 5),
(2, 10),
(3, 4),
(3, 10),
(4, 1),
(4, 6),
(5, 1),
(6, 1),
(6, 3),
(7, 2),
(7, 5),
(8, 1),
(9, 8),
(9, 9),
(10, 4),
(10, 10);

INSERT INTO MediaContentSource (source_id, mediaContent_id) VALUES
(1, 1), (1, 10),
(2, 2), (2, 9),
(3, 3), (3, 8),
(4, 4), (4, 7),
(5, 5), (5, 6),
(6, 6), (6, 5),
(7, 7), (7, 4),
(8, 8), (8, 3),
(9, 9), (9, 2),
(10, 10), (10, 1);


INSERT INTO MediaContentTag (tag_id, mediaContent_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 5),
(1, 7),
(1, 10),
(2, 2),
(2, 3),
(2, 4),
(2, 5),
(2, 7),
(2, 10),
(3, 4),
(3, 10),
(4, 6),
(5, 1),
(5, 7),
(6, 3),
(7, 5),
(8, 7),
(9, 8),
(9,9),
(10, 4),
(10, 10);


INSERT INTO AnalysisReportTag (analysisReport_id, tag_id) VALUES
(1, 2),
(2, 2),
(3, 3),
(4, 2),
(5, 8),
(6, 3),
(7, 2),
(8, 1),
(9, 8),
(10, 2);


INSERT INTO AnalysisResultTag (analysisResult_id, tag_id) VALUES
(1, 1),
(1, 11),
(2, 5),
(2, 11),
(3, 12),
(4, 13),
(5, 14),
(6, 3),
(6, 15),
(7, 16),
(8, 17),
(9, 18),
(10, 2),
(10, 19);


INSERT INTO MediaContentAnalysisResult (mediaContent_id, analysisResult_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 10),
(10, 1);


COMMIT;

```