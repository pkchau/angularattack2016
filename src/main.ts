import { bootstrap } from '@angular/platform-browser-dynamic';
import { enableProdMode } from '@angular/core';
import { AppComponent, OverviewPage, PackingListPage, AccountOverviewPage } from './app';
if (process.env.ENV === 'production') {
  enableProdMode();
}
bootstrap(AccountOverviewPage,[])
