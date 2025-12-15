export interface Rider {
  id: number;
  name: string;
  surname: string;
  number: number;
  country: string;
}

export type RidersResponseFromApi = Array<Rider>;
