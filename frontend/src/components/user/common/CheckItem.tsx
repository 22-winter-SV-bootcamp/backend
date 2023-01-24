import { Button, Typography } from '@mui/material';
import { Box } from '@mui/system';

const CheckItem = ({ info, title, setModal, setSelect }: any) => {
  return (
    <Box
      sx={{
        width: '100%',
        height: 50,
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
      }}
    >
      <Typography variant="h4">{title}</Typography>
      <Button
        onClick={() => {
          setModal(true);
          setSelect(title);
        }}
      >
        <Box
          sx={{ objectFit: 'fill' }}
          component="img"
          height={50}
          width={50}
          src={
            title === 'background'
              ? `src/assets/custom/${title}/${info[title]}.png`
              : `src/assets/custom/${info.gender}/${title}/${info[title]}.svg`
          }
          alt={info[title]}
        ></Box>
      </Button>
    </Box>
  );
};

export default CheckItem;
