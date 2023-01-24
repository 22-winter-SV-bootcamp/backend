import { useTheme } from '@mui/material';
import { Box } from '@mui/system';
import { ImageInfo } from './types';

interface ImageComponentProps {
  imageState: ImageInfo;
  isEnd: boolean;
}

export function ImageComponent(props: ImageComponentProps) {
  const { imageState, isEnd } = props;
  const theme = useTheme();

  return (
    <Box
      sx={{
        width: 1,
        mr: 0,
        display: 'flex',
        justifyContent: 'center',
        flexDirection: 'column',
        alignItems: 'center',
        [theme.breakpoints.between('mobile', 'tablet')]: {
          px: 2,
          pl: isEnd ? 0 : 2,
        },
        [theme.breakpoints.between('tablet', 'laptop')]: {
          px: 2,
          pl: isEnd ? 0 : 2,
        },
        [theme.breakpoints.up('laptop')]: {
          px: 4,
          pl: isEnd ? 0 : 4,
        },
      }}
    >
      <Box component={'img'} src={imageState?.url ?? ''} sx={{ width: 1 }} />
      <Box sx={{ pt: 4, fontSize: 50 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', fontSize: '3rem' }}>
          <Box sx={{ fontSize: '4rem' }}>{imageState?.count}</Box>
          ’s pick
        </Box>
      </Box>
    </Box>
  );
}
