<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title> Reponse au QUIZ</title>
    </head>
    <body>
        <?php
        echo "Merci d'avoir repondu au quiz ! <ul>";
        if ($_GET["foot"] == "Arg")
            echo "Bravo, question 1 : reponse juste";
        else
            echo "Non, question 1  : reponse fausse";

        if(lempty($_GET['distance'])) {
            echo "<li> Selon vous, la plus longue epreuve de natation aux 30 est de ".$_GET['distance']." m";
            if ($_GET['distance'] == '10000')
            echo "Bravo, la distance est de 10 000 m : reponse juste";
        else
            echo "Non, question 2  : reponse fausse";
        }
    </body>
</html>