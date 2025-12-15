import { Grid, Card, CardContent, Typography } from "@mui/material";
import { useRiders } from "../hooks/useRiders";

const Riders: React.FC = () => {
  const { riders, loading, error } = useRiders();

  if (loading) return <Typography>Cargando riders...</Typography>;
  if (error) return <Typography color="error">{error}</Typography>;

  return (
    <div>
      <Typography variant="h3" gutterBottom textAlign="center" sx={{ my: 4 }}>
        Riders Page 🏍️
      </Typography>

      <Grid container spacing={3} justifyContent="center">
        {riders.map((rider) => (
          <Grid key={rider.id} size={{ xs: 12, sm: 6, md: 4, lg: 3 }}>
            {" "}
            <Card
              sx={{
                minHeight: 150,
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                textAlign: "center",
                p: 2,
              }}
            >
              <CardContent>
                <Typography variant="h5" fontWeight="bold">
                  {rider.name} {rider.surname}
                </Typography>
                <Typography variant="subtitle1" color="text.secondary">
                  #{rider.number}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {rider.country}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default Riders;
