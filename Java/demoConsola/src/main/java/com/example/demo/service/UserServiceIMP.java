package com.example.demo.service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;
import com.example.demo.repository.IUserRepository;

@Service
public class UserServiceIMP implements IUserService {
	@Autowired
	@Qualifier("persona2")
	private IUserRepository userrepository;
	@Override
	public void signup(String name) {
		userrepository.signup(name);
		
	}
}