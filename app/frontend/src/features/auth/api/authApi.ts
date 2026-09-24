import { apiPost } from "../../../lib/apiClient";

export type User = {
  id: number;
  email: string;
  username: string;
  first_name: string;
  last_name: string;
  created_at: string;
};

export type LoginResponse = {
  access_token: string;
  token_type: string;
  expires_in: number;
  user: User;
};

export function registerUser(
  username: string,
  firstName: string,
  lastName: string,
  email: string,
  password: string,
) {
  return apiPost<User>("/auth/register", {
    username,
    first_name: firstName,
    last_name: lastName,
    email,
    password,
  });
}

export function loginUser(identifier: string, password: string) {
  return apiPost<LoginResponse>("/auth/login", { identifier, password });
}
