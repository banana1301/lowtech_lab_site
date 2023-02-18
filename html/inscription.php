<!DOCTYPE html>
<html>

    <head>
        <title>LowTech</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="/css/inscription.css">
        <script src="https://kit.fontawesome.com/6d4b55bdfe.js" crossorigin="anonymous"></script>
        
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&family=Source+Code+Pro&display=swap" rel="stylesheet">
    </head>

    <header>

        <nav class="sigle">
            <img src="/ressource/logo_remov.png" alt="">
            <h1>Low Tech Lab</h1>
            <div class="icone">
                <a href="" id="daltonien"><i class="fa-solid fa-eye-low-vision"></i></a>
                <a href="" id="contraste"><i class="fa-solid fa-circle-half-stroke"></i></a>
            </div>
        </nav>

        <div class="menu">
                <a href="/index.php" id="acceuil">Accueil</a>
                <a href="">Articles</a>
                <a href="">Graphiques</a>
                <a href="/html/connecter.php">Se connecter</a>
                <a href="" id="a_propos">A propos</a>
        </div>
    </header>
<!-- --------------------------------------------------navbar------------------------------------------------------------- -->
    <body>

        <section class="formulaire">
            <!--Formulaire-->
            <form method="POST" id="inscription">
                <h1>Inscription</h1>
        
                <div class="inputs">
                    <input type="text" placeholder="Nom" name="nom" autocomplete="off" >
                    <input type="text" placeholder="Prénom" name="prenom" autocomplete="off">
                    <input type="email" placeholder="Email" name="email" autocomplete="off">
                    <input type="password" placeholder="Mot de Passe" name="mdp" autocomplete="off">
                    <input type="password" placeholder="Retaper mot de Passe" name="rmdp" autocomplete="off">
                </div>

                <div align="center">
                    <button type="submit" name="envoi" >S'inscrire</button>
                </div>

            </form>
        
        </section>

    </body>

<?php 

include'../database.php';
global $pdo;


if(isset($_POST['envoi'])){

    extract($_POST);

    if ( !empty($nom) AND !empty($prenom) AND !empty($email) AND !empty($mdp) AND !empty($rmdp)){
        
        if ($mdp == $rmdp){

            $options = [
                'cost' =>12,    
            ];

            $hashmdp = password_hash($mdp, PASSWORD_BCRYPT, $options);

            $c = $pdo -> prepare("SELECT email FROM users WHERE email=:email");
            $c -> execute(['email' => $email]);
            $count = $c ->fetchColumn();
            

            if ($count == 0){
                $requete = $pdo->prepare("INSERT INTO users (nom, prenom, email, mdp ) VALUES (:nom, :prenom, :email, :mdp)");
                $sortie = $requete->execute(array(
                'nom'=> $nom,
                'prenom'=>$prenom,
                'email'=>$email,
                'mdp'=>$hashmdp
                ));
                echo "Ca marche";
            }else{
                echo "Le compte existe déja !!";
            }

        }else{
            echo"pas le meme mdp";
        }

    }else{
        echo "Les champs ne sont pas tous remplies";
    }

}

?>
<!-- --------------------------------------------------footer------------------------------------------------------ -->
    <footer>
        <div class="footer">
            <div class="plan_site">
                <h1>Plan du site</h1>
                <ul>
                    <li><a href="/index.php"> Accueil</a></li>
                    <li><a href=""> Articles</a></li>
                    <li><a href=""> Graphiques</a></li>
                    <li><a href="/html/connecter.php"> Se connecter</a></li>
                    <li><a href=""> A propos</a></li>    
                </ul>
            </div>

            <div class="coordonnes">
                <h1>Coordonnées</h1>
                <ul>
                    <li> Mail : test@gmail.com</li>
                    <li> Téléphone : 01.02.03.04.05 </li>
                    <li> Addresse : 1 rue de la grande allée Brest</li>    
                </ul>
            </div>

            <div class="sociaux">
                <h1>Réseaux sociaux</h1>
                <ul>
                    <li> <a href=""> Twitter</a></li>
                    <li> <a href=""> Instagram</a></li>
                    <li> <a href=""> Facebook</a> </li>    
                </ul>
            </div>
        </div>
    </footer>

</html>