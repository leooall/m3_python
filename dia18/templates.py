from string import Template

# instantiate template
template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
</head>
<body>
    <h1>aves de chile</h1>
    <br>
    
    $contenido
    
</body>
</html>                   
""")

body = Template("""
    <div>
        <h2>$titulo_esp</h2>
        <h2>$titulo_en</h2>
        <img src="$url_img_full" 
            alt="$titulo_esp"> 
    </div>               
""")