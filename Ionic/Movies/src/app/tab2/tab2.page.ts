import { Component } from '@angular/core';
import { InfiniteScrollCustomEvent } from '@ionic/angular';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page {
  public actorsList:any = [];
  constructor() {}
  public previous = "";
  public next = "";

  async loadActors(url = "http://localhost:8000/filmes/atores/?page=1"){
    const response = await fetch(url,{
      method : "GET",
      headers:{
        "Content-Type": "application/json",
        "Authorization": "Token " + sessionStorage.getItem("token")
      }
    });

    const status = response.status;
    if(status === 200){
      const data = await response.json();
      this.actorsList = this.actorsList.concat(data.results);
      this.next = data.next;
      this.previous = data.previous;
    } else {
      alert("Erro ao ligar o servidor")
    }
  }

  async ngOnInit(){
    this.loadActors();
  }

  onIonInfinite(ev:any) {
    setTimeout(() => {
      if(this.next !=null){
        this.loadActors(this.next);
      }
      (ev as InfiniteScrollCustomEvent).target.complete();
    }, 500);
  }


}
