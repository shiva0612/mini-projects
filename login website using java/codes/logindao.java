package com.loginmodule.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class LoginDao {
	
	String url = "jdbc:mysql://localhost:3306/shiva";
	String sql = "select * from login where uname=? and password=?" ;
	public boolean check(String user,String pass) {
		
		try 
		{
			Class.forName("com.mysql.jdbc.Driver");
			Connection con = DriverManager.getConnection(url,"root","0612");
			PreparedStatement st = con.prepareStatement(sql);
			st.setString(1,user);
			st.setString(2,pass);
			ResultSet rs = st.executeQuery();
			if (rs.next()) {
				return true;
			}
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
		return false;
	}
			
	

}
