import { bootstrap } from '@angular/platform-browser-dynamic';
import { enableProdMode } from '@angular/core';
import { AppComponent, OverviewPage } from './app';
if (process.env.ENV === 'production') {
  enableProdMode();
}
bootstrap(OverviewPage,[])
