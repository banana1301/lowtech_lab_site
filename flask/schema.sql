
CREATE TABLE IF NOT EXISTS 'users' (
	"id"	INTEGER NOT NULL,
	"nom"	TEXT,
	"prenom"	TEXT,
	"email"	BLOB,
	"mdp"	TEXT,
	PRIMARY KEY("id")
);

-- INSERT INTO users (nom, prenom, email, mdp) VALUES ('testm', 'testl', 'test@test.com', 'azertyuiop');