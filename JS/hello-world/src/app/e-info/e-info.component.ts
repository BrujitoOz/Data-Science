import { Component, OnInit } from '@angular/core';
import { DataService} from "../service/data.service"


@Component({
  selector: 'app-e-info',
  templateUrl: './e-info.component.html',
  styleUrls: ['./e-info.component.css'],
  providers: [DataService]
})
export class EInfoComponent implements OnInit {
  infoRecived1: string[]=[];
  infoRecived2: string[]=[];
  infoRecived3: string[]=[];

  getInfoFromS1(){
    this.infoRecived1 = this.dservice.getInfo1()
  }
  getInfoFromS2(){
    this.infoRecived2 = this.dservice.getInfo2()
  }
  getInfoFromS3(){
    this.infoRecived3 = this.dservice.getInfo3()
  }

  constructor(private dservice: DataService) { }

  ngOnInit(): void {
  }
  updateInfo(frm: any){
    this.dservice.addInfo(frm.value.location)
    
  }
}
