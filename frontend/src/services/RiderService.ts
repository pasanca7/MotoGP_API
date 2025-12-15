import api from "./axios";
import type { Rider, RidersResponseFromApi } from "../types/Rider";

export const getchAllRiders = async () => {
  const apiResponse = await fetchAllRiders();
  return mapFromApiToRider(apiResponse);
};

export const fetchAllRiders = async (): Promise<RidersResponseFromApi> => {
  const response = await api.get("/riders/");
  return response.data;
};

export const mapFromApiToRider = (
  apiResponse: RidersResponseFromApi
): Rider[] => {
  return apiResponse.map((riderApi) => {
    return {
      id: riderApi.id,
      name: riderApi.name,
      surname: riderApi.surname,
      number: riderApi.number,
      country: riderApi.country,
    };
  });
};
