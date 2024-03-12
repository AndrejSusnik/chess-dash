/* @refresh reload */
import { render } from 'solid-js/web';
import { Router, Route } from '@solidjs/router';

import './index.css';
import App from './App';
import Categories from './pages/Categories';
import Participants from './pages/Participants';
import Results from './pages/Results';

const root = document.getElementById('root');

if (import.meta.env.DEV && !(root instanceof HTMLElement)) {
  throw new Error(
    'Root element not found. Did you forget to add it to your index.html? Or maybe the id attribute got misspelled?',
  );
}

render(() => (
  <Router>
    <Route path="/" component={App} />
    <Route path="/categories" component={Categories} />
    <Route path="/participants" component={Participants} />
    <Route path="/results" component={Results} />
  </Router>
) ,root!);
