import React from 'react';
import { AppBar, Box, Toolbar, Container, Typography } from '@mui/material';
import NinjaParcel from './assets/ninja_parcel.png'

function NinjaAppBar() {

  return (
    <>
      <AppBar position="static" sx={{ bgcolor: "#212125", color: "white" }}>
        <Container maxWidth="xl" sx={{ width: { xs: 1, sm: 0.9 } }}>
          <Toolbar disableGutters style={{ display: 'flex', justifyContent: 'center' }}>
            <Box sx={{ flexGrow: 1, display: 'flex', justifyContent: 'center' }}>
                <img src={NinjaParcel} alt="Ninja Parcel" style={{ height: 50 }} />
                <Typography>Ninja Hub Status</Typography>
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
    </>
  );
}

export default NinjaAppBar;
