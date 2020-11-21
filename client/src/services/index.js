import axios from "axios";

export function getAxiosInstance(token, responseType, contentType) {
  return axios.create({
    headers: {
      "Content-Type": contentType || "application/json",
      Authorization: token ? `Bearer ${token}` : undefined,
    },
    responseType: responseType,
  });
}
