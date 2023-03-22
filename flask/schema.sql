
CREATE TABLE IF NOT EXISTS 'users' (
	"id"	INTEGER NOT NULL,
	"nom"	TEXT,
	"prenom"	TEXT,
	"email"	BLOB,
	"mdp"	TEXT,
	"status"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- INSERT INTO users (nom, prenom, email, mdp) VALUES ('testm', 'testl', 'test@test.com', 'azertyuiop');

CREATE TABLE IF NOT EXISTS 'posts' (
    "id" INTEGER NOT NULL,
    "created" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" TEXT NOT NULL,
    "content" TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);