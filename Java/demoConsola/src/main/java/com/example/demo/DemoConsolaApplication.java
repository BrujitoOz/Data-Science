package com.example.demo;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.example.demo.service.IUserService;


@SpringBootApplication
public class DemoConsolaApplication implements CommandLineRunner {
	
	private static Logger LOG = LoggerFactory.getLogger(DemoConsolaApplication.class);
	public static void main(String[] args) {
		SpringApplication.run(DemoConsolaApplication.class, args);
	}
	@Autowired
	private IUserService userservice;
	@Override
	public void run(String... args) throws Exception {
		// TODO Auto-generated method stub
		System.out.println("lol");
		LOG.info("lol");
		LOG.warn("cuidadito");
		//userservice.signup("lolaso");
		
	}

}
