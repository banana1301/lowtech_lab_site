
const sqlite3 = require('sqlite3').verbose();
const databasePath = 'database.db';
const batteryStatusElement = document.getElementById('battery-status');

setInterval(() => {
  const db = new sqlite3.Database(databasePath);
  db.get('SELECT Pourcentage_BAT FROM VALEURS_CAPTEURS', (err, row) => {

    if (err) {
      console.error(err);
    }
    else {
      const pourcent = row.Pourcentage_BAT;
      console.log(pourcent);
      if (pourcent >= 80) {
        console.log('La batterie est chargée à plus de 80%.');
        batteryStatusElement.innerHTML = '<img src="high.png" width="30" height="30">';
      }
      else if (pourcent >= 40 && pourcent < 79) {
        console.log('La batterie est chargée entre 40% et 79%.');
        batteryStatusElement.innerHTML = '<img src="medium.png" width="30" height="30">';
      }
      else {
        console.log('La batterie est chargée à moins de 40%.');
        batteryStatusElement.innerHTML = '<img src="low.png" width="30" height="30">';
      }
    }
    db.close();
  });
}, 5000);