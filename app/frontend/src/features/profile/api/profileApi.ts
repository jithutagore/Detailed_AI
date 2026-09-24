import { apiGet, apiPut } from "../../../lib/apiClient";

export type Profile = {
  id: number;
  email: string;
  username: string;
  first_name: string;
  last_name: string;
};

export const getProfile = () => apiGet<Profile>("/profile");

export const updateProfile = (firstName: string, lastName: string) =>
  apiPut<Profile>("/profile", { first_name: firstName, last_name: lastName });
