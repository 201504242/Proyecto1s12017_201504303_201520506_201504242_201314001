/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.net.URL;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.util.logging.Level;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author p_ab1
 */
@WebServlet(urlPatterns = {"/servletRegistrar"})
public class servletRegistrar extends HttpServlet {
private final OkHttpClient webClient = new OkHttpClient();
    private final String puerto ="http://127.0.0.1:5000/";
    Response respuesta;
    String imp;
    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        String usuario = request.getParameter("usuario");
        String password = request.getParameter("password");
        String empresa = request.getParameter("empresa");
        String departameto = request.getParameter("departamento");        
        RequestBody formBody = new FormEncodingBuilder()
                .add("empresa", empresa)
                .add("departamneto", departameto)
                .add("nombre", usuario)
                .add("password", password)
                .add("usuario", usuario)
                .build();
        try {
            URL url = new URL(puerto + "insertarMatriz");
            Request request2 = new Request.Builder().url(url).post(formBody).build();
            respuesta = webClient.newCall(request2).execute();
            System.out.println("1"+respuesta);
            String response_srting = respuesta.body().string();
            System.out.println(response_srting);
            imp= response_srting;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(servletRegistrar.class.getName()).log(Level.SEVERE,null,ex);
        } catch (IOException ex) {
            java.util.logging.Logger.getLogger(servletRegistrar.class.getName()).log(Level.SEVERE,null,ex);  
        }
        
        
//        RequestBody formBody = new FormEncodingBuilder().add("nombre", usu).build();
//        try {
//            URL url = new URL(puerto + "prueba");
//            Request request2 = new Request.Builder().url(url).post(formBody).build();
//            respuesta = webClient.newCall(request2).execute();
//            String response_string = respuesta.body().string();
//            System.out.println(response_string);
//            imp= response_string;
//        } catch (MalformedURLException ex) {
//            java.util.logging.Logger.getLogger(servletRegistrar.class.getName()).log(Level.SEVERE,null,ex);
//        } catch (IOException ex) {
//            java.util.logging.Logger.getLogger(servletRegistrar.class.getName()).log(Level.SEVERE,null,ex);  
//        }
        
        
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet servletRegistrar</title>");            
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>Aparecio " + imp+ "</h1>");
            out.println("</body>");
            out.println("</html>");
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
