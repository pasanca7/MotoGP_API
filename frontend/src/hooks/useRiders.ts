import { useEffect, useState } from "react";
import type { Rider } from "../types/Rider";
import { getchAllRiders } from "../services/RiderService";

export function useRiders() {
  const [riders, setRiders] = useState<Rider[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getchAllRiders()
      .then(setRiders)
      .catch(() => {
        setError("Error loading riders");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return {
    riders,
    loading,
    error,
  };
}
