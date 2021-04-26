import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { TextcomponentComponent } from './textcomponent.component';

describe('TextcomponentComponent', () => {
  let component: TextcomponentComponent;
  let fixture: ComponentFixture<TextcomponentComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ TextcomponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TextcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
