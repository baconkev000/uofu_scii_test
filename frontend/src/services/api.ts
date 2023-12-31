import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8000/",
  headers: {
    "Content-Type": "application/json",
  },
});
export default instance;

export class APIService {
  /**
   * First step login for Token Auth
   * @param email
   * @param password
   * @returns Promise
   */
  static login = async (email: string, password: string) =>
    instance.post(`auth-token`, { email: email, password: password });

  /**
   * Get Players
   * @returns Promise
   */
  static getPlayers = async () => instance.get("api/players/");

  /**
   * Get Player By Name
   * @returns Promise
   */
  static getPlayerByName = async () => instance.get("api/playesrs/{name}");

  /**
   * Get Attributes
   * @returns Promise
   */
  static getAttributes = async () => instance.get("api/attributes/");

  /**
   * Get Clubs
   * @returns Promise
   */
  static getClubs = async () => instance.get("api/clubs/");
}
