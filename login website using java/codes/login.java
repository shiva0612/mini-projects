package com.loginmodule;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.loginmodule.dao.LoginDao;

@WebServlet("/Login")
public class Login extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		LoginDao dao = new LoginDao();
		response.getWriter().append("Served at: ").append(request.getContextPath());
		String user = request.getParameter("user");
		String pass = request.getParameter("pass");
		
		if (dao.check(user, pass)) {
			HttpSession session = request.getSession();
			session.setAttribute("username", user);
			response.sendRedirect("welcome.jsp");
			
		}
		else {
			response.sendRedirect("login.jsp");
		}
	}

	}


	


