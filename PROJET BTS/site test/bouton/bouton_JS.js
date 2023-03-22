var select = document.getElementById("colorFilterSelect"); /* REGARDE CE QUI EST SELECTIONNEE DANS LE BOUTTON colorFilterSelec */
var CONTENU = document.getElementById("CONTENU"); /* REGARDE CE QUI CE SITUE DANS LES div >>CONTENU<< */
select.addEventListener("change", function() { /* ECOUTE S'IL Y A DU CHANGEMENT DANS select SI OUI IL EFFECTUE FONCTION DEFINIE EN DESSOUS */
  if (select.value === "Protanopia") {
    CONTENU.style.filter = "url(#protanopiaColourMatrix)";
  } else if (select.value === "protanomaly") {
    CONTENU.style.filter = "url(#protanomalyColourMatrix)";
  } else if (select.value === "deuteranopia") {
    CONTENU.style.filter = "url(#deuteranopiaColourMatrix)";
  } else if (select.value === "deutranomaly") {               /* TEST DE LA VALEUR DE select */
    CONTENU.style.filter = "url(#deutranomalyColourMatrix)";  /* APPLIQUE AUX div d'ID "CONTENU" LE FILTRE D'URL DONNEE */
  } else if (select.value === "tritanopia") {
    CONTENU.style.filter = "url(#tritanopiaColourMatrix)";
  } else if (select.value === "tritanomaly") {
    CONTENU.style.filter = "url(#tritanomalyColourMatrix)";
  } else if (select.value === "achromatopsia") {
    CONTENU.style.filter = "url(#achromatopsiaColourMatrix)";
  } else if (select.value === "achromatomaly") {
    CONTENU.style.filter = "url(#achromatomalyColourMatrix)";
  } else {
    CONTENU.style.filter = "none";
  }
});