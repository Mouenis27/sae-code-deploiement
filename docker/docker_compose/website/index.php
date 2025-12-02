<html>
    <head>
        <title>My SHOP</title>
    </head>
    <body>
        <h1>La liste des produits disponibles est :</h1>
        <ul>
            <?php
            // Correction du protocole : hhtp → http
            $json = file_get_contents('http://product-service/');
            
            // Décodage JSON en objet
            $obj = json_decode($json);

            // La clé retournée par ton API est "product" (pas "products")
            $products = $obj->product;

            // Boucle d'affichage
            foreach ($products as $product) {
                echo "<li>$product</li>";
            }
            ?>
        </ul>
    </body>
</html>
