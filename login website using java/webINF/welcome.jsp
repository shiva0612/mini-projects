<%@page import="org.apache.catalina.ha.backend.Sender"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<%
if(session.getAttribute("username") == null){
	
	response.sendRedirect("login.jsp");
}
%>
welcome ${username}
<a href="videos.jsp">click here for your videos</a>

<form action="Logout">
<input type ="submit" value = "Logout" >
</form>

</body>
</html>
