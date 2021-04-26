import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { FormcomponentComponent } from './formcomponent.component';

describe('FormcomponentComponent', () => {
  let component: FormcomponentComponent;
  let fixture: ComponentFixture<FormcomponentComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ FormcomponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FormcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
