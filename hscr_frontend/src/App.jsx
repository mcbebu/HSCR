import { useState } from "react";
import "./App.css";
import NinjaAppBar from "./NinjaAppBar";
import CallIcon from "@mui/icons-material/Call";
import { Box, Grid, Typography, Card, Avatar, Button } from "@mui/material";

function App() {
  const [base64Encoded, setBase64Encoded] = useState("");

  useEffect(() => {
    fetch("http://190.92.221.226/predict")
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setBase64Encoded(data.image_bytes);
      });
  }, []);

  return (
    <>
      <NinjaAppBar />
      <Grid
        container
        spacing={0}
        sx={{ display: "flex", justifyContent: "center" }}>
        <Grid
          item
          xs={12}
          s={12}
          md={12}
          lg={5}
          sx={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            flexDirection: "column",
            boxShadow: 4,
            borderRadius: 4,
            p: 2,
            m: 3,
          }}>
          <Typography variant="h5" sx={{ textAlign: "center" }}>
            View from Yio Chu Kang Sorting Hub
          </Typography>
          <Typography
            variant="subtitle"
            sx={{ textAlign: "center", color: "grey", mb: 1 }}>
            Last updated: 26/02/2023 03:17 AM
          </Typography>
          <Box sx={{ alignItems: "center", justifyContent: "center" }}>
            <img src={`data:image/png;base64,${base64Encoded}`}></img>
          </Box>
        </Grid>
        <Grid
          item
          xs={12}
          s={12}
          md={12}
          lg={5}
          sx={{
            display: "flex",
            alignItems: "center",
            flexDirection: "column",
            boxShadow: 4,
            borderRadius: 4,
            px: 5,
            py: 2,
            m: 3,
          }}>
          <Typography variant="h5" sx={{ textAlign: "center", mb: 3 }}>
            Alerts & Monitoring
          </Typography>
          <Grid container spacing={2} sx={{ justifyContent: "center" }}>
            <Grid item xs={6}>
              <Card variant="outlined" sx={{ p: 1.5 }}>
                <Typography variant="h6">
                  Hub Capacity: <span style={{ color: "green" }}>10%</span>
                </Typography>
              </Card>
            </Grid>
            <Grid item xs={6}>
              <Card variant="outlined" sx={{ p: 1.5 }}>
                <Typography variant="h6">
                  Available Grids: <span style={{ color: "green" }}>9/10</span>
                </Typography>
              </Card>
            </Grid>
          </Grid>
          <Typography variant="h6" sx={{ mt: 3 }}>
            Drivers En Route
          </Typography>
          <Card
            variant="outlined"
            sx={{
              width: 1,
              p: 1,
              mt: 2,
              display: "flex",
              alignItems: "center",
            }}>
            <Avatar alt="" sx={{ width: 32, height: 32, mr: 1.5 }}>
              J
            </Avatar>
            <Box>
              <Typography variant="h6">Jane Doe</Typography>
              <Typography variant="subtitle">Parcels: 66</Typography>
            </Box>
            <Button
              variant="contained"
              sx={{
                ml: "auto",
                color: "white",
                backgroundColor: "rgb(194, 0, 47)",
                maxHeight: 38,
                "&:hover": { backgroundColor: "#d80135" },
              }}>
              <CallIcon></CallIcon>Contact
            </Button>
          </Card>
          <Card
            variant="outlined"
            sx={{
              width: 1,
              p: 1,
              mt: 2,
              display: "flex",
              alignItems: "center",
            }}>
            <Avatar alt="" sx={{ width: 32, height: 32, mr: 1.5 }}>
              J
            </Avatar>
            <Box>
              <Typography variant="h6">Joseph Prince</Typography>
              <Typography variant="subtitle">Parcels: 39</Typography>
            </Box>
            <Button
              variant="contained"
              sx={{
                ml: "auto",
                color: "white",
                backgroundColor: "rgb(194, 0, 47)",
                maxHeight: 38,
                "&:hover": { backgroundColor: "#d80135" },
              }}>
              <CallIcon></CallIcon>Contact
            </Button>
          </Card>
          <Card
            variant="outlined"
            sx={{
              width: 1,
              p: 1,
              mt: 2,
              display: "flex",
              alignItems: "center",
            }}>
            <Avatar alt="" sx={{ width: 32, height: 32, mr: 1.5 }}>
              J
            </Avatar>
            <Box>
              <Typography variant="h6">Jeff Malone</Typography>
              <Typography variant="subtitle">Parcels: 40</Typography>
            </Box>
            <Button
              variant="contained"
              sx={{
                ml: "auto",
                color: "white",
                backgroundColor: "rgb(194, 0, 47)",
                maxHeight: 38,
                "&:hover": { backgroundColor: "#d80135" },
              }}>
              <CallIcon></CallIcon>Contact
            </Button>
          </Card>
          <Card
            variant="outlined"
            sx={{
              width: 1,
              p: 1,
              mt: 2,
              display: "flex",
              alignItems: "center",
            }}>
            <Avatar alt="" sx={{ width: 32, height: 32, mr: 1.5 }}>
              J
            </Avatar>
            <Box>
              <Typography variant="h6">John Mayer</Typography>
              <Typography variant="subtitle">Parcels: 80</Typography>
            </Box>
            <Button
              variant="contained"
              sx={{
                ml: "auto",
                color: "white",
                backgroundColor: "rgb(194, 0, 47)",
                maxHeight: 38,
                "&:hover": { backgroundColor: "#d80135" },
              }}>
              <CallIcon></CallIcon>Contact
            </Button>
          </Card>
        </Grid>
      </Grid>
    </>
  );
}

export default App;
