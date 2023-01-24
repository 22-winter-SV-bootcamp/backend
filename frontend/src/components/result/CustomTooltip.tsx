import { styled, Tooltip, tooltipClasses, TooltipProps } from '@mui/material';

export const CustomTooltip = styled(({ className, ...props }: TooltipProps) => (
  <Tooltip {...props} classes={{ popper: className }} />
))(({ theme }) => ({
  [`& .${tooltipClasses.arrow}`]: {
    color: '#4caf50',
    '&::before': {
      backgroundColor: '#4caf50',
      border: '1px solid #dadde9',
    },
  },
  [`& .${tooltipClasses.tooltip}`]: {
    backgroundColor: '#4caf50',
    color: '#ffffff',
    maxWidth: 220,
    fontSize: theme.typography.pxToRem(15),
    border: '1px solid #dadde9',
    boxShadow: theme.shadows[1],
    display: 'flex',
  },
}));
