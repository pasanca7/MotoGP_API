import {
  BrowserRouter,
  Routes,
  Route,
  Link as RouterLink,
} from "react-router-dom";
import { AppBar, Toolbar, Typography, Button, Container } from "@mui/material";
import Home from "./pages/Home";
import Riders from "./pages/Riders";
import Teams from "./pages/Teams";

function App() {
  return (
    <BrowserRouter>
      <AppBar
        position="static"
        sx={{ backgroundColor: "#111827" /* gris oscuro */ }}
      >
        <Container maxWidth="lg">
          <Toolbar
            disableGutters
            sx={{ display: "flex", justifyContent: "space-between" }}
          >
            <Typography
              variant="h6"
              sx={{ color: "#ef4444", fontWeight: "bold" }}
            >
              MotoGP
            </Typography>

            <div>
              <Button
                component={RouterLink}
                to="/"
                sx={{
                  color: "white",
                  "&:hover": { color: "#f87171" },
                  textTransform: "none",
                }}
              >
                Home
              </Button>
              <Button
                component={RouterLink}
                to="/riders"
                sx={{
                  color: "white",
                  "&:hover": { color: "#f87171" },
                  textTransform: "none",
                }}
              >
                Riders
              </Button>
              <Button
                component={RouterLink}
                to="/teams"
                sx={{
                  color: "white",
                  "&:hover": { color: "#f87171" },
                  textTransform: "none",
                }}
              >
                Teams
              </Button>
            </div>
          </Toolbar>
        </Container>
      </AppBar>

      <Container maxWidth="lg" sx={{ mt: 4 }}>
        <Routes>
          <Route index element={<Home />} />
          <Route path="/riders" element={<Riders />} />
          <Route path="/teams" element={<Teams />} />
        </Routes>
      </Container>
    </BrowserRouter>
  );
}

export default App;
