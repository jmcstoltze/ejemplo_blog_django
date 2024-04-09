from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(
        """
            <!DOCTYPE html>
            <html lang="es">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Nicanor Parra</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #fff3e6;
                    }
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                        text-align: center;
                    }
                    h1 {
                        color: #333;
                    }
                    p {
                        text-align: justify;
                    }
                    .quote {
                        font-size: 30px;
                        font-style: italic;
                        color: #666;
                    }
                    .centrado {
                        text-align: center;
                    }
                    .contacto-link {
                        color: #ff6600;
                        text-decoration: none;
                    }
                    .contacto-link:hover {
                        text-decoration: underline;
                    }
                </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Nicanor Parra: Entre la Tinta y la Revolución Poética</h1>
                        <hr>
                        <p>Nicanor Parra, voz rebelde de la poesía chilena, rompió esquemas con su "antipoesía", desafiando la norma con versos crudos y directos. Su obra, un espejo de la humanidad, refleja el absurdo y la ironía de la existencia, cautivando con su estilo único y provocativo. Parra, maestro de la palabra, sigue resonando en el alma de quienes buscan la verdad en la belleza de lo simple.</p>
                        <br>
                        <p class="centrado">En palabras del propio Parra:</p>
                        <blockquote class="quote">
                            <strong>"Lo importante no es ser sino parecer."</strong>
                        </blockquote>
                        <img src="https://cvc.cervantes.es/img/parra/portada.jpg" alt="Nicanor Parra">
                        <p class="centrado"><a href="/about/"</a>¡Explora nuestro sitio para descubrir más sobre su vida y obra!</a></p>
                        
                        <!-- Enlace hacia la página de contacto -->
                        <p class="centrado">¿Interesado en asistir al evento o recibir un libro de obsequio? <a href="/contact/" class="contacto-link">Contáctanos</a></p>
                    </div>
                </body>
            </html>
        """
    )

def contact(request):
    return HttpResponse(
        """
            <!DOCTYPE html>
            <html lang="es">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Contacto</title>
                <style>
                    body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #fff3e6;
                    }
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                        text-align: center;
                    }
                    h1 {
                        color: #333;
                    }
                    p {
                        text-align: justify;
                    }
                    .form-container {
                        text-align: left;
                    }
                    input[type="text"],
                    input[type="email"],
                    textarea {
                        width: 100%;
                        padding: 10px;
                        margin-bottom: 10px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                    textarea {
                        height: 150px;
                    }
                    input[type="button"] {
                        background-color: #ff6600;
                        color: #fff;
                        border: none;
                        padding: 10px 20px;
                        cursor: pointer;
                        border-radius: 5px;
                    }
                    input[type="button"]:hover {
                        background-color: #ff8533;
                    }
                </style>
                <script>
                        function mostrarFrase() {
                            alert("Las palabras deben ser un puente y no una barrera.");
                        }
                </script>
                </head>
            <body>
                <div class="container">
                    <h1>Contacto</h1>
                    <p><a href="/home">Volver al inicio</a></p>
                    <hr>
                    <div class="form-container">
                        <form>
                            <center>
                                <img src="https://1.bp.blogspot.com/-sxdzE8YY1QI/TtoKt5DOjJI/AAAAAAAAARE/MU2iI5dHPUU/s1600/Obras_completas_Nicanor_Parra_incluyen_rap_Sagrada_Familia.jpg" height="400px";/>
                            </center>
                            <br>
                            <label for="nombre">Nombre:</label><br>
                            <input type="text" id="nombre" name="nombre"><br>
                            
                            <label for="email">Email:</label><br>
                            <input type="email" id="email" name="email"><br>
                            
                            <label for="mensaje">Mensaje:</label><br>
                            <textarea id="mensaje" name="mensaje" rows="4" cols="50"></textarea><br>
                            
                            <input type="button" value="Enviar" onclick="mostrarFrase()">

                        </form>
                    </div>
                
                </div>

                
                
            </body>
        </html>        
        """
        )

def about(request):
    return HttpResponse(
        """
            <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Acerca de Nicanor Parra</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #fff3e6;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: justify;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        h2 {
            color: #555;
        }
        p {
            margin-bottom: 20px;
        }
        img {
            display: block;
            margin: 0 auto;
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Acerca de Nicanor Parra</h1>
        <p><a href="/home">Volver al inicio</a></p>
        <hr>
        <img src="https://www.fayerwayer.com/resizer/OSejMXIBpozpUvGtJQe-8sYeFiU=/800x0/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/metroworldnews/4KDMTVGAIJAEFAGIMYPJBAVEMA.jpg" alt="Nicanor Parra">
        
        <h2>Biografía</h2>
        <p>Nicanor Parra nació el 5 de septiembre de 1914 en San Fabián de Alico, Chile. Fue un destacado poeta y físico chileno, conocido principalmente por su estilo innovador y su rechazo a los convencionalismos literarios.</p>
        
        <h2>Legado y Obras</h2>
        <p>Parra es reconocido por su contribución a la literatura latinoamericana con su "antipoesía", un estilo que desafía las normas poéticas tradicionales. Sus obras más destacadas incluyen "Poemas y antipoemas" (1954), "Artefactos" (1972), y "Sermones y prédicas del Cristo de Elqui" (1977).</p>
        
        <h2>Geografía y Artefactos</h2>
        <p>Nicanor Parra pasó gran parte de su vida en Chile, influenciado por el entorno de la naturaleza y la cultura chilena. Su legado también incluye una serie de "artefactos", objetos y poemas que desafían las convenciones literarias y sociales.</p>
        
        <h2>Familia</h2>
        <p>Parra proviene de una familia de destacados intelectuales chilenos. Su hermana Violeta Parra fue una reconocida cantautora y folclorista, y su hermano Roberto Parra también fue un músico y compositor conocido.</p>
    
    </div>
    
</body>
</html>

        """
    )
