<?php ?>
<!DOCTYPE html>
<html>

    <head>
        <title>LowTech</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="/css/connecter.css">
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
            <form method="POST" id="connection">
                <h1>Se Connecter</h1>
        
                <div class="inputs">
                    <input type="email" placeholder="Email" name="email">
                    <input type="password" placeholder="Mot de Passe" name="mdp">
                </div>

                <p class="inscription">Je n'ai pas de compte.<a href="/html/inscription.php"> Je m'en crée un.</a></p>
                
                
                <div align="center">
                    <button type="submit" name="envoi">Se connecter</button>
                </div>

            </form>
        
        </section>

    </body>


<?php

include'../database.php';
global $pdo;

    if(isset($_POST['envoi'])){
        extract($_POST);

        if(!empty($email) && !empty($mdp)){

            $requete = $pdo->prepare("SELECT * FROM users WHERE email= :email");
            $requete -> execute(['email' => $email]);
            $sortie = $requete -> fetch();

            if($sortie == true){

                $hmdp = $sortie['mdp'];
                if(password_verify($mdp , $hmdp)){
                    echo "Le mdp est bon";
                }
                else{
                    echo "Le mdp n'est pas bon";
                }

            }else{
                echo "Le compte portant l'email ".$email." n'existe pas !!";
            }

        }else{
            echo "Remplir tous les champs";
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