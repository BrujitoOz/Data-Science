import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class RecordsService {
  info1: string[] = ["Adam Taylor", 'E234', 'abc@gmail.com']
  info2: string[] = ["Shaw Miche", 'E235', 'abcdef@gmail.com']
  info3: string[] = ["Mark Ruff", 'E236', 'zxy@gmail.com']

  getinfo1(): string[]{
    return this.info1
  }
  getinfo2(): string[]{
    return this.info2
  }
  getinfo3(): string[]{
    return this.info3
  }


  constructor() { }
}
