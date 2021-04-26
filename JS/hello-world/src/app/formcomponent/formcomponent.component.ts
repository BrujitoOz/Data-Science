import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-formcomponent',
  templateUrl: './formcomponent.component.html',
  styleUrls: ['./formcomponent.component.css']
})
export class FormcomponentComponent{

  submit(login){
    console.log("form submitted", login)
  }



}
