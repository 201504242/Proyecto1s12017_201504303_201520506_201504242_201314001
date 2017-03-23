package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class registrar_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("     <head> \n");
      out.write("\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n");
      out.write("\n");
      out.write("\n");
      out.write("\t\t<!-- Website CSS style -->\n");
      out.write("\t\t<link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">\n");
      out.write("\n");
      out.write("\t\t<!-- Website Font style -->\n");
      out.write("\t    <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/font-awesome/4.6.1/css/font-awesome.min.css\">\n");
      out.write("\t\t<link rel=\"stylesheet\" href=\"style.css\">\n");
      out.write("\t\t<!-- Google Fonts -->\n");
      out.write("\t\t<link href='https://fonts.googleapis.com/css?family=Passion+One' rel='stylesheet' type='text/css'>\n");
      out.write("\t\t<link href='https://fonts.googleapis.com/css?family=Oxygen' rel='stylesheet' type='text/css'>\n");
      out.write("\n");
      out.write("\t\t<title>Registrar</title>\n");
      out.write("\t</head>\n");
      out.write("<body>\n");
      out.write("    <div class=\"container\">\n");
      out.write("        <div class=\"row main\">\n");
      out.write("            <div class=\"main-login main-center\">\n");
      out.write("                <div class=\"form-group\">\n");
      out.write("                    <form action=\"servletRegistrar\" method=\"POST\">                    \n");
      out.write("                    <label for=\"name\" class=\"cols-sm-2 control-label\">Nombre usuario</label>\n");
      out.write("                    <div class=\"cols-sm-10\">\n");
      out.write("                        <div class=\"input-group\">\n");
      out.write("                            <span class=\"input-group-addon\"><i class=\"fa fa-user fa\" aria-hidden=\"true\"></i></span>\n");
      out.write("                            <input type=\"text\" class=\"form-control\" name=\"usuario\" placeholder=\"Usuario\"/>\n");
      out.write("                        </div>\n");
      out.write("                    </div>\n");
      out.write("                    \n");
      out.write("                    <label for=\"name\" class=\"cols-sm-2 control-label\">Empresa</label>\n");
      out.write("                    <div class=\"cols-sm-10\">\n");
      out.write("                        <div class=\"input-group\">\t\t\t\t\t\t\t\t\t\n");
      out.write("                            <span class=\"input-group-addon\"><i class=\"fa fa-users fa\" aria-hidden=\"true\"></i></span>\n");
      out.write("                            <input type=\"text\" class=\"form-control\" name=\"empresa\" placeholder=\"Empresa\"/>\n");
      out.write("                        </div>\n");
      out.write("                    </div>\n");
      out.write("                    <label for=\"name\" class=\"cols-sm-2 control-label\">Departamento</label>\n");
      out.write("                    <div class=\"cols-sm-10\">\n");
      out.write("                        <div class=\"input-group\">\n");
      out.write("                                <span class=\"input-group-addon\"><i class=\"fa fa-user fa\" aria-hidden=\"true\"></i></span>\n");
      out.write("                                <input type=\"text\" class=\"form-control\" name=\"departamento\" placeholder=\"Departamento\"/>\n");
      out.write("                        </div>\n");
      out.write("                    </div>\n");
      out.write("                    <label for=\"password\" class=\"cols-sm-2 control-label\">Contraseña</label>\n");
      out.write("                        <div class=\"cols-sm-10\">\n");
      out.write("                            <div class=\"input-group\">\n");
      out.write("                                <span class=\"input-group-addon\"><i class=\"fa fa-lock fa-lg\" aria-hidden=\"true\"></i></span>\n");
      out.write("                                <input type=\"password\" class=\"form-control\" name=\"password\" id=\"password\"  placeholder=\"Contraseña\"/>\n");
      out.write("                            </div>\n");
      out.write("                        </div>\n");
      out.write("                    <br>\n");
      out.write("                    <button type=\"submit\" class=\"btn btn-lg btn-warning\">Registrar</button>\n");
      out.write("                    </form>\n");
      out.write("                    <br>\n");
      out.write("                    <form action=\"newLogin.jsp\" method=\"POST\">\n");
      out.write("                        <button type=\"submit\" class=\"btn btn-lg btn-success\">Regresar a Login</button>\n");
      out.write("                    </form>\n");
      out.write("                </div>\n");
      out.write("            </div>\n");
      out.write("        </div>\n");
      out.write("    </div>\n");
      out.write("         <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->\n");
      out.write("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>\n");
      out.write("<!-- Include all compiled plugins (below), or include individual files as needed -->\n");
      out.write("<script src=\"js/bootstrap.min.js\"></script>\n");
      out.write("</body>\n");
      out.write("</html>");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
