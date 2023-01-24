import { Box } from '@mui/system';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { RouterProvider } from 'react-router-dom';
import { EasterEgg } from './components/user/EasterEgg';
import Simpson from './assets/Simpson.png';
import Simpson2 from './assets/Simpson2.png';
import Simpson3 from './assets/Simpson3.png';
import SimpsonDoh from './assets/SimpsonDoh.jpg';
import SimpsonDoh2 from './assets/SimpsonDoh2.png';

import router from './router/router';

function App() {
  return (
    <Box sx={{ width: 1, height: 1 }}>
      <RouterProvider router={router}></RouterProvider>
    </Box>
  );
}
export default App;

{
  /* <EasterEgg
        text="Are you Homer Simpson?"
        textSize="4.0"
        img1={Simpson}
        img2={Simpson2}
        img3={Simpson3}
      /> */
}
{
  /* <EasterEgg
        text="AI failed to determine the top & bottom."
        // textSize="3.5"
        textSize="3.5"
        img1={SimpsonDoh}
        img2={SimpsonDoh}
        img3={SimpsonDoh2}
      /> */
}
