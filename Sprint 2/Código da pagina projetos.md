<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="CSS/style2.css">
    <title>Projetos</title>
</head>
<body>

    <div class = "banner">
        <img src="design/projetos fundo.png">


        <div class="abas">
            <nav>
                <a href="home.html">Home</a>
                <a href="projeto.html">Projetos</a>
                <a href="#Sobre">Sobre</a>
                <a href="#Contato">Contatos</a>
            </nav>

        </div>
    </div>

    <div class="text" >
        <h1> Projetos </h1>
     </div>
     
     <div class="pastinha_1">
         <img src="design/pastinha.png" >
     </div>

    <div class="pastinha_2">
         <img src="design/pastinha.png">
    </div>>
     
    <div class="pastinha_3">
          <img src="design/pastinha.png">
    </div>>

    <div class="turma_ano">
        <nav>
            <a href="2020_1.html">1ºsemestre/2020</a>
            <a href="semestre2_2020">2ºsemestre/2020</a>
            <a href="semestre1_2021">1ºsemestre/2021</a>
        </nav>
    </div>        

    
</body>
</html>

#Style - CSS

@import url('https://fonts.googleapis.com/css2?family=Big+Shoulders+Stencil+Text:wght@700&display=swap');

body {
    margin: 0;
    padding: 0;
    font-family: 'Big Shoulders Stencil Text', cursive;
    height: 100px;
}

.banner img{
    position: fixed;
    top: 0;
    left: 0;
    object-fit: cover;
    width: 100%;
    height: 100vh;
}

div.abas nav a {
    display: inline-block;
    padding: 10px;
    position: relative;
    font-size: 200%;
    color: white;
    transition: .6s;
}

div.abas nav a:hover {
    background-color: rgb(46, 163, 151);
}

div.text {
    display: inline-block;
    position: relative;
    font-size: 200%;
    color: rgb(23, 230, 209);
    transition: .6s;
    left: 40%;
    font-family: 'Edo' ;
}

div.pastinha_1{
    position: fixed;
    transition: 10%;
    left: 25%;
    top: 37%;
}

div.pastinha_2{
    position: fixed;
    transition: 10%;
    left: 43%;
    top: 37%;
}

div.pastinha_3{
    position: fixed;
    transition: 10%;
    left: 61%;
    top: 37%;
}

div.turma_ano nav a{
    display: inline-block;
    padding: 130px 68px;
    position: relative;
    font-size: 100%;
    color: white;
    left: 21%;
}
