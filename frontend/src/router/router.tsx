import NotFound from '@/pages/NotFound';
import Root from '@/pages/Root';
import Main from '@/pages/Main';
import Result from '@/pages/Result';
import Custom from '@/pages/Custom';

import { createBrowserRouter } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root></Root>,
    errorElement: <NotFound></NotFound>,
    children: [
      { path: '/', element: <Main></Main> },
      { path: '/custom', element: <Custom></Custom> },
      { path: '/result', element: <Result></Result> },
    ],
  },
]);

export default router;
