package com.example.demo.repository;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Repository;

import com.example.demo.DemoConsolaApplication;

@Repository
@Qualifier("persona1")
public class UserRepositoryIMP1 implements IUserRepository {
	
	private static Logger LOG = LoggerFactory.getLogger(DemoConsolaApplication.class);
	@Override
	public void signup(String name) {
		LOG.info("Registro: " + name);
	}

}
