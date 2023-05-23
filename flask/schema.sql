CREATE TABLE IF NOT EXISTS 'users' (
	"id"	INTEGER NOT NULL,
	"nom"	TEXT,
	"prenom"	TEXT,
	"email"	BLOB,
	"mdp"	TEXT,
	"status"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS 'posts' (
    "id" INTEGER NOT NULL,
    "created" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "title" TEXT NOT NULL,
    "content" TEXT NOT NULL,
	"miniature"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS 'VALEURS_CAPTEURS' (
	"date_jour"	DATETIME,
	"Tension"	float,
	"Courant"	float,
	"Pourcentage_BAT"	INTEGER,
	"Luminosite"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS 'monitoring' (
	"cpu"	INTEGER,
	"mem"	INTEGER,
	"reseaux"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);