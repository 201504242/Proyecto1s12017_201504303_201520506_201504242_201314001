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

		<title>Registrar</title>
	</head>
<body>
    <div class="container">
        <div class="row main">
            <div class="main-login main-center">
                <div class="form-group">
                    <form action="servletRegistrar" method="POST">                    
                    <label for="name" class="cols-sm-2 control-label">Nombre usuario</label>
                    <div class="cols-sm-10">
                        <div class="input-group">
                            <span class="input-group-addon"><i class="fa fa-user fa" aria-hidden="true"></i></span>
                            <input type="text" class="form-control" name="usuario" placeholder="Usuario"/>
                        </div>
                    </div>
                    
                    <label for="name" class="cols-sm-2 control-label">Empresa</label>
                    <div class="cols-sm-10">
                        <div class="input-group">									
                            <span class="input-group-addon"><i class="fa fa-users fa" aria-hidden="true"></i></span>
                            <input type="text" class="form-control" name="empresa" placeholder="Empresa"/>
                        </div>
                    </div>
                    <label for="name" class="cols-sm-2 control-label">Departamento</label>
                    <div class="cols-sm-10">
                        <div class="input-group">
                                <span class="input-group-addon"><i class="fa fa-user fa" aria-hidden="true"></i></span>
                                <input type="text" class="form-control" name="departamento" placeholder="Departamento"/>
                        </div>
                    </div>
                    <label for="password" class="cols-sm-2 control-label">Contraseña</label>
                        <div class="cols-sm-10">
                            <div class="input-group">
                                <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
                                <input type="password" class="form-control" name="password" id="password"  placeholder="Contraseña"/>
                            </div>
                        </div>
                    <br>
                    <button type="submit" class="btn btn-lg btn-warning">Registrar</button>
                    </form>
                    <br>
                    <form action="newLogin.jsp" method="POST">
                        <button type="submit" class="btn btn-lg btn-success">Regresar a Login</button>
                    </form>
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