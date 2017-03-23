<%-- 
    Document   : index
    Created on : Mar 21, 2017, 7:09:40 PM
    Author     : p_ab1
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
     <head> 
		<meta name="viewport" content="width=device-width, initial-scale=1">


		<!-- Website CSS style -->
		<link href="css/bootstrap.min.css" rel="stylesheet">

		<!-- Website Font style -->
	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.1/css/font-awesome.min.css">
		<link rel="stylesheet" href="style.css">
		<!-- Google Fonts -->
		<link href='https://fonts.googleapis.com/css?family=Passion+One' rel='stylesheet' type='text/css'>
		<link href='https://fonts.googleapis.com/css?family=Oxygen' rel='stylesheet' type='text/css'>

		<title>Inicio</title>
	</head>
    	<body>
            <div class="container">
                <div class="row main">
                    <div class="main-login main-center">
                        <div class="form-group ">
                            <a href="crearActivo.jsp" type="button" id="button" class="btn btn-primary btn-lg btn-block login-button">Agregar Activo</a>
                        </div>
                        <div class="form-group ">
                            <a href="Login.jsp" type="button" id="button" class="btn btn-primary btn-lg btn-block login-button">Eliminar Activo</a>
                        </div>
                        
                        <div class="form-group ">
                            <a href="Login.jsp" type="button" id="button" class="btn btn-primary btn-lg btn-block login-button">Modificar la Descripcion de un activo</a>
                        </div>
                         <div class="form-group ">
                            <a href="Login.jsp" type="button" id="button" class="btn btn-danger">Cerrar Sesion</a>
                        </div>
                    </div>
            
					
		</div>
</div>
		 <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
	</body>
</html>