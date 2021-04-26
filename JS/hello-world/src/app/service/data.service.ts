import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  info1: string[]=["Jhon Mat", 'E32', 'jmb@gmail.com']
  info2: string[]=["Rob Will", 'E33', 'rw@gmail.com']
  info3: string[]=["Rose Adams", 'E34', 'ra@gmail.com']

  getInfo1():string[]{
    return this.info1
  }
  getInfo2():string[]{
    return this.info2
  }
  getInfo3():string[]{
    return this.info3
  }
  addInfo(info){
    this.info1.push(info)
    this.info2.push(info)
    this.info3.push(info)
  }
  constructor() { }
}
