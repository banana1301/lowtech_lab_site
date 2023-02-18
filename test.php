<h1>1</h1>
<?php
// include'../database.php';
// global $pdo;
// try{
//     $pdo = new PDO('sqlite:/var/lib/phpliteadmin/bd-low-tech');
//     $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
//     $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // ERRMODE_WARNING | ERRMODE_EXCEPTION | ERRMODE_SILENT
//     echo "canard ";
// } catch(Exception $e) {
//     echo "Impossible d'accéder à la base de données SQLite : ".$e->getMessage();
//     die();
// }


// $requete = $pdo->prepare("SELECT * FROM users");
// $requete->execute();
// $sortie = $requete->fetchAll();
// foreach ( $sortie as $result){
//     echo $result['nom'];
// }



// $requete = $pdo->prepare("INSERT INTO users (nom, prenom, email, mdp ) VALUES (:nom, :prenom, :email, :mdp)");
// $sortie = $requete->execute(array(
// 'nom'=> "test1nom",
// 'prenom'=>"tes1prenom",
// 'email'=>"test2email",
// 'mdp'=>"test1mdp"
// ));

// echo "Ca marche";


// $c = $pdo -> prepare("SELECT email FROM users WHERE email=:email");
// $c -> execute([
//     'email' => $email
// ]);
// $sortie = $c ->rowCount();
// echo $sortie;

// $requete = $pdo->prepare("SELECT * FROM users");
// $requete->execute();
// $sortie = $requete->fetchAll();
// foreach ( $sortie as $result){
//     echo $result['nom'];
// }

?>
