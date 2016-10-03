import { bootstrap } from '@angular/platform-browser-dynamic';
import { enableProdMode } from '@angular/core';
import { AppComponent, AppComponent2, OverviewPage, PackingListPage, AccountOverviewPage, AccountTripPage, ComponentLoginPage } from './app';
if (process.env.ENV === 'production') {
  enableProdMode();
}
bootstrap(AppComponent2,[])
