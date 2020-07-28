import { Component } from '@angular/core';
import {HttpClientModule, HttpClient} from '@angular/common/http'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angularImage';
  cover;

  constructor(private http : HttpClient){}
  onImageChanged(event:any){
    //we will select the first image file
    this.cover = event.target.files[0];

  }
  onTitleChanged(event:any){
    this.title = event.target.value;

  }
  base_url = "http://127.0.0.1:8000/"
  newBook(){
    const uploadData = new FormData();
    uploadData.append('title', this.title);
    uploadData.append('cover', this.cover, this.cover.name);
    this.http.post(this.base_url+'books/', uploadData).subscribe(
      data => console.log(data),
      error => console.log(error)
    );
    }
}

